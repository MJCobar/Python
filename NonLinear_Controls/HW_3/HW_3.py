import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as ctl

def Derivatives(xstate,t):
    theta = xstate[0]
    thetadot = xstate[1] 
    
    thetadbldot = -thetadot**2 - 0.5*theta
    
    xstatedot = np.asarray([thetadot,thetadbldot])
    
    return xstatedot

tout = np.linspace(0,60,1000)
xstateinitial = np.asarray([0.01,0])
stateout = I.odeint(Derivatives,xstateinitial,tout)

thetaout = stateout[:,0]
thetadotout = stateout[:,1]
plt.plot(tout,thetaout)

plt.figure()
for theta in np.arange(-np.pi/4,np.pi/4,0.5):
    for thetadot in np.arange(-np.pi/4,np.pi/4,0.5):
        xstateinitial = np.asarray([theta,thetadot])
        stateout = I.odeint(Derivatives,xstateinitial,tout)
        thetaout = stateout[:,0]
        thetadotout = stateout[:,1]
        plt.plot(thetaout,thetadotout)
        #plt.pause(0.0001)
        plt.axis([-np.pi,np.pi,-np.pi,np.pi])

plt.show()