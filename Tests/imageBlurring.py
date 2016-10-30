import cv2
import numpy as np
from matplotlib import pyplot as plt
#
# img = cv2.imread('alex.png')
#
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)
#
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()


img2 = cv2.imread('space.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img2,-1,kernel)
# blur is added using Gaussian to swith between filters change which to show.
blur = cv2.GaussianBlur(img2,(5,5),0)
median = cv2.medianBlur(img2,5)
blurEdge = cv2.bilateralFilter(img2,9,75,75)
plt.subplot(121),plt.imshow(img2),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blurEdge),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()