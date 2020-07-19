import cv2
import numpy as np


cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    img=frame.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)
    minLineLength = 10
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    try:
        for x in range(len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                #cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
                cv2.circle(img, (x1, y1), 3, (255, 0, 0), 3)

                cv2.circle(img, (x2, y2), 3, (255, 0, 0), 3)

    except:
        pass
    cv2.imshow('out', img)
    if(cv2.waitKey(1) & 0xff==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()



