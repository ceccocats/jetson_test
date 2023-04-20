import serial
import struct
import time
import numpy as np

def imageCmd(img, bvol, bon, boff):
    payloadSize = 8*8*3 + 5
    header = struct.pack('=BBH', 0x24, 1, payloadSize)
    img_buffer = bytearray(img)
    beep_buffer = struct.pack('=BHHB', bvol, bon, boff, 0x42)
    return header + img_buffer + beep_buffer

def shutdownCmd(time):
    return struct.pack('=BBHHB', 0x24, 2, 2, time, 0x42)



ser = serial.Serial('/dev/ttyTHS0', 115200, timeout=1)
ser.write(shutdownCmd(50))

img = np.zeros([8,8,3],dtype=np.uint8)

print("test glitch")
for n in range(2):
    for i in range(8):
        img.fill(0)
        for j in range(8):
            for k in range(3):
                img[i,j,k] = 255
                cmd = imageCmd(img, 20, 0, 1)
                ser.write(cmd)
                #print(bytes(cmd).hex())
                time.sleep(0.1)
img.fill(0)
print("test beep")
for i in range(10):
    print("vol: ", (i+1)*10)
    cmd = imageCmd(img, (i+1)*10, 1, 1)
    ser.write(cmd)
    time.sleep(2.0)

print("shutdown in 1 sec")
ser.write(shutdownCmd(10))
time.sleep(3.0)

print("sometime this fail to set after shutdown")
ser.write(shutdownCmd(100))
img.fill(255)
cmd = imageCmd(img, 30, 1, 1)
ser.write(cmd)
time.sleep(4.0)

print("resending twice after shutdown helps")
ser.write(shutdownCmd(100))
img.fill(255)
cmd = imageCmd(img, 30, 1, 1)
ser.write(cmd)
time.sleep(0.1)
ser.write(cmd)
time.sleep(4.0)


ser.close()

#hexstring ="24010E00000000FF0000010101320A00140042"
#cmd = bytearray.fromhex(hexstring)
#print(bytes(cmd).hex())
#ser.write(cmd)
