
import time
import serial
def write():
    ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)
    counter = 0

    while 1:
        ser.write('Write counter: %d \n'%(counter))
        time.sleep(1)
        counter += 1