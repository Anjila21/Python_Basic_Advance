import cv2
import numpy as np
input = cv2.imread('ss.png')


width,height = 809,548
pts1 = np.float32([[517,295],[698,397],[450,406],[629,510]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
final = cv2.warpPerspective(input,matrix,(width,height))


cv2.imshow('input',input)
cv2.imshow('output',final)
cv2.waitKey(0)