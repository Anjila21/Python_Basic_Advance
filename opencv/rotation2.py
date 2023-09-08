#Cropping images and rotating (image ss into ss1,ss2,ss3 and ss4)
import cv2
import numpy as np

# Load the image
image = cv2.imread('ss.png')

def crop_rectangle_frm_img(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thrash = cv2.threshold(img_gray, 240, 255, cv2.CHAIN_APPROX_NONE)
    contours, _ = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cropped_rect_images = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.015 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            cropped_image = image[y:y + h, x:x + w]
            cropped_rect_images.append(cropped_image)
    return cropped_rect_images


def rotation(image):
    edges = cv2.Canny(image, 50, 150)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assuming the largest contour is the rectangle
    largest_contour = max(contours, key=cv2.contourArea)

    # Fit a line to the contour using least squares
    [vx, vy, x, y] = cv2.fitLine(largest_contour, cv2.DIST_L2, 0, 0.01, 0.01)
    # print(vx,vy)


    slope = np.arctan2(vy, vx) * 180 / np.pi
    # print(f"Slope of the rectangle: {slope}")

    h, w = image.shape[:2]

    center = (w // 2, h // 2)
    slope = int(slope[0])


    rotate = cv2.getRotationMatrix2D(center, slope, 1.0)


    result = cv2.warpAffine(image, rotate, (w, h))
    return result

crops = crop_rectangle_frm_img(image)

rotated0 = rotation(crops[0])
rotated1 = rotation(crops[1])
rotated2 = rotation(crops[2])
rotated3 = rotation(crops[3])
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Images ', rotated0)
cv2.imshow('Rotated Images1 ', rotated1)
cv2.imshow('Rotated Images2 ', rotated2)
cv2.imshow('Rotated Images3 ', rotated3)
# cv2.imshow('Rotated Images1 ', crops[1])
# cv2.imshow('Rotated Images2 ', crops[2])
# cv2.imshow('Rotated Images3 ', crops[3])
cv2.waitKey(0)
cv2.destroyAllWindows()