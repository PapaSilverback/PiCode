import cv2
flags= [i for i in dir(cv2) if i.startswith('COLO_')]
print (flags)