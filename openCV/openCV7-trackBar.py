import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
def nothing(x):
    pass
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得
cv2.namedWindow('nanoCam')
cv2.createTrackbar('xVal','nanoCam',25,dispW,nothing)
cv2.createTrackbar('yVal','nanoCam',25,dispH,nothing)


while True:
    ret, frame=cam.read()
    xVal=cv2.getTrackbarPos('xVal','nanoCam')
    yVal=cv2.getTrackbarPos('yVal','nanoCam')
    cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)
    #print(xVal, yVal)
    
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
