import cv2
import numpy as np
print(cv2.__version__)

#coord=[]
#pnt=(0,0)
evt=-1
posA=int()
posB=int()
posC=int()
posD=int()
flag=int()
img=np.zeros((250,250,3),np.uint8)
def click(event,x,y,flags,parames):
    global pnt
    global evt
    global posA
    global posB
    global posC
    global posD
    global flag
    if event==cv2.EVENT_FLAG_LBUTTON:
        evt=-1
        print('Mouse Event Was DOWN: event=',event)  #event==1
        print(x,',',y)
        posA=x
        posB=y
        evt=event
        flag=1
    elif event==cv2.EVENT_MOUSEMOVE:
        #print('Mouse Event Is Moving: event=',event)  #event==0
        #print(x,',',y)
        posC=x
        posD=y
        evt=event
    elif event==cv2.EVENT_LBUTTONUP:
        print('Mouse Event Was UP: event=',event)  #event==4
        print(x,',',y)
        posC=x
        posD=y
        evt=event
        flag=0

dispW=640
dispH=480
#flip=2

cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',click)

#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得

while True:
    ret, frame=cam.read()

    if evt==4 or (evt==0 and flag==1):
        cv2.rectangle(frame,(posA,posB),(posC,posD),(0,255,0),2)

    #if evt==4 and (posA<posC and posB<posD):
    if evt==4 and (posA!=posC or posB!=posD):
        if posA > posC:
            tmp=posC
            posC=posA
            posA=tmp
        if posB > posD:
            tmp=posD
            posD=posB
            posB=tmp
        roi=frame[posB:posD,posA:posC].copy()
        roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
        frame[posB:posD,posA:posC]=roiGray
        frame=cv2.rectangle(frame,(posA,posB),(posC,posD),(255,0,0),2)
        cv2.imshow('ROI',roi)
        cv2.imshow('GRAY',roiGray)
        cv2.moveWindow('ROI',650,0)
        cv2.moveWindow('GRAY',650,250)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    KeyEvent=cv2.waitKey(1)
    if KeyEvent==ord('q'):
        break
    if KeyEvent==ord('c'):
        evt=-1

cam.release()
cv2.destroyAllWindows()
