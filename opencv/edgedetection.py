import cv2
image = cv2.imread('panda.jpg')
edge = cv2.Canny(image,100,100)
cv2.imshow('Edge Detection', edge)
cv2.waitKey(0)
