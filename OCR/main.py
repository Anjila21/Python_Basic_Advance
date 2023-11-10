# libraries used :
# 1.Opencv: To read the input image
# 2.Tesseract API: which is a deep Learning API , detect text inside the image

import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
config = 'digits'
image = cv2.imread("images\\sample.jpg")
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# prints RGB image
# print (pytesseract.image_to_string(img_RGB))

# Prints numeric digits only
# results = pytesseract.image_to_boxes(img_RGB,config= config)
# ih, iw, ic = image.shape
# for box in results.splitlines():
#     box = box.split(' ')
#     print(box)
#
#     x,y,w,h = int(box[1]),  int(box[2])  ,int(box[3]),  int(box[4])
#     cv2.rectangle(image,(x,ih-y),(w,ih-h),(0,255,0),2)
#     cv2.putText(image,box[0],(x,ih-h),cv2.FONT_HERSHEY_SIMPLEX,1,(0 , 211 , 223), 1)

results = pytesseract.image_to_data(img_RGB)
for id, lines in enumerate(results.splitlines()):

    if id != 0:
        lines = lines.split()
        if len(lines) == 12:
            x, y, w, h = int(lines[6]), int(lines[7]), int(lines[8]), int(lines[9])
            cv2.rectangle(image, (x, y), (w + h, h + y), (0, 255, 0), 2)
            cv2.putText(image, lines[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

cv2.imshow("Input", image)
cv2.waitKey(0)
