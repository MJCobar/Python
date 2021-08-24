import sys, time

import navio.rcinput
import navio.util

navio.util.check_apm()

rcin = navio.rcinput.RCInput()

SERVO_MAX = 2015.
SERVO_MID = 1507.
SERVO_MIN = 993.

DIFFERENTIAL_LEFT = -1.0
DIFFERENTIAL_RIGHT = 1.0

while (True):
    #Read signals from the transmitter
    yawrc = rcin.read(0)
    #print(type(yaw))
    pitchrc = rcin.read(1)
    throttlerc = rcin.read(2)
    rollrc = rcin.read(3)
    aileron_switch = rcin.read(4) #Next to 3-pos switch
    three_pos = rcin.read(5) #3-position switch on top right
    #If you need to set any other switch, check menu 5/10 on transmitter
    #Switch names can be found on FS-TH9X user manual online
    #print(roll,pitch,yaw,throttle)

    #Convert signals from transmitter to floats
    yaw = float(yawrc)
    pitch = float(pitchrc)
    roll = float(rollrc)
    throttle = float(throttlerc)
    arm_switch = float(aileron_switch)
    mode_switch = float(three_pos)

    #Need to use differential thrust since there are two independently driven wheels
    steering = (yaw - SERVO_MID)/(SERVO_MID - SERVO_MIN)
    motor_left = throttle + DIFFERENTIAL_LEFT*steering*(SERVO_MAX - SERVO_MID)
    motor_right = throttle + DIFFERENTIAL_RIGHT*steering*(SERVO_MAX - SERVO_MID)
    print(yaw,steering,throttle,motor_left,motor_right)

    #Send signals to the ESC
    
