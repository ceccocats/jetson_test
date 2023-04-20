#!/usr/bin/python
import sys
import time
import Jetson.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

channels = [7, 35]

for channel in channels:
    GPIO.cleanup(channel)
    GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)

for n in range(5):
    print("set LOW to: ", channels)
    for channel in channels:
        GPIO.output(channel, GPIO.LOW)
    time.sleep(1.0)
    print("set HIGH to: ", channels)
    for channel in channels:
        GPIO.output(channel, GPIO.HIGH)
    time.sleep(1.0)

