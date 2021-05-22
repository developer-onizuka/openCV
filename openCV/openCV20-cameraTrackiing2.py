import cv2
print(cv2.__version__)
import numpy as np
from adafruit_servokit import ServoKit
myKit=ServoKit(channels=16)
#import time
pan=90
tilt=90
myKit.servo[0].angle=pan
myKit.servo[1].angle=tilt


def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)
cv2.createTrackbar('hueLower','Trackbars',0,179,nothing)
cv2.createTrackbar('hueUpper','Trackbars',0,179,nothing)
cv2.createTrackbar('hue2Lower','Trackbars',170,179,nothing)
cv2.createTrackbar('hue2Upper','Trackbars',179,179,nothing)
cv2.createTrackbar('satLow','Trackbars',80,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',221,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('areaLow','Trackbars',0,100000,nothing)
cv2.createTrackbar('areaHigh','Trackbars',100000,100000,nothing)
cv2.moveWindow('Trackbars',650,0)

dispW=640
dispH=480
centerW=int(dispW/2)
centerH=int(dispH/2)
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得

while True:
    ret, frame=cam.read()
    #frame=cv2.imread('smarties.png')
    #frame=cv2.resize(frame,(320,300))



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
    cv2.moveWindow('FGmaskComp',0,400)

    contours,_=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    #print(len(contours))
    #for cnt in contours:
    for i in range(len(contours)):
        #area=cv2.contourArea(cnt)
        area=cv2.contourArea(contours[i])
        (x,y,w,h)=cv2.boundingRect(contours[i])
        if area>=Al and area<=Ah:
            #cv2.drawContours(frame,[cnt],0,(0,255,0),2)
            #cv2.drawContours(frame,contours,i,(0,255,0),2)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            xPos=int((x+x+w)/2)
            yPos=int((y+y+h)/2)
            cv2.line(frame,(0,yPos),(dispW,yPos),(0,255,0),1)
            cv2.line(frame,(xPos,0),(xPos,dispH),(0,255,0),1)
            if xPos < centerW-int(dispW*0.1):
                pan=pan+2
            elif xPos > centerW+int(dispW*0.1):
                pan=pan-2
            else:
                print("centerW is true.")
            if yPos < centerH-int(dispH*0.1):
                tilt=tilt+2
            elif yPos > centerH+int(dispH*0.1):
                tilt=tilt-2
            else:
                print("centerH is true.")
            if pan > 180:
                pan = 180
            elif pan < 0:
                pan = 0
            if tilt > 180:
                tilt = 180
            elif tilt < 0:
                tilt = 0
            myKit.servo[0].angle=pan
            myKit.servo[1].angle=tilt
        break

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()