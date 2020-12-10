#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from matplotlib.backends.backend_pdf import PdfPages

data1 = np.loadtxt('Meta_1_Double_Irvington_8_30_2019_1.txt')
data2 = np.loadtxt('Meta_2_Double_Irvington_8_30_2019_2.txt')

#Fixes time to seconds
time1 = data1[:,0]
time1 -= time1[0]
time1 /= 1000000.0

time2 = data2[:,0]
time2 -= time2[0]
time2 /= 1000000.0

#Fixes GPS speed unit error
GPS_Speed1 = data1[:,20]
#GPS_Speed1 *= 1000000.0

GPS_Speed2 = data2[:,20]
#GPS_Speed2 *= 1000000.0

#Convert Roll and Pitch commands from microseconds to degrees
rollrc1 = data1[:,7]
pitchrc1 = data1[:,8]
yawrc1 = data1[:,9]
roll_command1 = (45.0/515.0)*(rollrc1-1500.0)
pitch_command1 = -(45.0/515.0)*(pitchrc1-1500.0)
yaw_command1 = (45.0/515.0)*(yawrc1-1500.0)

rollrc2 = data2[:,7]
pitchrc2 = data2[:,8]
yawrc2 = data2[:,9]
roll_command2 = (45.0/515.0)*(rollrc2-1500.0)
pitch_command2 = -(45.0/515.0)*(pitchrc2-1500.0)
yaw_command2 = (45.0/515.0)*(yawrc2-1500.0)

###Corrects Lat and Long data so no zero values###
Long1 = data1[:,17]
Lat1 = data1[:,18]
altitude1 = data1[:,19]

altitude_trim1 = []
Lat_trim1 = []
Long_trim1 = []
time_trim1 = []

for x in range (0,len(Lat1)):
  if Lat1[x] != -99:
    if Long1[x] != -99:
      if altitude1[x] != -99:
        Lat_trim1.append(Lat1[x])
        Long_trim1.append(Long1[x])
        altitude_trim1.append(altitude1[x])
        time_trim1.append(time1[x])
        
Long2 = data2[:,17]
Lat2 = data2[:,18]
altitude2 = data2[:,19]

altitude_trim2 = []
Lat_trim2 = []
Long_trim2 = []
time_trim2 = []

for x in range (0,len(Lat2)):
  if Lat2[x] != -99:
    if Long2[x] != -99:
      if altitude2[x] != -99:
        Lat_trim2.append(Lat2[x])
        Long_trim2.append(Long2[x])
        altitude_trim2.append(altitude2[x])
        time_trim2.append(time2[x])

###Shows rows and columns of data###
print(np.shape(data1))
print(np.shape(Lat_trim1))
print(np.shape(Long_trim1))

print(np.shape(data2))
print(np.shape(Lat_trim2))
print(np.shape(Long_trim2))

print('Generating Plots')

###Begins plotting data and saves all plots to single pdf###
pdfhandle = PdfPages('Meta_Double_Flight_Plots.pdf')

plt.figure()
plt.plot(time1,data1[:,1],label = 'Meta_1_IMU')
plt.plot(time1,roll_command1,label = 'Meta_1_Transmitter')
plt.plot(time2,data2[:,1],label = 'Meta_2_IMU')
plt.plot(time2,roll_command2,label = 'Meta_2_Transmitter')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Roll Angle (deg)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,2],label = 'Meta_1_IMU')
plt.plot(time1,pitch_command1,label = 'Meta_1_Transmitter')
plt.plot(time2,data2[:,2],label = 'Meta_2_IMU')
plt.plot(time2,pitch_command2,label = 'Meta_2_Transmitter')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Pitch Angle (deg)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,3],label = 'Meta_1_IMU')
plt.plot(time1,yaw_command1,label = 'Meta_1_Transmitter')
plt.plot(time2,data2[:,3],label = 'Meta_2_IMU')
plt.plot(time2,yaw_command2,label = 'Meta_2_Transmitter')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Yaw Angle (deg)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,4],label = 'Meta_1')
plt.plot(time2,data2[:,4],label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Roll Rate, P (deg/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,5],label = 'Meta_1')
plt.plot(time2,data2[:,5],label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Pitch Rate, Q (deg/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,6],label = 'Meta_1')
plt.plot(time2,data2[:,6],label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Yaw Rate, R (deg/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,10],label = 'Meta_1')
plt.plot(time2,data2[:,10],label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Throttle Command (usec)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,11],label = 'Meta_1_Autopilot')
plt.plot(time1,data1[:,12],label = 'Meta_1_Panic')
plt.plot(time2,data2[:,11],label = 'Meta_2_Autopilot')
plt.plot(time2,data2[:,12],label = 'Meta_2_Panic')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Switch Command (usec)')
pdfhandle.savefig()

ylabels = ['Motor (usec)','Aileron (usec)','Elevator (usec)','Rudder (usec)']
for x in range (13,17):
  plt.figure()
  plt.plot(time1,data1[:,x],label = 'Meta_1')
  plt.plot(time2,data2[:,x],label = 'Meta_2')
  plt.grid()
  plt.xlabel('Time (sec)')
  plt.ylabel(ylabels[x-17])
  pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,21],label = 'Meta_1_Pitot1:Raw_Windspeed')
plt.plot(time1,data1[:,23],label = 'Meta_1_Pitot1:Filtered_Windspeed')
plt.plot(time2,data2[:,21],label = 'Meta_2_Pitot1:Raw_Windspeed')
plt.plot(time2,data2[:,23],label = 'Meta_2_Pitot1:Filtered_Windspeed')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Wind Speed (m/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,data1[:,22],label = 'Meta_1_Pitot2:Raw_Windspeed')
plt.plot(time1,data1[:,24],label = 'Meta_1_Pitot2:Filtered_Windspeed')
plt.plot(time2,data2[:,22],label = 'Meta_2_Pitot2:Raw_Windspeed')
plt.plot(time2,data2[:,24],label = 'Meta_2_Pitot2:Filtered_Windspeed')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Wind Speed (m/s)')
pdfhandle.savefig()

plt.figure()
plt.plot(time1,GPS_Speed1,label = 'Meta_1')
plt.plot(time2,GPS_Speed2,label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('GPS Speed (m/s)')
pdfhandle.savefig()

fig1 = plt.figure()
plt1 = fig1.add_subplot(1,1,1)
plt1.plot(time_trim1,Long_trim1,label = 'Meta_1')
plt2 = fig1.add_subplot(1,1,1)
plt2.plot(time_trim2,Long_trim2,label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Longitude (deg)')
plt1.get_yaxis().get_major_formatter().set_useOffset(False)
plt2.get_yaxis().get_major_formatter().set_useOffset(False)
plt.gcf().subplots_adjust(left = 0.18)
pdfhandle.savefig()

fig1 = plt.figure()
plt1 = fig1.add_subplot(1,1,1)
plt1.plot(time_trim1,Lat_trim1,label = 'Meta_1')
plt2 = fig1.add_subplot(1,1,1)
plt2.plot(time_trim2,Lat_trim2,label = 'Meta_2')
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Latitude (deg)')
plt1.get_yaxis().get_major_formatter().set_useOffset(False)
plt2.get_yaxis().get_major_formatter().set_useOffset(False)
plt.gcf().subplots_adjust(left = 0.18)
pdfhandle.savefig()

fig1 = plt.figure()
plt1 = fig1.add_subplot(1,1,1)
plt1.plot(Long_trim1,Lat_trim1)
plt1.plot(Long_trim1[0],Lat_trim1[0],'gs',label = 'Meta_1_Start_Point')
plt1.plot(Long_trim1[1993],Lat_trim1[1993],'b^',label = 'Meta_1_End_Point') #Need to adjust numbers according to print(np.shape(Long_trim)) and print(np.shape(Lat_trim))
plt2 = fig1.add_subplot(1,1,1)
plt2.plot(Long_trim2,Lat_trim2)
plt2.plot(Long_trim2[0],Lat_trim2[0],'ks',label = 'Meta_2_Start_Point')
plt2.plot(Long_trim2[2091],Lat_trim2[2091],'r^',label = 'Meta_2_End_Point') #Need to adjust numbers according to print(np.shape(Long_trim)) and print(np.shape(Lat_trim))
plt.legend()
plt.grid()
plt.xlabel('Longitude (deg)')
plt.ylabel('Latitude (deg)')
plt1.get_yaxis().get_major_formatter().set_useOffset(False)
plt1.get_xaxis().get_major_formatter().set_useOffset(False)
plt2.get_yaxis().get_major_formatter().set_useOffset(False)
plt2.get_xaxis().get_major_formatter().set_useOffset(False)
plt.gcf().subplots_adjust(left = 0.18)
pdfhandle.savefig()

plt.figure()
plt.plot(time_trim1,altitude_trim1,label = "Meta_1_GPS")
plt.plot(time1,data1[:,25],label = "Meta_1_Barometer")
plt.plot(time_trim2,altitude_trim2,label = "Meta_2_GPS")
plt.plot(time2,data2[:,25],label = "Meta_2_Barometer")
plt.legend()
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Altitude (m)')
pdfhandle.savefig()

pdfhandle.close()

print('Plotting Routine Complete for Python')
#os.system('evince python_plots.pdf &')
#plt.show
