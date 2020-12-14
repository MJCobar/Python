import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as ctl
import scipy.signal as S

plt.close("all")

def Devs(state,t):
    x = state[0]
    xdot = state[1]
    xddot = 10-(25*x)-(8*xdot)
    dstatedt = np.asarray([xdot,xddot])
    return dstatedt

############################################################

time = np.linspace(0,10,10000)
xinit = np.asarray([0,0])
x_num = I.odeint(Devs,xinit,time)
plt.plot(time,x_num[:,0],label='Numerical')

############################################################

A = -2.0/5.0
B = 4.0*A/3.0
x_analy = (A*np.exp(-4*time)*np.cos(3*time))+(B*np.exp(-4*time)*np.sin(3*time))+(2.0/5.0)
line,=plt.plot(time,x_analy,label='Analytical')
line.set_dashes([2,2])
plt.legend()
plt.grid()
plt.show()