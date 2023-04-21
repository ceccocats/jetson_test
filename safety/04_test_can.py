import can
import os
import time

os.system("modprobe mttcan")
os.system("ifconfig can0 down")
os.system("ip link set can0 up type can bitrate 500000")
os.system("ifconfig can0 up")

bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

msg = can.Message(arbitration_id=0x01, data=[0, 25, 0, 1, 3, 1, 4, 1])

for i in range(10):
    try:
        bus.send(msg)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")
    time.sleep(0.5)

