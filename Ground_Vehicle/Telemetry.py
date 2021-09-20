#This is code for using LV-MaxSonar-EZ UltraSonic Range Sensor
import serial
import time
#import board
#import busio
import adafruit_us100

uart = serial.Serial("/dev/ttyUSB0",baudrate=9600,timeout=1)

us100 = adafruit_us100.US100(uart)

while True:
    print("Temperature: ", us100.temperature)
    print("Distance: ", us100.distance)
