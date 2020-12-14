import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I

def Derivatives(state,t):
    ##States
    x = state[0]
    xdot = state[1]
    xm = state[2]
    xmdot = state[3]
    ahat = state[4]
    
    ###Parameters
    f = -9.81 #N
    g = 0.5 #Represents half a fault
    m = 1.0 #kg
    r = 10. #m
    
    ###Error Signals
    e = x - xm
    
    ###Model Dynamics
    Ts = 10.0
    zed = 0.8
    wn = 4.6/(Ts*zed)
    xmddot = -2*zed*wn*xmdot - (wn**2)*xm + (wn**2)*r
    
    ###Control
    v = (wn**2)*(r - x) - 2*zed*wn*xdot - (f/m)
    gamma = 0.001
    ahatdot = -gamma*np.sign(g/((wn**2)*m))*e*v
    u = ahat*v
    
    ###Plant Dynamics and Kinematics
    xddot = (f/m) + (g/m)*u
    
    return np.asarray([xdot,xddot,xmdot,xmddot,ahatdot])
    

plt.close("all")

##Time vector
tout = np.linspace(0,200,10000)
##Initial Conditions
x0 = 0. 
xdot0 = 0. 
xm0 = 0. 
xmdot0 = 0.
ahat0 = 1. 
state_initial = np.asarray([x0,xdot0,xm0,xmdot0,ahat0])
state_out = I.odeint(Derivatives,state_initial,tout)

###Extract my states
xout = state_out[:,0]
xmout = state_out[:,2]
ahatout = state_out[:,4]

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
plt.plot(tout,ahatout)
plt.xlabel('Time (s)')
plt.ylabel('Faults')
plt.grid()

plt.show()