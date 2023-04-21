from ADS7828 import *
from INA219 import *
import os, time

# init ads7828
adc = Ads7828()

# init INA219
ina219_reading_mA = 1000
ext_meter_reading_mA = 1000
ina1 = INA219(8, INA219.INA219_I2C_ADDRESS1) 
ina2 = INA219(8, INA219.INA219_I2C_ADDRESS2)

#begin return True if succeed, otherwise return False
while not ina1.begin():
    time.sleep(2)
ina1.linear_cal(ina219_reading_mA, ext_meter_reading_mA)
while not ina2.begin():
    time.sleep(2)
ina2.linear_cal(ina219_reading_mA, ext_meter_reading_mA)

while True:

    #v0 = adc.read_raw_adc(0)
    #print(f"ADS7828 V1 voltage: {v0}")
    
    ina1_v = ina1.get_bus_voltage_V()
    ina1_a = ina1.get_current_mA()
    print(f"INA219 A1 voltage: {ina1_v} V current: {ina1_a} mA")

    ina2_v = ina2.get_bus_voltage_V()
    ina2_a = ina2.get_current_mA()
    print(f"INA219 A2 voltage: {ina2_v} V current: {ina2_a} mA")

    time.sleep(0.2)
