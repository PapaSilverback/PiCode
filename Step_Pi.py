import RPi.GPIO as GPIO
import time
import spidev
from threading import Thread
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7800000  # 7.8MHz clock
spi.mode = 0b01

sclock = 29
nxt = 7
direction = 11
mosi = 19


GPIO.setmode(GPIO.BCM)
GPIO.setup(nxt, GPIO.OUT)  # NXT pin used to step the motor
GPIO.setup(direction, GPIO.OUT)  # DIR pin used to specify direction
GPIO.setup(mosi, GPIO.OUT)  # Connect to DI(MOSI) on stepper control board
GPIO.setup(21, GPIO.IN)  # Connect to DO(MISO) on stepper control board
GPIO.setup(sclock, GPIO.OUT)  # Clock signal out
GPIO.setup(22, GPIO.OUT)  # CS (chip select) only one slave needed
GPIO.setup(23, GPIO.OUT)

GPIO.output(7, GPIO.LOW)  # NXT pin set
GPIO.output(11, GPIO.LOW)  # direction pin set
GPIO.output(mosi, GPIO.LOW)  # DI(MOSI)
GPIO.output(22, GPIO.HIGH)  # CS pin offset HIGH
GPIO.output(23, GPIO.LOW)


# Tell the board what current to set
def setup():
    bitsToSend = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
    for i in range(0, len(bitsToSend)):
        if bitsToSend[i]:
            GPIO.output(mosi, GPIO.HIGH)
        else:
            GPIO.output(mosi, GPIO.LOW)
        GPIO.output(sclock, GPIO.HIGH)
        time.sleep(.0001) #sleep 100us
        GPIO.output(sclock, GPIO.LOW)
        time.sleep(.0001)

#OLD stuff translated from ARDUINO:
    #cr0 = 0b00000000
    #cr2 = 0b00000000
    ## Set the current
    #cr0 = (cr0 & 0b11100000) | mamps
    #writeReg(0x1, cr0)
    ## Set the steps
    #step = 0b000  # for 1/32 of a step, not generic, ToDo
    #cr0 = (cr0 & ~0b11100000) | (step << 5)
    #writeReg(0x1, cr0)
    ## enable driver
    #cr2 |= 0b10000000
    #writeReg(0x3, cr2)


def writeReg(addr, value):
    selectChip()
    spi.xfer([0x80 | addr & 0b11111, value])
    deselectChip()


def selectChip():
    GPIO.output(22, GPIO.LOW)
    #spi.xfer([spi.max_speed_hz, 3000, 8])


def deselectChip():
    GPIO.output(22, GPIO.HIGH)
    #High time for this chip is 2.5ms.  Wait to complete
    time.sleep(.003)


# spi with 8 bit transfer packet
def transfer(data):
    spi.xfer(spi.max_speed_hz, 3000, data)


def setDir(dir):
    time.sleep(.001)
    GPIO.output(direction, dir)
    time.sleep(.001)


#  Pulse a signal to the "NXT"" pin on the driver (spin motor one tick)
def step():
    GPIO.output(nxt, GPIO.HIGH)
    time.sleep(.003)
    GPIO.output(nxt, GPIO.LOW)
    time.sleep(.003)

    # Control the motor's speed: higher delay time means higher motor speed
    # time.sleep(1000)


def clockRun():
    GPIO.output(sclock, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(sclock, GPIO.LOW)
    time.sleep(0.0001)
# thread = Thread(target = clockRun, args = ())
# thread.start()

setup()  # Desired 2700 mA is defined as 10111 from driver datasheet
setDir(0)

x = 0
while (x < 1000):
    step()
    x += 1
time.sleep(.003)
setDir(1)
x = 0
while (x < 1000):
    step()
    x += 1
time.sleep(.003)
GPIO.cleanup()