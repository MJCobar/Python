#This is a test for the USB Storage Device
import sys
import os
import time
import random
import numpy as np
from datalogger import *

os.system("sudo mount /dev/sdb1 /media/mntpt")
print("Mounted!")
location = sys.argv[1]
filename = "/media/mntpt/USB_Test/" + location

logger = Datalogger()
print("Looking for File in " + filename);
logger.findfile(filename);
logger.open();
outdata = np.zeros(10)

while True:
    for i in range(0,10):
        n = random.randint(1,100)
        outdata[i] = n
    print(outdata)
    logger.println(outdata)
    time.sleep(1)

os.system("sudo umount /dev/sdc1")
print("Unmounted!")
