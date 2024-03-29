import cv2 as cv
import numpy as np
img =cv.imread('photos/man.jpeg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
haar_cascade = cv.CascadeClassifier('haar_cascade.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
print(f'No of faces detected={len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected',img)  
cv.waitKey(0)