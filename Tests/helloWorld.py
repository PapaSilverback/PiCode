import numpy as np
import cv2
import platform
from matplotlib import pyplot as plt


def imageGrayscaleConverter():
    """This method demos some basic features of OPENCV
        It will take in an image convert it to greyscale and then by pressing any key it will save the new image to a
        location.
    """
    # Load an color image in greyscale
    img = cv2.imread('alex.png', 0)
    # Tell if the image worked will print 'none' if it failed to load.
    print(img)
    cv2.imshow('image', img)  # open a new window and display the grey image.
    while True:
        k = cv2.waitKey(0)

        if k == 27:  # wait for ESC key to exit
            cv2.destroyAllWindows()
            break
        elif k == ord('s'):  # wait for 's' key to save and exit
            cv2.imwrite('alexGrey.png', img)
            cv2.destroyAllWindows()
            break
        else:
            print("Type Either an 's'(To save and Close) or press esc to close(without save)")

    print(platform.platform())
    return


def plotLibDemo():
    """Basic demo that will open the PLOTLib Screen and show the image."""
    img = cv2.imread('wombat.jpg', 0)
    print(img)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


def saveVideo():
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    out = cv2.VideoWriter('saveVideo.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', ret)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return


def recordVideo():
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    # fourcc = cv2.cv.CV_FOURCC(*'DIVX')
    # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    out = cv2.VideoWriter('record.avi', -1, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                playMovie()
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return


def basicVideoCapture():
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        hsv = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        keyPressed = cv2.waitKey(1) & 0xFF
        if keyPressed == ord('q'):
            break
        elif keyPressed == ord('p'):
            cv2.imshow('image', hsv)
            continue
        elif keyPressed == ord('v'):
            recordVideo()
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return


def playMovie():
    cap = cv2.VideoCapture('record.avi')
    print("movie Playing")
    while (cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return


# imageGrayscaleConverter()
# plotLibDemo()
basicVideoCapture()
#playMovie()
#saveVideo()
#recordVideo()
