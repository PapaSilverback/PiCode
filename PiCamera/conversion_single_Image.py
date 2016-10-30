#imports for camera conversion
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import PiCamera_Converter
import picam

#initialize the camera


#PiCamera_Converter.PiCamera_Converter.take_Picture()

#(camera, rawCapture) = PiCamera_Converter.PiCamera_Converter.createConvertedCameraObject()

#camera.capture(rawCapture, format="bgr")
#image = rawCapture.array
#cv2.imshow("Image",image)
#cv2.waitKey(0)

cv2.imshow("image", picam.OpenCVCapture().read())
cv2.waitKey(0)