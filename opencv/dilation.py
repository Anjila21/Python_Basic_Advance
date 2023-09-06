import cv2
import numpy as np
image = cv2.imread('panda.jpg')
resize = cv2.resize(image,(300,400))
kernel = np.ones((5,5),np.uint8)
edge = cv2.Canny(resize,100,100)
dilation = cv2.dilate(edge,kernel, iterations=1)
cv2.imshow('Edge Detection', edge)
cv2.imshow('Image dilation', dilation)
cv2.waitKey(0)
