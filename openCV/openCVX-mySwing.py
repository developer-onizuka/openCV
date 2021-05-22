import cv2
print(cv2.__version__)
import numpy as np

def nothing(x):
    pass
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)
cv2.createTrackbar('hueLower','Trackbars',80,179,nothing)
cv2.createTrackbar('hueUpper','Trackbars',179,179,nothing)
cv2.createTrackbar('hue2Lower','Trackbars',80,179,nothing)
cv2.createTrackbar('hue2Upper','Trackbars',179,179,nothing)
cv2.createTrackbar('satLow','Trackbars',0,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',8,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',75,255,nothing)
cv2.createTrackbar('areaLow','Trackbars',6220,100000,nothing)
cv2.createTrackbar('areaHigh','Trackbars',20588,100000,nothing)
cv2.moveWindow('Trackbars',428,0)

cam=cv2.VideoCapture('mySwing2.MOV')
dispW=426
dispH=640

while True:
    ret, frame=cam.read()

    if ret:
        frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        frame=cv2.resize(frame,(dispW,dispH))

        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        hueLow=cv2.getTrackbarPos('hueLower','Trackbars')
        hueUp=cv2.getTrackbarPos('hueUpper','Trackbars')
        hue2Low=cv2.getTrackbarPos('hue2Lower','Trackbars')
        hue2Up=cv2.getTrackbarPos('hue2Upper','Trackbars')
        Ls=cv2.getTrackbarPos('satLow','Trackbars')
        Us=cv2.getTrackbarPos('satHigh','Trackbars')
        Lv=cv2.getTrackbarPos('valLow','Trackbars')
        Uv=cv2.getTrackbarPos('valHigh','Trackbars')
        Al=cv2.getTrackbarPos('areaLow','Trackbars')
        Ah=cv2.getTrackbarPos('areaHigh','Trackbars')
        l_b=np.array([hueLow,Ls,Lv])
        u_b=np.array([hueUp,Us,Uv])
        l_b2=np.array([hue2Low,Ls,Lv])
        u_b2=np.array([hue2Up,Us,Uv])
        FGmask=cv2.inRange(hsv,l_b,u_b)
        FGmask2=cv2.inRange(hsv,l_b2,u_b2)
        FGmaskComp=cv2.add(FGmask,FGmask2)
        cv2.imshow('FGmaskComp',FGmaskComp)
        cv2.moveWindow('FGmaskComp',752,0)

        contours,_=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contours)):
            area=cv2.contourArea(contours[i])
            (x,y,w,h)=cv2.boundingRect(contours[i])
            if area>=Al and area<=Ah:
                cv2.drawContours(frame,contours,i,(255,0,0),3)
                #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                xPos=int((x+x+w)/2)
                yPos=int((y+y+h)/2)
                #cv2.line(frame,(0,yPos),(dispW,yPos),(0,255,0),1)
                #cv2.line(frame,(xPos,0),(xPos,dispH),(0,255,0),1)

        cv2.imshow('nanoCam',frame)
        cv2.moveWindow('nanoCam',0,0)

    if not ret:
        cam.set(cv2.CAP_PROP_POS_FRAMES,0)

    #outVid.write(frame)
    if cv2.waitKey(50)==ord('q'):
        break
cam.release()

cv2.destroyAllWindows()