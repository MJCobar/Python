import numpy as np
import matplotlib.pyplot as plt
import control as ctl

plt.close("all")

deg_rad = np.pi/180

ydata_deg = np.asarray([20.0,
                        10.0,
                        -9.0,
                        -19.0,
                        -12.0,
                        1.0,
                        16.0,
                        18.0,
                        5.0,
                        -10.0,
                        -17.0,
                        5.0,
                        16.0,
                        14.0,
                        2.0,
                        -10.0,
                        -15.0,
                        -8.0,
                        8.0,
                        14.0,
                        10.0,
                        0.0,
                        -13.0,
                        -4.0,
                        8.0,
                        11.0,
                        9.0,
                        -1.0,
                        -10.0,
                        -9.0,
                        -1.0,
                        8.0,
                        10.0,
                        6.0,
                        -3.0,
                        -9.0,
                        -7.0,
                        0.0,
                        8.0,
                        3.0,
                        -2.0,
                        -7.0,
                        -4.0,
                        0.0,
                        6.0,
                        5.0,
                        1.0,
                        -1.0,
                        -5.0,
                        -2.0,
                        4.0,
                        3.0,
                        1.0,
                        -1.0,
                        -3.0,
                        -2.0,
                        0.0,
                        3.0,
                        2.0,
                        1.0,
                        0.0,
                        -2.0,
                        -1.5,
                        1.5,
                        2.0,
                        1.5,
                        0.5,
                        0.0,
                        -1.0,
                        -0.5,
                        0.25,
                        0.75,
                        1.0,
                        0.25,
                        -0.25,
                        -0.75,
                        0.0,
                        0.25,
                        0.75,
                        0.5,
                        0.0,
                        -0.12,
                        -0.25,
                        -0.12,
                        0.0,
                        0.12,
                        0.25,
                        0.12,
                        0.0,
                        -0.6,
                        -0.12,
                        0.0,
                        0.6,
                        0.12,
                        0.6,
                        0.0,
                        -0.6,
                        -0.3,
                        0.0,
                        0.3,
                        0.6,
                        0.3,
                        0.0,
                        -0.015,
                        -0.3,
                        0.0,
                        0.0,
                        0.0,
                        0.0])
ydata_rad = ydata_deg*deg_rad

xdata = np.linspace(0,27,109)

plt.plot(xdata,ydata_rad,label='Experimental Data')

w_n = 3.41
z = 0.035

G = ctl.tf([0.35,0.7*w_n*z],[1,2*w_n*z,w_n*w_n])

time = np.linspace(0,27,100)

time,yout = ctl.impulse_response(G,time)

plt.plot(time,yout,label='Control Toolbox')

plt.xlabel('Time (sec)')
plt.ylabel('Angular Displacement (rad/s)')
plt.legend()
plt.grid()
plt.show()