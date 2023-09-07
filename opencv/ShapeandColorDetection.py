import cv2

cap = cv2.VideoCapture(0)
cap.set(3,500)
cap.set(4,500)
while True:
    success,img= cap.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("video",img)
    cv2.imshow("hsv", hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

