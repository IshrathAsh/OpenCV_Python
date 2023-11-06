import cv2 as cv
img = cv.imread('photos/eagle.jpeg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

threshold , thresh =cv.threshold(gray,200 ,255,cv.THRESH_BINARY)
cv.imshow('gray',thresh)
threshold , thresh_inv =cv.threshold(gray,200 ,255,cv.THRESH_BINARY_INV)
cv.imshow('grayinv',thresh_inv)
adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,51,3)
cv.imshow('adptthresh',adaptive_threshold)
adaptive_thresholdinv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,51,3)
cv.imshow('adptthreshy',adaptive_thresholdinv)
cv.waitKey(0) 