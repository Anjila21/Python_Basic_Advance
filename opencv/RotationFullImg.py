import cv2
import numpy as np

image = cv2.imread('ss.png')
height, width = image.shape[0:2]
x1, y1 = int(height * 0.00), int(width * 0.0)
x2, y2 = int(height * 0.50), int(width * 0.50)

# Crop the image using the corrected indices
cropimage = image[x1:x2, y1:y2]
# Convert the image to grayscale
gray = cv2.cvtColor(cropimage, cv2.COLOR_BGR2GRAY)

# Apply edge detection (optional, but can help in some cases)
edges = cv2.Canny(gray, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming the largest contour is the rectangle
largest_contour = max(contours, key=cv2.contourArea)

# Fit a line to the contour using least squares
[vx, vy, x, y] = cv2.fitLine(largest_contour, cv2.DIST_L2, 0, 0.01, 0.01)
print(vx,vy)
slope = np.arctan2(vy, vx) * 180 / np.pi
print(f"Slope of the rectangle: {slope}")
h, w = image.shape[:2]
center = (w // 2, h // 2)
slope = int(slope[0])
rotate = cv2.getRotationMatrix2D(center, slope, 1.0)
result = cv2.warpAffine(cropimage, rotate, (w, h))
cv2.imshow('Original Image1', image)
cv2.imshow('Rotated Image1', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
