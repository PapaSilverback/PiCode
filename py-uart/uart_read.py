import time
import serial


def setup():
    ser = serial.Serial(

        port='dev/ttyAMA0',#This will have to be changed to whatever I need to get it to be
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

def read():
counter = 0
while 1:
    x=ser.readline()
    print x