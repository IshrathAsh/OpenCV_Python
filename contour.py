import cv2 as cv
import numpy as np
def rescale(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions =(width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)
img = cv.imread('photos/eagle.jpeg')

rescale_img = rescale(img,.5)
# cv.imshow('Eagle',rescale_img)
gray = cv.cvtColor(rescale_img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
blur = cv.GaussianBlur(gray,(17,17),cv.BORDER_DEFAULT)
# cv.imshow('bLUR',blur)
canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)
# ret,thresh = cv.threshold(gray,125,225,cv.THRESH_BINARY)
countours,heirarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.imshow('THRESH',thresh)
cv.drawContours(rescale_img,countours,-1,(0,255,255),2)
cv.imshow('Contours Drawn',rescale_img)
print(f'{len(countours)} countour(s) found!')
cv.waitKey(0)