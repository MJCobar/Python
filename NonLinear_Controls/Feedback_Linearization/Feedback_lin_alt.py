import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as C
import scipy.signal as S

g = 9.81
m = 0.0502
h1 = 1/m
z_c = 10.0
zdot_c = 0.0
zddot_c = 0.0
z0 = 0.0
zdot0 = 0.0

def Derivatives(z,t):
    z1 = z[0] #z
    z2 = z[1] #zdot
    
    fz2 = -g
    kp1 = 1.0 #kp
    kd1 = 1.0 #kd
    gamma = zddot_c - kp1*(z1 - z_c) - kd1*(z2 - zdot_c)
    T = m*(g+gamma)
    u = h1*(gamma - fz2)
    z1dot = z2
    z2dot = -g + (T/m)

    zdot = np.asarray([z1dot,z2dot])

    return zdot

plt.close("all")

tout = np.linspace(0,20,1000)
zinitial = np.asarray([z0,zdot0])
zout = I.odeint(Derivatives,zinitial,tout)
z1out = zout[:,0]
z2out = zout[:,1]
plt.figure()
plt.plot(z1out,z2out)
plt.plot(z1out[0],z2out[0],'b*')
plt.plot(z1out[-1],z2out[-1],'rs')
plt.xlabel('z1')
plt.ylabel('z2')
plt.grid()

plt.figure()
plt.plot(tout,z1out)
plt.xlabel('time')
plt.ylabel('z1')
plt.grid()

plt.figure()
plt.plot(tout,z2out)
plt.xlabel('time')
plt.ylabel('z2')
plt.grid()
plt.show()