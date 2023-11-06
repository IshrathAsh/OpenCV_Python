import cv2 as cv
import numpy as np
# img = cv.imread('photos/eagle.jpeg')
blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('eagle',blank)
# blank[300:400,400:500]=0,0,255
# cv.imshow('red',blank)
cv.putText(blank,'Hello',(100,100),cv.FONT_HERSHEY_PLAIN,10.0,(0,0,255),1)
cv.imshow('eagle',blank)
cv.waitKey(0)