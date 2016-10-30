#imports for camera conversion
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class PiCamera_Converter():

    def __init__(self):
        super(PiCamera_Converter, self).__init__()

    @staticmethod
    def take_Picture():
        #initialize the camera
        camera = PiCamera()
        camera.resolution = (500, 500)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera)
        time.sleep(0.1)

        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        cv2.imshow("Image",image)
        cv2.waitKey(0)
    #This method will take the Raspberry Pi object and create a converted
    #version of it so it is compatible with OpenCV
    @staticmethod
    def createConvertedCameraObject():
         #initialize the camera
        camera = PiCamera()
        camera.resolution = (500, 500)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera)
        time.sleep(0.1)
        return (camera, rawCapture)
