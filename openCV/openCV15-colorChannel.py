import cv2
import numpy as np
print(cv2.__version__)
dispW=320
dispH=240
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得

blank=np.zeros([240,320,1],np.uint8)
while True:
    ret, frame=cam.read()
    #print (frame[200,300,0])
    #print(frame.shape)
    #print(frame.size)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #print(gray.shape)
    #print(gray.size)
    
    b,g,r=cv2.split(frame)
    blue=cv2.merge((b,blank,blank))
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))

    b[:]=b[:]*.1
    merge=cv2.merge((b,g,r))
    merge2=cv2.add(blue,green)
    merge3=cv2.add(merge2,red)

    #b=cv2.split(frame)[0]
    #g=cv2.split(frame)[1]
    #r=cv2.split(frame)[2]
    cv2.imshow('nanoCam-Blue',blue)
    cv2.moveWindow('nanoCam-Blue',400,0)
    cv2.imshow('nanoCam-Green',green)
    cv2.moveWindow('nanoCam-Green',800,0)
    cv2.imshow('nanoCam-Red',red)
    cv2.moveWindow('nanoCam-Red',1200,0)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    cv2.imshow('merge',merge)
    cv2.moveWindow('merge',0,300)
    cv2.imshow('merge2',merge2)
    cv2.moveWindow('merge2',800,300)
    cv2.imshow('merge3',merge3)
    cv2.moveWindow('merge3',1200,300)

    cv2.imshow('blank',blank)
    cv2.moveWindow('blank',400,300)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()