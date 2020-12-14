import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as C
import scipy.signal as S

ry = 0.33
Ix = 0.0545
h2 = (2.0*ry)/Ix
pi = 3.14
phi_c = 0.0
phidot_c = 0.0
phiddot_c = 0.0
phi0 = 10.0*(pi/180.0)
phidot0 = 0.0

def Derivatives(phi,t):
    phi1 = phi[0]
    phi2 = phi[1]
    
    fphi2 = 0.0
    kp2 = 1.0
    kd2 = 1.0
    gamma = phiddot_c - kp2*(phi1 - phi_c) - kd2*(phi2 - phidot_c)
    T_phi = (1/h2)*(gamma - fphi2)
    phi1dot = phi2
    phi2dot = h2*T_phi

    phidot = np.asarray([phi1dot,phi2dot])

    return phidot

plt.close("all")

tout = np.linspace(0,20,1000)
phiinitial = np.asarray([phi0,phidot0])
phiout = I.odeint(Derivatives,phiinitial,tout)
phi1out = phiout[:,0]
phi2out = phiout[:,1]
plt.figure()
plt.plot(phi1out,phi2out)
plt.plot(phi1out[0],phi2out[0],'b*')
plt.plot(phi1out[-1],phi2out[-1],'rs')
plt.xlabel('phi1')
plt.ylabel('phi2')
plt.grid()

plt.figure()
plt.plot(tout,phi1out)
plt.xlabel('time')
plt.ylabel('phi1')
plt.grid()

plt.figure()
plt.plot(tout,phi2out)
plt.xlabel('time')
plt.ylabel('phi2')
plt.grid()
plt.show()