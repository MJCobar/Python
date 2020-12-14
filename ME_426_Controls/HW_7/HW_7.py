import control as ctl
import matplotlib.pyplot as plt
import numpy as np

d = 1.0
I = 1.0

G = ctl.tf([d],[I,0,0])
print(G)
tout = np.linspace(0,100,1000)
tout,yout = ctl.step_response(G,tout)
plt.plot(tout,yout)
plt.ylabel('Theta (rad)')
plt.xlabel('Time (sec)')

kp = 0.04
kd = 2.0/5.0
GCL = ctl.tf([kd*d,kp*d],[I,kd*d,kp*d])
print(GCL)

tout,yout_closed_loop = ctl.step_response(GCL,tout)

plt.figure()
plt.plot(tout,yout_closed_loop)
plt.ylabel('Theta (rad)')
plt.xlabel('Time (sec)')

plt.show()