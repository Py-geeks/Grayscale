import cv2
import numpy as np

#reading imagae from file
img = cv2.imread("cat.png")

#GRAY SCALE
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#completion message
print('Image Grayscaled.')

#comparing original vs resized
cv2.imshow('ORIGINAL',img)
cv2.imshow('GRAYSCALE',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
