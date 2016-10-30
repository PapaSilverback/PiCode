import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (500, 500)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (500, 500))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
    image = frame.array
    flip = cv2.flip(image, 0)
    cv2.imshow("Frame", flip)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
    	break
