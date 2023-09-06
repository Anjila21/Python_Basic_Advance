import cv2



points=[]
def getpoints(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),4,(255,0,0),-1)
        points.append([x,y])
        cv2.imshow('image',img)


        img = cv2.imread('ss1.png')
        img = cv2.resize(img,(400,300))
        cv2.imshow('image',img)
        cv2.setMouseCallback('image',getpoints)
        cv2.waitKey(0)
        cv2.destroyAllWindows()