import cv2 as cv
import numpy as np
img=cv.imread('photos/eagle.jpeg')
cv.imshow('normal',img)
# hsv = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('HSV',hsv)
b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2],dtype='uint8')
blue =cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

merged = cv.merge([b,g,r])
cv.imshow("Blank",merged)
cv.waitKey(0)