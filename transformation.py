import cv2 as cv
# import numpy as np
img = cv.imread('photos/handloomh.jpg')
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)
def rotate(img,angle,rotationpoint=None):
    (h,w)=img.shape[:2]
    if rotationpoint is None:
        rotationpoint =(w//2,h//2)
        rotMat = cv.getRotationMatrix2D(rotationpoint,angle,1.0)
        dimensions= (w,h)
        return cv.warpAffine(img,rotMat,dimensions)
rtd = rotate(img,40)
cv.imshow('Rotated',rtd)
cv.waitKey(0)
