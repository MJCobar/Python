import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I

g = 9.81
pi = 3.14

s1 = 0.95 ##Simulating a fault
s1hat0 = 1.0  ##Fault detection algorithm
s2 = 0.8
s2hat0 = 1.0

m = 5.
Ix = 1.

#Initial Conditions
#Altitude
z0 = 0.
zdot0 = 0.
#Roll
phi0 = 45.*(np.pi/180.)
phidot0 = 0.

#Command Signals
#Altitude
zc = 10.0
zdotc = 0.0
zddotc = 0.0
#Roll
phic = 0.0
phidotc = 0.0
phiddotc = 0.0

def Derivatives(state,t):
    z = state[0]
    phi = state[1]
    s1hat = state[2]
    s2hat = state[3]
    zdot = state[4]
    phidot = state[5]
    #state = [z,phi,s1hat,s2hat,zdot,phidot]]
    
    s1hatdot = 0.
    s2hatdot = 0.
    
    M = np.asarray([[m,0],[0,Ix]])
    #print(M)
    H = np.asarray([[-1*s1,-1*s2],[-1*s1,1*s2]])
    Hhat = np.asarray([[-1*s1hat,-1*s2hat],[-1*s1hat,1*s2hat]])
    #print(H)
    f = np.asarray([m*g,0])
    #print(f)
    kp = np.asarray([[1,0],[0,1]])
    #print(kp)
    kd = np.asarray([[1,0],[0,1]])
    #print(kd)
    qdot = np.asarray([zdot,phidot])
    #print(qdot)
    q = np.asarray([z,phi])
    #print(q)
    qddotc = np.asarray([zddotc,phiddotc])
    #print(qddotc)
    qdotc = np.asarray([zdotc,phidotc])
    #print(qdotc)
    qc = np.asarray([zc,phic])
    #print(qc)
    gamma = qddotc - np.matmul(kp,(q-qc)) - np.matmul(kd,(qdot-qdotc))
    #print('gamma=',gamma)
    Minv = np.linalg.inv(M)
    #print('Minv=',Minv)
    invMH = np.matmul(Minv,H)
    invMHhat = np.matmul(Minv,Hhat)
    #print(invMH)
    GAUSSMATRIXHAT = np.linalg.inv(invMHhat)
    #print(GAUSSMATRIX)
    chi = np.matmul(GAUSSMATRIXHAT,(gamma - f)) ##This is the controller with the unknown states
    #print('chi=',chi)
    qddot = np.matmul(invMH,chi) + f ##These are the dynamics with known states
    #print('qddot=',qddot)
    statedot = np.hstack(([zdot,phidot,s1hatdot,s2hatdot],qddot))
    #print('statedot = ',statedot)
    return statedot

tout = np.linspace(0,100,10000)
stateinit = np.asarray([z0,phi0,s1hat0,s2hat0,zdot0,phidot0])
stateout = I.odeint(Derivatives,stateinit,tout)

plt.figure()
plt.plot(tout,stateout[:,0],label='Z')
plt.plot(tout,stateout[:,4],label='Zdot')
plt.xlabel('Time')
plt.ylabel('Altitude')
plt.legend()
plt.grid()

plt.figure()
plt.plot(tout,stateout[:,1],label='Phi')
plt.plot(tout,stateout[:,5],label='Phidot')
plt.xlabel('Time')
plt.ylabel('Roll')
plt.legend()
plt.grid()

plt.figure()
plt.plot(tout,stateout[:,2],label='s1hat')
plt.plot(tout,stateout[:,3],label='s2hat')
plt.xlabel('Time')
plt.ylabel('Faults')
plt.legend()
plt.grid()
plt.show()