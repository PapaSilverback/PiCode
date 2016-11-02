import time
import serial

ser = 0


def setup():
    ser = serial.Serial('/dev/ttyAMA0',baudrate=9600, timeout=1)
    print("I have just set up the uart.")


def read():
    while 1:
        x = ser.readline()
        print (x)