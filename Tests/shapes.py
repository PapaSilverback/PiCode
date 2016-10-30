import numpy as np
import cv2


def drawLine():
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)

    # Draw a diagonal blue line with thickness of 5 px
    img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    img2 = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    img3 = cv2.circle(img, (50, 50), 15, (0, 0, 255), 12)
    img4 = cv2.ellipse(img, (256, 256), (50, 50), 300, 0, 300, 255, 10)
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 255))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'Master Control', (10, 500), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    assert isinstance(img, object)
    return img



cv2.imshow('image', drawLine())
k = cv2.waitKey(0)
cv2.destroyAllWindows()
