import control as ctl
import matplotlib.pyplot as plt
import numpy as np

G1 = ctl.tf([3],[1,4,4])
print(G1)
tout = np.linspace(0,100,1000)
tout,yout = ctl.step_response(G1,tout)
plt.figure()
plt.plot(tout,yout)
plt.ylabel('Angle of Attack (deg)')
plt.xlabel('Time (sec)')

G2 = ctl.tf([-1,-4,14],[3,0,0])
print(G2)
tout,yout = ctl.step_response(G2,tout)
plt.figure()
plt.plot(tout,yout)
plt.ylabel('Height (m)')
plt.xlabel('Time (sec)')

kp = 0.88881519
kd = 0.88881519
GCL = ctl.tf([-kd,-kp-4*kd,14*kd-4*kp,14*kp],[1,4-kd,4-kp-4*kd,14*kd-4*kp,14*kp])
print(GCL)
tout,yout_closed_loop = ctl.step_response(GCL,tout)
plt.figure()
plt.plot(tout,yout_closed_loop)
plt.ylabel('Height (m)')
plt.xlabel('Time (sec)')

plt.show()