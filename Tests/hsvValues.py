import cv2
import numpy as np
import time as t
from picamera.array import PiRGBArray
from picamera import PiCamera




cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)
cv2.createTrackbar('h_high', 'result',0,179,nothing)
cv2.createTrackbar('s_high', 'result',0,255,nothing)
cv2.createTrackbar('v_high', 'result',0,255,nothing)




camera = PiCamera()
camera.resolution= (500, 500)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(500,500))

t.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array


    #converting to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')
    h_high = cv2.getTrackbarPos('h_high','result')
    s_high = cv2.getTrackbarPos('s_high','result')
    v_high = cv2.getTrackbarPos('v_high','result')

    # Normal masking algorithm
    lower_blue = np.array([h,s,v])
    upper_blue = np.array([h_high,s_high,v_high])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(image,image,mask = mask)

    cv2.imshow('result',result)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
