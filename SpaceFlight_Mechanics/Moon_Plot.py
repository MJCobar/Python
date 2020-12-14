#!/usr/bin/python

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
try:
    from pdf import *
    usepdf = 1
except:
    print('No module pdf')
    usepdf = 0

if usepdf:
    pp = PDF(1,plt)

e = 0.07
a = 387000 #km
p = a*(1-e**2) #km
enorm = np.linalg.norm(e)
omega = 150.0 #deg
OHM = 13.0 #deg
inc = 5.1 #deg

##Plot orbital plane
nu = np.linspace(0,2*np.pi,1000)
rorbit = p/(1+enorm*np.cos(nu))
rx = rorbit*np.cos(nu)
ry = rorbit*np.sin(nu)
plt.plot(rx,ry)
plt.plot(0,0,'y*')
plt.title('Orbital Plane')
plt.grid()
plt.axis('equal')
if usepdf:
    pp.savefig()

##Now let's rotate the entire orbit to the ecliptic plane
xecl = (np.cos(omega)*np.cos(OHM) - np.sin(omega)*np.sin(OHM)*np.cos(inc)) * rx + (-np.sin(omega)*np.cos(OHM)-np.cos(omega)*np.sin(OHM)*np.cos(inc))*ry
yecl = (np.cos(omega)*np.sin(OHM) + np.sin(omega)*np.cos(OHM)*np.cos(inc)) * rx + (-np.sin(omega)*np.sin(OHM)+np.cos(omega)*np.cos(OHM)*np.cos(inc))*ry
zecl = (np.sin(omega)*np.sin(inc))*rx + (np.cos(omega)*np.sin(inc))*ry

fig = plt.figure('Ecliptic')
#ax = fig.add_subplot(111,projection='3d')
ax = Axes3D(fig)
ax.plot(xecl,yecl,zecl, color = 'blue', linestyle = 'solid')
plt.title('Ecliptic')
plt.grid()
#plt.axis('equal')
ax.plot([0.],[0.],[0.],'y*',markersize=5)
#ax.plot([r[0]],[r[1]],[r[2]],'r*',markersize=5)
if usepdf:
    pp.savefig()

if usepdf:
    pp.close()
else:
    plt.show()