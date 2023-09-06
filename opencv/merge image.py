import cv2
import numpy as np

img = cv2.imread('ss1.png')

imgVer = np.vstack((img,img))

cv2.imshow('output',imgVer)
cv2.waitKey(0)