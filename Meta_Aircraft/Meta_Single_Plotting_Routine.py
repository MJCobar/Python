#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib.backends.backend_pdf import PdfPages

data = np.loadtxt('Meta_2_Double_Irvington_8_30_2019_2.txt')

#Fixes time to seconds
time = data[:,0]
time -= time[0]
time /= 1000000.0

#Fixes GPS speed unit error
GPS_Speed = data[:,20]
GPS_Speed *= 1000000.0

#Convert Roll and Pitch commands from microseconds to degrees
rollrc = data[:,7]
pitchrc = data[:,8]
yawrc = data[:,9]
roll_command = (45.0/515.0)*(rollrc-1500.0)
#print(roll_command)
pitch_command = -(45.0/515.0)*(pitchrc-1500.0)
#print(pitch_command)
yaw_command = (45.0/515.0)*(yawrc-1500.0)

###Corrects Lat and Long data so no zero values###
Long = data[:,17]
Lat = data[:,18]
altitude = data[:,19]

altitude_trim = []
Lat_trim = []
Long_trim = []
time_trim = []

for x in range (0,len(Lat)):
  if Lat[x] != -99:
    if Long[x] != -99:
      if altitude[x] != -99:
        Lat_trim.append(Lat[x])
        Long_trim.append(Long[x])
        altitude_trim.append(altitude[x])
        time_trim.append(time[x])

###Shows rows and columns of data###
print(np.shape(data))
print(np.shape(Lat_trim))
print(np.shape(Long_trim))
print('Generating Plots')

###Begins plotting data and saves all plots to single pdf###
pdfhandle = PdfPages('Meta2_Flight_Plots_2.pdf')

plt.figure()
plt.plot(time,data[:,1],label = 'IMU')
plt.plot(time,roll_command,label = 'Transmitter')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Roll Angle (deg)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,2],label = 'IMU')
plt.plot(time,pitch_command,label = 'Transmitter')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Pitch Angle (deg)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,3],label = 'IMU')
plt.plot(time,yaw_command,label = 'Transmitter')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Yaw Angle (deg)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,4])
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Roll Rate, P (deg/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,5])
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Pitch Rate, Q (deg/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,6])
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Yaw Rate, R (deg/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,10])
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Throttle Command (usec)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,11],label = 'Autopilot')
plt.plot(time,data[:,12],label = 'Panic')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Switch Command (usec)')
pdfhandle.savefig()

ylabels = ['Motor (usec)','Aileron (usec)','Elevator (usec)','Rudder (usec)']
for x in range (13,17):
  plt.figure()
  plt.plot(time,data[:,x])
  plt.grid()
  plt.xlabel('Time (sec)')
  plt.ylabel(ylabels[x-17])
  pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,21],label = 'Pitot1: Raw Windspeed')
plt.plot(time,data[:,23],label = 'Pitot1: Filtered Windspeed')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Wind Speed (m/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,data[:,22],label = 'Pitot2: Raw Windspeed')
plt.plot(time,data[:,24],label = 'Pitot2: Filtered Windspeed')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Wind Speed (m/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time,GPS_Speed)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('GPS Speed (m/s)')
pdfhandle.savefig()

fig1 = plt.figure()
plt1 = fig1.add_subplot(1,1,1)
plt1.plot(time_trim,Long_trim)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Longitude (deg)')
plt1.get_yaxis().get_major_formatter().set_useOffset(False)
plt.gcf().subplots_adjust(left = 0.18)
pdfhandle.savefig()

fig1 = plt.figure()
plt1 = fig1.add_subplot(1,1,1)
plt1.plot(time_trim,Lat_trim)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Latitude (deg)')
plt1.get_yaxis().get_major_formatter().set_useOffset(False)
plt.gcf().subplots_adjust(left = 0.18)
pdfhandle.savefig()

fig1 = plt.figure()
plt1 = fig1.add_subplot(1,1,1)
plt1.plot(Long_trim,Lat_trim)
plt1.plot(Long_trim[0],Lat_trim[0],'gs',label = 'Start Point')
plt1.plot(Long_trim[2091],Lat_trim[2091],'b^',label = 'End Point') #Need to adjust numbers according to print(np.shape(Long_trim)) and print(np.shape(Lat_trim))
plt.legend()
plt.grid()
plt.xlabel('Longitude (deg)')
plt.ylabel('Latitude (deg)')
plt1.get_yaxis().get_major_formatter().set_useOffset(False)
plt1.get_xaxis().get_major_formatter().set_useOffset(False)
plt.gcf().subplots_adjust(left = 0.18)
pdfhandle.savefig()

plt.figure()
plt.plot(time_trim,altitude_trim,label = "GPS")
plt.plot(time,data[:,25],label = "Barometer")
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Altitude (m)')
pdfhandle.savefig()

pdfhandle.close()

print('Plotting Routine Complete for Python')
#os.system('evince python_plots.pdf &')
#plt.show
