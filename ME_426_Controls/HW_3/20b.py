import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as ctl
import scipy.signal as S

plt.close("all")

def Devs(state,t):
    x = state[0]
    xdot = state[1]
    xddot = (5*np.sin(3*t))-(6*xdot)-(8*x)
    dstatedt = np.asarray([xdot,xddot])
    return dstatedt

############################################################

time = np.linspace(0,10,10000)
xinit = np.asarray([0,0])
x_num = I.odeint(Devs,xinit,time)
plt.plot(time,x_num[:,0],label='Numerical')

############################################################

A = 0.58
B = -0.3
x_analy = (A*np.exp(-2*time))+(B*np.exp(-4*time))-(0.015*np.sin(3*time))-(0.277*np.cos(3*time))
line,=plt.plot(time,x_analy,label='Analytical')
line.set_dashes([2,2])
plt.legend()
plt.grid()
plt.show()