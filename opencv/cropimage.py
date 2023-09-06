import cv2
import numpy as np
image = cv2.imread('panda.jpg')
print(image.shape)
resize = cv2.resize(image,(400,400))
imgcrop = image[200:400, 500:1000]
cv2.imshow('output',resize)
cv2.imshow('cropped image',imgcrop)
cv2.waitKey(0)