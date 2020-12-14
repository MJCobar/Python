import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as C
import scipy.signal as S

rx = 0.33
Iy = 0.0545
h3 = (2.0*rx)/Iy
pi = 3.14
theta_c = 0.0
thetadot_c = 0.0
thetaddot_c = 0.0
theta0 = -3.0*(pi/180.0)
thetadot0 = 0.0

def Derivatives(theta,t):
    theta1 = theta[0]
    theta2 = theta[1]
    
    ftheta2 = 0.0
    kp3 = 1.0
    kd3 = 1.0
    gamma = thetaddot_c - kp3*(theta1 - theta_c) - kd3*(theta2 - thetadot_c)
    T_theta = (1/h3)*gamma
    theta1dot = theta2
    theta2dot = h3*T_theta

    thetadot = np.asarray([theta1dot,theta2dot])

    return thetadot

plt.close("all")

tout = np.linspace(0,20,1000)
thetainitial = np.asarray([theta0,thetadot0])
thetaout = I.odeint(Derivatives,thetainitial,tout)
theta1out = thetaout[:,0]
theta2out = thetaout[:,1]
plt.figure()
plt.plot(theta1out,theta2out)
plt.plot(theta1out[0],theta2out[0],'b*')
plt.plot(theta1out[-1],theta2out[-1],'rs')
plt.xlabel('theta1')
plt.ylabel('theta2')
plt.grid()

plt.figure()
plt.plot(tout,theta1out)
plt.xlabel('time')
plt.ylabel('theta1')
plt.grid()

plt.figure()
plt.plot(tout,theta2out)
plt.xlabel('time')
plt.ylabel('theta2')
plt.grid()
plt.show()