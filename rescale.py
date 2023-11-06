import cv2 as cv
def rescale(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions =(width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)
img = cv.imread('photos/eagle.jpeg')
cv.imshow('eagle',img)
rescale_img = rescale(img,.2)
cv.imshow('eagle',rescale_img)
cv.waitKey(0)