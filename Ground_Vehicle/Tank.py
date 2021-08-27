import sys, time

import navio.rcinput
import navio.util
import navio.pwm

navio.util.check_apm()

rcin = navio.rcinput.RCInput()

#These values come from reading the transmitter signals
SERVO_MAX = 2015./1000. #milliseconds
SERVO_MID = 1504./1000. #milliseconds
SERVO_MIN = 993./1000. #milliseconds

Motor_left = 0 #This is the first PWM Channel (Channel 1 on Navio2)
Motor_right = 1 #This is the second PWM Channel (Channel 2 on Navio2)

DIFFERENTIAL = 1.0

#Setup PWM output
with navio.pwm.PWM(Motor_left) as pwmLeft:
    pwmLeft.set_period(50)
    pwmLeft.enable()
    
    with navio.pwm.PWM(Motor_right) as pwmRight:
        pwmRight.set_period(50)
        pwmRight.enable()

        while (True):
            #Read signals from the transmitter
            yawrc = rcin.read(0)
            #print(type(yaw))
            pitchrc = rcin.read(1)
            throttlerc = rcin.read(2)
            rollrc = rcin.read(3)
            #If you need to set any other switch, check menu 5/10 on transmitter
            #Switch names can be found on FS-TH9X user manual online
            aileron_switch = rcin.read(4) #Next to 3-pos switch
            three_pos = rcin.read(5) #3-position switch on top right
            #print(yawrc,throttlerc)
            
            #Convert signals from transmitter to floats and from micro to milliseconds
            yaw = float(yawrc)/1000.
            pitch = float(pitchrc)/1000.
            roll = float(rollrc)/1000.
            throttle = float(throttlerc)/1000.
            arm_switch = float(aileron_switch)/1000.
            mode_switch = float(three_pos)/1000.

            #Need to use differential thrust since there are two independently driven wheels
            diff_left = SERVO_MID + (SERVO_MID - pitch) + DIFFERENTIAL * (roll - SERVO_MID)
            #Need a saturation block so I don't burn up the motors
            if(diff_left < SERVO_MIN):
                diff_left = SERVO_MIN
            if(diff_left > SERVO_MAX):
                diff_left = SERVO_MAX
            diff_right = pitch + DIFFERENTIAL * (roll-SERVO_MID)
            #Need a saturation block so I don't burn up the motors
            if(diff_right < SERVO_MIN):
                diff_right = SERVO_MIN
            if(diff_right > SERVO_MAX):
                diff_right = SERVO_MAX
            f_roll = "{:.2f}".format(roll)
            f_pitch = "{:.2f}".format(pitch)
            f_diff_left = "{:.2f}".format(diff_left)
            f_diff_right = "{:.2f}".format(diff_right)
            print(f_roll,f_pitch,f_diff_left,f_diff_right)

            #Send signals to the ESC
            pwmLeft.set_duty_cycle(diff_left)
            pwmRight.set_duty_cycle(diff_right)
            #time.sleep(1)
