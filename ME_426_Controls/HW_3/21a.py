import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as ctl
import scipy.signal as S

plt.close("all")

def Devs(state,t):
    x = state[0]
    xdot = state[1]
    xddot = (np.sin(2.0*t))-(2.0*xdot)-(2.0*x)
    dstatedt = np.asarray([xdot,xddot])
    return dstatedt

############################################################

time = np.linspace(0,10,10000)
xinit = np.asarray([2.0,-3.0])
x_num = I.odeint(Devs,xinit,time)
plt.plot(time,x_num[:,0],label='Numerical')

############################################################

A = 11.0/5.0
B = -6.0/10.0
x_analy = (A*np.exp(-1.0*time)*np.cos(1.0*time))+(B*np.exp(-1.0*time)*np.sin(1.0*time))-((2.0/10.0)*np.cos(2.0*time))-((1.0/10.0)*np.sin(2.0*time))
line,=plt.plot(time,x_analy,label='Analytical')
line.set_dashes([1,1])
plt.legend()
plt.grid()
plt.show()