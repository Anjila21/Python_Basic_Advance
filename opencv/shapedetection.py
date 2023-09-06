import cv2
import numpy as np

image = cv2.imread('shapes.jpg')
imageRe = cv2.resize(image,(500,500))
gray = cv2.cvtColor(imageRe,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(7,7),3)
cv2.imshow('output',imageRe)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.waitKey(0)