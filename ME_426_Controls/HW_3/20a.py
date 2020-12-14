import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I

plt.close("all")

def Devs(x,t):
    xdot = (-7*x)+(5*np.cos(2*t))
    return xdot

############################################################

tout = np.linspace(0,10,1000)
zinit = 0.0
xout = I.odeint(Devs,zinit,tout)
plt.plot(tout,xout,label='Numerical')

############################################################

xtot = (5.0/53.0)*((2.0*np.sin(2.0*tout))+(7.0*np.cos(2.0*tout))-(7.0*np.exp(-7.0*tout)))
line,=plt.plot(tout,xtot,color='red',label='Analytical')
line.set_dashes([2,2])
plt.legend(loc='upper left')
plt.grid()
plt.xlabel('Time, sec')
plt.ylabel('Position, m')
plt.show()