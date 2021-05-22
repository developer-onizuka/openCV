import cv2
print(cv2.__version__)
dispW=640
dispH=480
#flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                # カメラのFPSを取得
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
    frame=cv2.rectangle(frame,(140,100),(250,170),(255,255,0),7)
    frame=cv2.circle(frame,(320,240),50,(0,0,255),7)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame, 'my first text',(300,300),fnt,1.5,(255,0,150),2)
    frame=cv2.line(frame,(10,10),(630,470),(0,0,0),4)
    frame=cv2.arrowedLine(frame,(10,470),(630,10),(255,0,0),1)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()