import cv2
import numpy as np
print(cv2.__version__)

evt=-1
coord=[]
img=np.zeros((250,250,3),np.uint8)
def click(event,x,y,flags,parames):
    global pnt
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ', event)
        print(x,',',y)
        pnt=(x,y)
        coord.append(pnt)
        #print(coord)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x,',',y)
        blue=frame[y,x,0]
        green=frame[y,x,1]
        red=frame[y,x,2]
        print(blue,green,red)
        colorString=str(blue)+','+str(green)+','+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_PLAIN
        r=255-int(red)
        g=255-int(green)
        b=255-int(blue)
        tp=(b,g,r)
        cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
        cv2.imshow('myColor',img)

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

#fps = int(cam.get(cv2.CAP_PROP_FPS))                                # カメラのFPSを取得
#dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))                      # カメラの横幅を取得
#dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))                     # カメラの縦幅を取得
#fourcc = cv2.VideoWriter_fourcc(*'XVID')                            # 動画保存時のfourcc設定（mp4用）
#outVid = cv2.VideoWriter('myCam.avi', fourcc, fps, (dispW, dispH))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

#print("Your WebCam's WIDTH is", dispW)
#print("Your WebCam's HIGHT is", dispH)
#print("Your WebCam's FPS is", fps)

while True:
    ret, frame=cam.read()
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,0,255),-1)
        font=cv2.FONT_HERSHEY_PLAIN
        myStr=str(pnts)
        cv2.putText(frame,myStr,pnts,font,1.5,(255,0,0),2)
#    if evt==1:
#        cv2.circle(frame,pnt,5,(0,0,255),-1)
#        font=cv2.FONT_HERSHEY_PLAIN
#        myStr=str(pnt)
#        cv2.putText(frame,myStr,pnt,font,1.5,(255,0,0),2)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    KeyEvent=cv2.waitKey(1)
    if KeyEvent==ord('q'):
        break
    if KeyEvent==ord('c'):
        coord=[]
cam.release()
cv2.destroyAllWindows()