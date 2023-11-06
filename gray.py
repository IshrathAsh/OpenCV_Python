import cv2 as cv 
img = cv.imread('photos/eagle.jpeg')
cv.imshow('Eagle',img)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

dilate=cv.dilate(canny,(10,10),iterations=2)
cv.imshow('Dilate',dilate)

erode=cv.erode(dilate,(10,10),iterations=2)
cv.imshow('Erode',erode)

cv.waitKey(0)