import cv2
import numpy as np

# Load the image
image = cv2.imread("ss2.png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_contour = None
max_slope_degrees = None

for contour in contours:

    if len(contour) >= 2:
        [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)


        slope_degrees = np.arctan2(vy, vx) * 180 / np.pi


        if max_slope_degrees is None or abs(slope_degrees) > abs(max_slope_degrees):
            max_slope_degrees = slope_degrees
            max_contour = contour

if max_contour is not None:

    h, w = image.shape[:2]


    center = (w // 2, h // 2)


    rotate = cv2.getRotationMatrix2D(center, max_slope_degrees, 1.0)


    result = cv2.warpAffine(image, rotate, (w, h))

    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

