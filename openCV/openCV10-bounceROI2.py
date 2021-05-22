import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得

BW=int(.25*dispW)
BH=int(.15*dispH)
posX=200
posY=50
dx=2
dy=2

while True:
    ret, frame=cam.read()
    roi=frame[posY:posY+BH,posX:posX+BW].copy()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameGray=cv2.cvtColor(frameGray,cv2.COLOR_GRAY2BGR)
    roiGray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    frameGray[posY:posY+BH,posX:posX+BW]=roi
    frameGray=cv2.rectangle(frameGray,(posX,posY),(posX+BW,posY+BH),(255,0,0),3)

    cv2.imshow('ROI',roi)
    cv2.imshow('nanoCam',frameGray)
    cv2.imshow('GRAY',roiGray)
    
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('GRAY',705,250)
    cv2.moveWindow('nanoCam',0,0)
    
    posX=posX+dx
    posY=posY+dy
    if posX<=0 or posX+BW>=dispW:
        dx=dx*(-1)
    if posY<=0 or posY+BH>=dispH:
        dy=dy*(-1)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
