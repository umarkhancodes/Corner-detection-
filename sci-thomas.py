import cv2
import numpy as np


def click_event(event,x,y,flags,param):

    if (event==cv2.EVENT_LBUTTONDOWN):
        if((x,y) in c_nei):
            print('corner point ',x,y)



cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 1)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(cap.isOpened()):
    ret,frame=cap.read()
    if (ret==True):
        img=frame.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        edges = cv2.Canny(gray, 100, 175)
        cv2.imshow('edges', edges)

        corner = cv2.goodFeaturesToTrack(edges, 100, 0.1,10 )
        c_nei=[]
        try:
            corner = np.int0(corner)
            for i in corner:
                x, y = i.ravel()
                if((y>70) and (y<h-70)):
                    cv2.circle(img, (x, y), 3, (0, 0, 255), 2)
                    for xx in range(30):
                        for yy in range(30):
                            c_nei.append((x+xx,y+yy))
                            c_nei.append((x-xx,y-yy))
                else:
                    pass

        except:
            pass



        cv2.imshow('output',img)
        cv2.setMouseCallback('output', click_event)



        if(cv2.waitKey(1) & 0xff==ord('q')):
            break


cap.release()
cv2.destroyAllWindows()



