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

fps = int(cam.get(cv2.CAP_PROP_FPS))                                # カメラのFPSを取得
#dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))                      # カメラの横幅を取得
#dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))                     # カメラの縦幅を取得
#fourcc = cv2.VideoWriter_fourcc(*'XVID')                            # 動画保存時のfourcc設定（mp4用）
#outVid = cv2.VideoWriter('myCam.avi', fourcc, fps, (dispW, dispH))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

BW=int(.25*dispW)
BH=int(.15*dispH)
posX=10
posY=270
dx=2
dy=2

print("Your WebCam's WIDTH is", dispW)
print("Your WebCam's HIGHT is", dispH)
print("Your WebCam's FPS is", fps)

while True:
    ret, frame=cam.read()

    cv2.moveWindow('nanoCam',0,0)
    frame=cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),-1)
    cv2.imshow('nanoCam',frame)
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