import serial
import struct
import time
ser = serial.Serial('/dev/ttyTHS0', 38400, timeout=1)

res = False
for i in range(30):
    try:
        line = ser.readline()
        #print(line)
        if "$GNGGA" in line.decode("utf-8"):
            res = True
    except:
        pass
ser.close()

print("Result: ", res)
