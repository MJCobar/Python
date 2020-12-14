import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as C
import scipy.signal as S

def Derivatives(state,t):
    ##States
    x = state[0]
    xdot = state[1]
    xm = state[2]
    xmdot = state[3]
    mhat = state[4]
    
    ###Parameters
    m = 5.0
    
    ###Error Signals
    xtilde = x - xm
    xtildedot = xdot - xmdot
    
    ###Model Dynamics
    xmddot = 0.
    
    ###Control
    kd = 1.
    kp = 1.
    v = xmddot - kd*xtildedot - kp*xtilde
    u = mhat*v
    
    ###Plant Dynamics and Kinematics
    #xdot already defined
    xddot = u/m
    
    e = mhat*xddot - u
    integral = (xddot**2)*200
    P = 1/integral
    mhatdot = -P*xddot*e 
    
    return np.asarray([xdot,xddot,xmdot,xmddot,mhatdot])
    
##Time vector
tout = np.linspace(0,1000,10000)
##Initial Conditions
x0 = 0.
xdot0 = 0.
xm0 = 1.
xmdot0 = 0.
mhat0 = 1.
state_initial = np.asarray([x0,xdot0,xm0,xmdot0,mhat0])
state_out = I.odeint(Derivatives,state_initial,tout)

###Extract my states
xout = state_out[:,0]
xmout = state_out[:,2]
mhatout = state_out[:,4]

plt.figure()
plt.plot(tout,xout,label='X')
plt.plot(tout,xmout,label='Xm')
plt.xlabel('Time (s)')
plt.ylabel('Model trajectory')
plt.legend()
plt.grid()

plt.figure()
plt.plot(tout,xout-xmout)
plt.xlabel('Time (s)')
plt.ylabel('Error')
plt.grid()

plt.figure()
plt.plot(tout,mhatout)
plt.xlabel('Time (s)')
plt.ylabel('Mass (kg)')
plt.grid()

plt.show()