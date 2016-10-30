import cv2
import numpy as np

def convertColorSchema():

    cap = cv2.VideoCapture(2)

    while (1):

        # Take each frame
        _, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([14, 86, 75])
        upper_blue = np.array([160, 215, 139])

        lowerG = np.array([36, 84, 129])
        upperG = np.array([61, 164, 196])
        #Green 25 , 75, 121
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask2= cv2.inRange(hsv, lowerG, upperG)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res2 = cv2.bitwise_or(frame, frame, mask=mask2)
        restot = res | res2
        cv2.imshow('frame', frame)
        # cv2.imshow('mask', mask)
        cv2.imshow('res', restot)
        # cv2.imshow('clr', hsv)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

convertColorSchema()
