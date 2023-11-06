# bitwise
import cv2 as cv
import numpy as np
img= cv.imread('photos/eagle.jpeg')
blank = np.zeros(img.shape[:2],dtype='uint8')
# rectangle = cv.rectangle(blank.copy(),(30,30),(200,200),255,-1)
# circle = cv.circle(blank.copy(),(200,200),200,255,-1)
mask = cv.circle  (blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask',masked)
cv.waitKey(0)

