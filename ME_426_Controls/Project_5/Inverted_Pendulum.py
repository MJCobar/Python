import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as S

plt.close("all")

g = 9.81
L = 1.0
m = 5.0
M = 10.0
K = 1000.0
alpha = 20.0
beta = 75.0
theta0 = 20*np.pi/180.
thetac = 0*np.pi/180.

def controller(x):
    thetacdot = 0.0
    theta = x[0]
    thetadot = x[1]
    xdot = x[2]
    xddot= x[3]
    eint = x[4]
    e = thetac - theta
    edot = thetacdot - thetadot
    #T = K(s^2 + b*s + c)/s
    #T = K*s + K*b + K*c/s
    #Compute Disturbance
    W = 0.0
    #W = 100.0
    #W = 10000.0
    T = K*alpha*e + K*edot + K*beta*eint + W
    return T,e

def DerivativesNL(x,t):
    theta = x[0]
    thetadot = x[1]
    xdot = x[2]
    xddot= x[3]
    eint = x[4]
    T,e = controller(x)
    thetaddot = (T-m*L*thetadot**2*np.sin(theta)+(M+m)*g*np.tan(theta))/((M+m)*L/np.cos(theta)-m*L*np.cos(theta))
    xddot = (L*thetaddot-g*np.sin(theta))/np.cos(theta)
    eintdot = e
    xdot1 = np.asarray([thetadot,thetaddot,xdot,xddot,eintdot])
    return xdot1
    
def Derivatives(x,t):
    theta = x[0]
    thetadot = x[1]
    xdot = x[2]
    xddot= x[3]
    eint = x[4]
    T,e = controller(x)
    xdot1 = np.matmul(A,x) + B1*T  + B2*e
    return xdot1
    
A = np.asarray([[0,1,0,0,0],
                [(M+m)*g/L*((M+m)-m),0,0,0,0],
                [0,0,0,1,0],
                [((M+m)*g/((M+m)-m))-g,0,0,0,0],
                [0,0,0,0,0]])
B1 = np.asarray([0,1/L*((M+m)-m),0,1/((M+m)-m),0])
B2 = np.asarray([0,0,0,0,1])
#eigs = np.linalg.eig(A)
#print(eigs)
xinitial = np.asarray([theta0,0,0,0,0])
tout = np.linspace(0,20,1000)
xout = S.odeint(Derivatives,xinitial,tout)
xoutNL = S.odeint(DerivativesNL,xinitial,tout)

plt.plot(tout,xout[:,0]*180/np.pi,label="Linear")
plt.plot(tout,xoutNL[:,0]*180./np.pi,'r-',label="Nonlinear")
plt.xlabel('Time (sec)')
plt.ylabel('Angle (deg)')
plt.legend()
plt.grid()

plt.show()