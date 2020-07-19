import numpy as np
import cv2

#the following function recieves images in BGR format along with their width and height
# It returns a list containing x and y coordinates of all the corner points
# this function also displays corner points as red circle on the passed image
def corners(frame,h,w):
    img = frame.copy()
    # following line converts BGR to Gray , if passed image is RGB format then change BGR2GRAY to RGB2GRAY
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(gray, 100, 175)
    cv2.imshow('edges', edges)

    corner = cv2.goodFeaturesToTrack(edges, 100, 0.1, 10)
    c_nei = []
    try:
        corner = np.int0(corner)
        for i in corner:
            x, y = i.ravel()
            if ((y > 70) and (y < h - 70)):
                cv2.circle(img, (x, y), 3, (0, 0, 255), 2)
                for xx in range(30):
                    for yy in range(30):
                        c_nei.append((x + xx, y + yy))
                        c_nei.append((x - xx, y - yy))
            else:
                pass


    except:
        pass

    cv2.imshow('output', img)
    return c_nei
#Here I am using opencv to start video capture using default device camera
#the captured frames are passed to the above function
#change the following code to however you find suitable to capture frames as the method for that is different in IOS

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 1)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret,frame=cap.read()
    cs=corners(frame,h,w)
    if (cv2.waitKey(1) & 0xff == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()