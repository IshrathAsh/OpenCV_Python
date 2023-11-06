import cv2 as cv
img = cv.imread('photos/eagle.jpeg')
average = cv.bilateralFilter(img,10,35,25)
cv.imshow('avg_blur',average)
cv.imshow('normal',img)
cv.waitKey(0)