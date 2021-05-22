import cv2
print(cv2.__version__)
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)
cv2.createTrackbar('hueLower','Trackbars',50,179,nothing)
cv2.createTrackbar('hueUpper','Trackbars',100,179,nothing)
cv2.createTrackbar('satLow','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)
cv2.moveWindow('Trackbars',420,0)

dispW=640
dispH=480
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得

while True:
    #ret, frame=cam.read()
    frame=cv2.imread('smarties.png')
    frame=cv2.resize(frame,(320,300))
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)


    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow=cv2.getTrackbarPos('hueLower','Trackbars')
    hueUp=cv2.getTrackbarPos('hueUpper','Trackbars')
    Ls=cv2.getTrackbarPos('satLow','Trackbars')
    Us=cv2.getTrackbarPos('satHigh','Trackbars')
    Lv=cv2.getTrackbarPos('valLow','Trackbars')
    Uv=cv2.getTrackbarPos('valHigh','Trackbars')

    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])

    FGmask=cv2.inRange(hsv,l_b,u_b)
    cv2.imshow('FGmaskComp',FGmask)
    cv2.moveWindow('FGmaskComp',0,400)

    FG=cv2.bitwise_and(frame,frame,mask=FGmask)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',840,0)

    BGmask=cv2.bitwise_not(FGmask)
    cv2.imshow('BGmask',BGmask)
    cv2.moveWindow('BGmask',420,400)

    BG=cv2.cvtColor(BGmask,cv2.COLOR_GRAY2BGR)
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',1260,0)

    final=cv2.add(FG,BG)
    cv2.imshow('final',final)
    cv2.moveWindow('final',840,400)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()