import cv2
import numpy as np

# Load the image
image = cv2.imread('ss1.png')
image2 = cv2.imread('ss2.png')
image3 = cv2.imread('ss3.png')
image4 = cv2.imread('ss4.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
gray4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)

# Apply edge detection (optional, but can help in some cases)
edges = cv2.Canny(gray, 50, 150)
edges2 = cv2.Canny(gray2, 50, 150)
edges3= cv2.Canny(gray3, 50, 150)
edges4 = cv2.Canny(gray4, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(edges2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours3, _ = cv2.findContours(edges3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours4, _ = cv2.findContours(edges4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Assuming the largest contour is the rectangle
largest_contour = max(contours, key=cv2.contourArea)
largest_contour2 = max(contours2, key=cv2.contourArea)
largest_contour3 = max(contours3, key=cv2.contourArea)
largest_contour4 = max(contours4, key=cv2.contourArea)

# Fit a line to the contour using least squares
[vx1, vy1, x, y] = cv2.fitLine(largest_contour, cv2.DIST_L2, 0, 0.01, 0.01)
print(vx1,vy1)
[vx2, vy2, x2, y2] = cv2.fitLine(largest_contour2, cv2.DIST_L2, 0, 0.01, 0.01)
print(vx2,vy2)
[vx3, vy3, x3, y3] = cv2.fitLine(largest_contour3, cv2.DIST_L2, 0, 0.01, 0.01)
print(vx3,vy3)
[vx4, vy4, x4, y4] = cv2.fitLine(largest_contour4, cv2.DIST_L2, 0, 0.01, 0.01)
print(vx4,vy4)

slope = np.arctan2(vy1, vx1) * 180 / np.pi
slope2 = np.arctan2(vy2, vx2) * 180 / np.pi
slope3 = np.arctan2(vy3, vx3) * 180 / np.pi
slope4 = np.arctan2(vy4, vx4) * 180 / np.pi

print(f"Slope of the rectangle: {slope}")


h, w = image.shape[:2]



center = (w // 2, h // 2)
slope = int(slope[0])


rotate = cv2.getRotationMatrix2D(center, slope, 1.0)


result = cv2.warpAffine(image, rotate, (w, h))


print(f"Slope of the rectangle: {slope2}")


h2, w2 = image2.shape[:2]



center2 = (w2 // 2, h2 // 2)
slope2 = int(slope2[0])


rotate2 = cv2.getRotationMatrix2D(center2, slope2, 1.0)


result2 = cv2.warpAffine(image2, rotate2, (w2, h2))
print(f"Slope of the rectangle: {slope3}")


h3, w3 = image3.shape[:2]



center3 = (w3 // 2, h3 // 2)
slope3 = int(slope3[0])


rotate3 = cv2.getRotationMatrix2D(center3, slope3, 1.0)


result3 = cv2.warpAffine(image3, rotate3, (w3, h3))
print(f"Slope of the rectangle: {slope4}")


h4, w4 = image4.shape[:2]



center4 = (w4 // 2, h4 // 2)
slope4 = int(slope4[0])


rotate4 = cv2.getRotationMatrix2D(center4, slope4, 1.0)


result4 = cv2.warpAffine(image4, rotate4, (w4, h4))

cv2.imshow('Original Image1', image)
cv2.imshow('Rotated Image1', result)
cv2.imshow('Original Image2', image2)
cv2.imshow('Rotated Image2', result2)
cv2.imshow('Original Image3', image3)
cv2.imshow('Rotated Image3', result3)
cv2.imshow('Original Image4', image4)
cv2.imshow('Rotated Image4', result4)
cv2.waitKey(0)
cv2.destroyAllWindows()