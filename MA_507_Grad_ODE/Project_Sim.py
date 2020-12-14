import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,1000)
J = 1
mgl = 1
theta0 = 0
thetadot0 = 0
theta_desired = 1

###Proportional Controller
kp1 = 8
kp2 = 12
kp3 = 16
kp4 = 20
kp5 = 24

data1 = []
for x in time:
    theta1 = ((1/kp1)-1)*(np.cos(np.sqrt(kp1)*x)) + 1 - (1/kp1)
    data1.append(theta1)
data_kp1 = np.asarray(data1)

data2 = []
for x in time:
    theta2 = ((1/kp2)-1)*(np.cos(np.sqrt(kp2)*x)) + 1 - (1/kp2)
    data2.append(theta2)
data_kp2 = np.asarray(data2)

data3 = []
for x in time:
    theta3 = ((1/kp3)-1)*(np.cos(np.sqrt(kp3)*x)) + 1 - (1/kp3)
    data3.append(theta3)
data_kp3 = np.asarray(data3)

data4 = []
for x in time:
    theta4 = ((1/kp4)-1)*(np.cos(np.sqrt(kp4)*x)) + 1 - (1/kp4)
    data4.append(theta4)
data_kp4 = np.asarray(data4)

data5 = []
for x in time:
    theta5 = ((1/kp5)-1)*(np.cos(np.sqrt(kp5)*x)) + 1 - (1/kp5)
    data5.append(theta5)
data_kp5 = np.asarray(data5)

plt.figure()
plt.plot(time,data_kp1,label='kp=8')
plt.plot(time,data_kp2,label='kp=12')
plt.plot(time,data_kp3,label='kp=16')
plt.plot(time,data_kp4,label='kp=20')
plt.plot(time,data_kp5,label='kp=24')
plt.grid()
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Theta (deg)')

###Proportional & Derivative Controller
kp = kp5
kd1 = 3
kd2 = 4
kd3 = 5
kd4 = 6
kd5 = 7
kd6 = 8

data6 = []
for x in time:
    theta6 = np.exp(-(kd1/2)*x)*(((1/kp) - 1)*np.cos((np.sqrt(4*kp - kd1**2)/2)*x) + ((kd1*(1-kp))/(kp*(np.sqrt(4*kp - kd1**2))))*np.sin((np.sqrt(4*kp - kd1**2)/2)*x)) + 1 - (1/kp)
    data6.append(theta6)
data_kd1 = np.asarray(data6)

data7 = []
for x in time:
    theta7 = np.exp(-(kd2/2)*x)*(((1/kp) - 1)*np.cos((np.sqrt(4*kp - kd2**2)/2)*x) + ((kd2*(1-kp))/(kp*(np.sqrt(4*kp - kd2**2))))*np.sin((np.sqrt(4*kp - kd2**2)/2)*x))+ 1 - (1/kp)
    data7.append(theta7)
data_kd2 = np.asarray(data7)

data8 = []
for x in time:
    theta8 = np.exp(-(kd3/2)*x)*(((1/kp) - 1)*np.cos((np.sqrt(4*kp - kd3**2)/2)*x) + ((kd3*(1-kp))/(kp*(np.sqrt(4*kp - kd3**2))))*np.sin((np.sqrt(4*kp - kd3**2)/2)*x))+ 1 - (1/kp)
    data8.append(theta8)
data_kd3 = np.asarray(data8)

data9 = []
for x in time:
    theta9 = np.exp(-(kd4/2)*x)*(((1/kp) - 1)*np.cos((np.sqrt(4*kp - kd4**2)/2)*x) + ((kd4*(1-kp))/(kp*(np.sqrt(4*kp - kd4**2))))*np.sin((np.sqrt(4*kp - kd4**2)/2)*x))+ 1 - (1/kp)
    data9.append(theta9)
data_kd4 = np.asarray(data9)

data10 = []
for x in time:
    theta10 = np.exp(-(kd5/2)*x)*(((1/kp) - 1)*np.cos((np.sqrt(4*kp - kd5**2)/2)*x) + ((kd5*(1-kp))/(kp*(np.sqrt(4*kp - kd5**2))))*np.sin((np.sqrt(4*kp - kd5**2)/2)*x))+ 1 - (1/kp)
    data10.append(theta10)
data_kd5 = np.asarray(data10)

data11 = []
for x in time:
    theta11 = np.exp(-(kd6/2)*x)*(((1/kp) - 1)*np.cos((np.sqrt(4*kp - kd6**2)/2)*x) + ((kd6*(1-kp))/(kp*(np.sqrt(4*kp - kd6**2))))*np.sin((np.sqrt(4*kp - kd6**2)/2)*x))+ 1 - (1/kp)
    data11.append(theta11)
data_kd6 = np.asarray(data11)

plt.figure()
plt.plot(time,data_kd1,label='kd=3,kp=24')
plt.plot(time,data_kd2,label='kd=4,kp=24')
plt.plot(time,data_kd3,label='kd=5,kp=24')
plt.plot(time,data_kd4,label='kd=6,kp=24')
plt.plot(time,data_kd5,label='kd=7,kp=24')
plt.plot(time,data_kd6,label='kd=8,kp=24')
plt.grid()
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Theta (deg)')

###Full PID Controller
kd = kd6
ki1 = 24
ki2 = 27
ki3 = 32
ki4 = 45
ki5 = 72
ki6 = 119

data12 = []
for x in time:
    theta12 = 1 + 4*np.exp(-2*x) + np.exp(-3*x)*(np.sin(np.sqrt(3)*x) - 5*np.cos(np.sqrt(3)*x))
    data12.append(theta12)
data_ki1 = np.asarray(data12)

data13 = []
for x in time:
    theta13 = 1 + 2*np.exp(-3*x) + np.exp(-(5/2)*x)*(np.sin((np.sqrt(11)/2)*x) - 3*np.cos((np.sqrt(11)/2)*x))
    data13.append(theta13)
data_ki2 = np.asarray(data13)

data14 = []
for x in time:
    theta14 = 1 + 2*np.exp(-4*x) + np.exp(-2*x)*(np.sin(2*x) - 3*np.cos(2*x))
    data14.append(theta14)
data_ki3 = np.asarray(data14)

data15 = []
for x in time:
    theta15 = 1 - 1*np.exp(-5*x) + np.exp(-(3/2)*x)*(np.sin(((3*np.sqrt(3))/2)*x) - 3*np.cos((3*np.sqrt(3))/2)*x)
    data15.append(theta15)
data_ki4 = np.asarray(data15)

data16 = []
for x in time:
    theta16 = 1 + 2*np.exp(-6*x) + np.exp(-1*x)*(np.sin(np.sqrt(11)*x) - 3*np.cos(np.sqrt(11)*x))
    data16.append(theta16)
data_ki5 = np.asarray(data16)

data17 = []
for x in time:
    theta17 = 1 + 2*np.exp(-7*x) + np.exp(-(1/2)*x)*(np.sin((np.sqrt(67)/2)*x) - 3*np.cos((np.sqrt(67)/2)*x))
    data17.append(theta17)
data_ki6 = np.asarray(data17)

plt.figure()
plt.plot(time,data_ki1,label='ki=24,kd=8,kp=24')
plt.plot(time,data_ki2,label='ki=27,kd=8,kp=24')
plt.plot(time,data_ki3,label='ki=32,kd=8,kp=24')
plt.plot(time,data_ki4,label='ki=45,kd=8,kp=24')
plt.plot(time,data_ki5,label='ki=72,kd=8,kp=24')
plt.plot(time,data_ki6,label='ki=119,kd=8,kp=24')
plt.grid()
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Theta (deg)')

plt.show()