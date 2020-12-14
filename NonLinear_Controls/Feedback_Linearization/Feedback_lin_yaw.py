import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as C
import scipy.signal as S

Iz = 0.109
#h4 = 2.0/Iz
pi = 3.14
#psi_c = 0.0
#psidot_c = 0.0
#psiddot_c = 0.0
T = 5.0
R = 5.0
C_t = 0.0335
psi0 = 45.0*(pi/180.0)
psidot0 = 0.0

def Derivatives(psi,t):
    psi1 = psi[0]
    psi2 = psi[1]
    
    fpsi2 = 0.0
    #kp4 = 1.0
    #kd4 = 1.0
    #gamma = psiddot_c - kp4*(psi1 - psi_c) - kd4*(psi2 - psidot_c)
    C_q = (C_t**(3/2))/(np.sqrt(2))
    Q = ((T*R)/C_t)*C_q
    psi1dot = psi2
    psi2dot = h*Q

    psidot = np.asarray([psi1dot,psi2dot])

    return psidot

plt.close("all")

tout = np.linspace(0,20,1000)
psiinitial = np.asarray([psi0,psidot0])
psiout = I.odeint(Derivatives,psiinitial,tout)
psi1out = psiout[:,0]
psi2out = psiout[:,1]
plt.figure()
plt.plot(psi1out,psi2out)
plt.plot(psi1out[0],psi2out[0],'b*')
plt.plot(psi1out[-1],psi2out[-1],'rs')
plt.xlabel('psi1')
plt.ylabel('psi2')
plt.grid()

plt.figure()
plt.plot(tout,psi1out)
plt.xlabel('time')
plt.ylabel('psi1')
plt.grid()

plt.figure()
plt.plot(tout,psi2out)
plt.xlabel('time')
plt.ylabel('psi2')
plt.grid()
plt.show()