import numpy as np
import matplotlib.pyplot as plt
import control as ctl

plt.close("all")

Step = 30*(np.pi/180)

plt.figure()
G_step = ctl.tf([-0.125*Step,-0.054375*Step],[1,1.456,0.29488,0.020787])
time_step = np.linspace(0,80,1000)
time_step,yout_step = ctl.step_response(G_step,time_step)
plt.plot(time_step,yout_step,label='Open-Loop Dynamics with Step')

G_act_step = ctl.tf([-0.25*Step,-0.10875*Step],[1,3.456,3.20688,0.610547,0.041574])
time_act_step = np.linspace(0,80,1000)
time_act_step,yout_act_step = ctl.step_response(G_act_step,time_act_step)
plt.plot(time_act_step,yout_act_step,label='Open-Loop Dynamics with Actuator and Step')

plt.xlabel('Time (sec)')
plt.ylabel('Pitch (rad)')
plt.legend()
plt.grid()

plt.figure()
G_impulse = ctl.tf([-0.125,-0.054375],[1,1.456,0.29488,0.020787])
time_impulse = np.linspace(0,80,1000)
time_impulse,yout_impulse = ctl.impulse_response(G_impulse,time_impulse)
plt.plot(time_impulse,yout_impulse,label='Impulse Dynamics')

plt.xlabel('Time (sec)')
plt.ylabel('Pitch (rad)')
plt.legend()
plt.grid()

plt.figure()
Actuator = ctl.tf([2*Step],[1,2])
time_actuator = np.linspace(0,80,1000)
time_actuator,yout_actuator = ctl.step_response(Actuator,time_actuator)
plt.plot(time_actuator,yout_actuator,label='Pitch Angle of Elevator')

plt.xlabel('Time (sec)')
plt.ylabel('Pitch (rad)')
plt.legend()
plt.grid()

plt.figure()
k_1 = 13.0
k_2 = 28.0
k_3 = -0.01
G_inner = ctl.tf([-0.25,-0.10875],[1,3.456,3.20688+0.25*k_2,0.610547+0.10875*k_2,0.041574])
Controller = ctl.tf([-k_1,k_3],[1,0])
G_closed = Controller*G_inner/(1+Controller*G_inner)
G_closed_step = G_closed*Step
print(G_closed)

time_closed = np.linspace(0,15,3000)
time_closed,yout_closed = ctl.step_response(G_closed_step,time_closed)
plt.plot(time_closed,yout_closed,label='Closed-Loop Dynamics with Control')

plt.xlabel('Time (sec)')
plt.ylabel('Pitch (rad)')
plt.legend()
plt.grid()
plt.show()

#This code was originally downloaded from the ME 426 Google Drive. The code was created by Dr. Montalvo. I have adapted this code
#for project 4. I had Dr. Montalvo help me with this code. I am not sure how to reference I live person.