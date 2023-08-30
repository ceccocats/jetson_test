#!/usr/bin/python
import cv2
import sys
import time
import Jetson.GPIO as GPIO
import os.path
import os
import numpy as np

camID = sys.argv[1]
vid = cv2.VideoCapture(camID, cv2.CAP_V4L2)
while True:
    ret, frame = vid.read()
    print("cam: ", camID, np.shape(frame))

