import cv2
import numpy as np

# Load the image
image = cv2.imread('ss.png')

def crop_rectangle_frm_img(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
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

crops = crop_rectangle_frm_img(image)
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Images ', crops[0])
cv2.imshow('Rotated Images1 ', crops[1])
cv2.imshow('Rotated Images2 ', crops[2])
cv2.imshow('Rotated Images3 ', crops[3])
cv2.waitKey(0)
cv2.destroyAllWindows()