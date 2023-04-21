# -*- coding: utf-8 -*-
import smbus
import time

DEVICE_ADDRESS = 0x48      #7 bit address (will be left shifted to add the read write bit)
I2C_CHANNEL = 8  #raspberry i2c channel

#ADC7828 CONTROL REGISTER
ADS7828_CONFIG_SD_DIFFERENTIAL      = 0x00
ADS7828_CONFIG_SD_SINGLE            = 0x80
ADS7828_CONFIG_CS_CH0               = 0x00
ADS7828_CONFIG_CS_CH1               = 0x40
ADS7828_CONFIG_CS_CH2               = 0x10
ADS7828_CONFIG_CS_CH3               = 0x50
ADS7828_CONFIG_CS_CH4               = 0x20
ADS7828_CONFIG_CS_CH5               = 0x60
ADS7828_CONFIG_CS_CH6               = 0x30
ADS7828_CONFIG_CS_CH7               = 0x70
ADS7828_CONFIG_PD_OFF               = 0x00
ADS7828_CONFIG_PD_REFOFF_ADON       = 0x04
ADS7828_CONFIG_PD_REFON_ADOFF       = 0x08
ADS7828_CONFIG_PD_REFON_ADON        = 0x0c

#ADS 7828 I2C CONTROL CLASS
class Ads7828:
    def __init__(self, address=DEVICE_ADDRESS, bus_id=I2C_CHANNEL, debug=False):
        self.i2c = smbus.SMBus(bus_id)
        self.address = address
        self.debug = debug
    def read_raw_adc(self, ch):
        config = 0
        config |= ADS7828_CONFIG_SD_SINGLE
        config |= ADS7828_CONFIG_PD_REFOFF_ADON
        if ch == 0:
            config |= ADS7828_CONFIG_CS_CH0
        elif ch == 1:
            config |= ADS7828_CONFIG_CS_CH1
        elif ch == 2:
            config |= ADS7828_CONFIG_CS_CH2
        elif ch == 3:
            config |= ADS7828_CONFIG_CS_CH3
        elif ch == 4:
            config |= ADS7828_CONFIG_CS_CH4
        elif ch == 5:
            config |= ADS7828_CONFIG_CS_CH5
        elif ch == 6:
            config |= ADS7828_CONFIG_CS_CH6
        elif ch == 7:
            config |= ADS7828_CONFIG_CS_CH7
 
        time.sleep(0.01)#adc convertion time waiting
        data =[0,0]
        data = self.i2c.read_i2c_block_data(self.address,config,2)
        time.sleep(0.01)
        return ((data[0] << 8) + data[1])

    def all_ch_raw_adc_display(self):
        data= [0]*8
        for i in range (8) :
           data[i] = adc.read_raw_adc(i)
        print ("ch0=%d, ch1=%d, ch2=%d, ch3=%d, ch4=%d, ch5=%d, ch6=%d, ch7=%d"  %(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
 
if __name__ =="__main__":
    adc = Ads7828()
    while True:
        adc.all_ch_raw_adc_display()


