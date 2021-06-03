import numpy as np
import Orbit as O
#import wmm2020
import igrf

example_inputs = np.loadtxt('ABEX_Data_File.txt')

FS = example_inputs[0] #factor of safety
print(FS)

Ixx = example_inputs[1] #kg-m^2
Iyy = example_inputs[2]
Izz = example_inputs[3]

wmax = example_inputs[4] #deg/s - Not sure where this comes from

length = example_inputs[5]/100.0 #meters
width = example_inputs[6]/100.0
height = example_inputs[7]/100.0

Mission_Duration = example_inputs[8] #months

CD = example_inputs[9] #Drag

print(Ixx)
print(Iyy)
print(Izz)
print(wmax)
print(length)
print(width)
print(height)
print(Mission_Duration)
print(CD)

rp = 400.0
ra = 160000.0
orbit = O.Earth_Orbit(ra,rp)
orbit.Numerical_Orbit(1000)
orbit.make_plots()

mag = igrf.igrf('2010-07-12', glat=65, glon=-148, alt_km=100)