import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        print(x,y)




cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()

    img=frame.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray, 100, 175)
    cv2.imshow('frame', edges)
    dst = cv2.cornerHarris(edges, 2, 3, 0.04)
    dst = cv2.dilate(dst, None,iterations=1)

    img[dst >0.1*dst.max()] = [0, 0, 255]
    cv2.imshow('out',img)

    out_pts=np.where(dst>0.1*dst.max())
    cl=[]
    for x in range(len(out_pts[0])):
        cl.append((out_pts[1][x],out_pts[0][x]))

    cv2.setMouseCallback('out',click_event)
    cv2.imshow('outing', img)

    if(cv2.waitKey(1) & 0xff==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()



