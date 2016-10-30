import cv2
import numpy as np
img = cv2.imread('mars.jpg')
px = img[100, 100] # get the pixel value from image at 100, 100
print (px) # returns something like [26 34 63]

blue = img[100, 100, 0] # accessiing just the blue pixel or 0 in the array. can change 0 to 1 or 2
print (blue)

img[100, 100] = [255, 255, 255] # change pixel value.
# Numpy is a optimized library for fast array calculations.
# So simply accessing each and every pixel values and
# modifying it will be very slow and it is discouraged.

# ***********Better method of accessing pixels*****************

better = img.item(100, 100, 1) # should be 255 because we set it above.
print(better)

print (img.shape)
print(img.size)
print(img.dtype)

extra = img[400:500, 400:500]
img[0:100, 0:100] = extra
cv2.imwrite('space.png', img)
img2 = cv2.imread('space.png')
b, g, r = cv2.split(img2)
img2 = cv2.merge((b, g, r))
e1 = cv2.getTickCount()
# your code execution
# Marshall was here!
img1 = cv2.imread('spaceWolf.jpg')
img2 = cv2.imread('space.png')
crop_img1 = img1[0:600, 0:1000] # Crop from [y1:y2, x1:x2]
crop_img2 = img2[0:600, 0:1000]
cv2.imwrite('testCrop.png', img2)
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

print("begin merge")

dst = cv2.addWeighted(crop_img1, 0.3, crop_img2, 0.7, 0)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)



cv2.imshow('dst', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()


