import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as C
import scipy.signal as S

g = 9.81
pi = 3.14

m = 0.0502
Ix = 0.0545
Iy = 0.0545
Iz = 0.109

#Initial Conditions
#Altitude
z0 = 0.0
zdot0 = 0.0
#Roll
phi0 = 10.0*(pi/180.0)
phidot0 = 0.0
#Pitch
theta0 = -3.0*(pi/180.0)
thetadot0 = 0.0
#Yaw
psi0 = 45.0*(pi/180.0)
psidot0 = 0.0

#Command Signals
#Altitude
zc = 10.0
zdotc = 0.0
zddotc = 0.0
#Roll
phic = 0.0
phidotc = 0.0
phiddotc = 0.0
#Pitch
thetac = 0.0
thetadotc = 0.0
thetaddotc = 0.0
#Yaw
psic = 0.0
psidotc = 0.0
psiddotc = 0.0

def Derivatives(state,t):
    z = state[0]
    phi = state[1]
    theta = state[2]
    psi = state[3]
    zdot = state[4]
    phidot = state[5]
    thetadot = state[6]
    psidot = state[7]
    #state = [[z],[phi],[theta],[psi],[zdot],[phidot],[thetadot],[psidot]]
    M = np.asarray([[m,0,0,0],[0,Ix,0,0],[0,0,Iy,0],[0,0,0,Iz]])
    #print(M)
    H = np.asarray([[-1,-1,-1,-1],[-1,1,1,-1],[1,1,-1,-1],[-1,1,-1,1]])
    #print(H)
    f = np.asarray([m*g,0,0,0])
    #print(f)
    kp = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    #print(kp)
    kd = np.asarray([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    #print(kd)
    qdot = np.asarray([zdot,phidot,thetadot,psidot])
    #print(qdot)
    q = np.asarray([z,phi,theta,psi])
    #print(q)
    qddotc = np.asarray([zddotc,phiddotc,thetaddotc,psiddotc])
    #print(qddotc)
    qdotc = np.asarray([zdotc,phidotc,thetadotc,psidotc])
    #print(qdotc)
    qc = np.asarray([zc,phic,thetac,psic])
    #print(qc)
    gamma = qddotc - np.matmul(kp,(q-qc)) - np.matmul(kd,(qdot-qdotc))
    #print('gamma=',gamma)
    Minv = np.linalg.inv(M)
    #print('Minv=',Minv)
    invMH = np.matmul(Minv,H)
    #print(invMH)
    GAUSSMATRIX = np.linalg.inv(invMH)
    #print(GAUSSMATRIX)
    chi = np.matmul(GAUSSMATRIX,(gamma - f))
    #print('chi=',chi)
    qddot = np.matmul(invMH,chi) + f
    #print('qddot=',qddot)
    statedot = np.hstack(([zdot,phidot,thetadot,psidot],qddot))
    #print('statedot = ',statedot)
    return statedot

tout = np.linspace(0,100,10000)
stateinit = np.asarray([z0,phi0,theta0,psi0,zdot0,phidot0,thetadot0,psidot0])
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
plt.plot(tout,stateout[:,2],label='Theta')
plt.plot(tout,stateout[:,6],label='Thetadot')
plt.xlabel('Time')
plt.ylabel('Pitch')
plt.legend()
plt.grid()

plt.figure()
plt.plot(tout,stateout[:,3],label='Psi')
plt.plot(tout,stateout[:,7],label='Psidot')
plt.xlabel('Time')
plt.ylabel('Yaw')
plt.legend()
plt.grid()
plt.show()