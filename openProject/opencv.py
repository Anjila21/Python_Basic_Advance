import cv2
import numpy as np

image = cv2.imread("ss1.png")
reimage = cv2.resize(image, (500, 400))
pts1 = np.float32([[25,30], [193, 30], [13, 117], [180,117]])
pts2 = np.float32([[0, 0], [500, 0], [0, 400], [500, 400]])
mat = cv2.getPerspectiveTransform(pts1, pts2)

final = cv2.warpPerspective(reimage, mat, (500, 400))

cv2.imshow('output', final)
cv2.imshow('input', reimage)
cv2.waitKey(0)

