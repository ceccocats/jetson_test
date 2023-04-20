#!/usr/bin/python
import cv2
import sys
import time
import Jetson.GPIO as GPIO
import os.path
import os
import numpy as np
GPIO.setmode(GPIO.BOARD)

def checkFile(f):
    for i in range(5):
        if os.path.exists(f):
            return True
        time.sleep(2.0)
    return False

os.system("rmmod uvcvideo")
os.system("modprobe uvcvideo quirks=128")

print("reset hub")
channel = [7]
GPIO.cleanup(channel)
GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(channel, GPIO.LOW)
time.sleep(5.0)
GPIO.output(channel, GPIO.HIGH)

time.sleep(10.0)

result = [ False for i in range(4) ]
for i in range(4):
    camfile = f"/dev/video{i}"
    print("test camera: ", camfile)
    if not checkFile(camfile):
        print("unable to open camera!!")
        continue

    print("try read")
    vid = cv2.VideoCapture(i, cv2.CAP_V4L2)

    readed = 0
    for j in range(10):
        ret, frame = vid.read()
        if(ret):
            readed += 1

    if(readed == 10):
        print("--> OK")
        result[i] = True
    else:
        print("--> FAIL")

print("\nResult:")
for i in range(4):
    print(f"cam{i}: {result[i]}")


print("\ntest all together")
vids = []
result = True
for i in range(4):
    vid = cv2.VideoCapture(i, cv2.CAP_V4L2)
    vids.append(vid)
for n in range(10):
    for i in range(4):
        ret, frame = vids[i].read()
        if(ret is False):
            result = False
print("Result: ", result)
