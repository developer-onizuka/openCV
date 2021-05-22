import cv2
print(cv2.__version__)

#cam=cv2.VideoCapture(0)
cam=cv2.VideoCapture('myCam.avi')
fps = int(cam.get(cv2.CAP_PROP_FPS))                                # カメラのFPSを取得
dispW = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))                      # カメラの横幅を取得
dispH = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))                     # カメラの縦幅を取得
fourcc = cv2.VideoWriter_fourcc(*'XVID')                            # 動画保存時のfourcc設定（mp4用）


while True:
    ret, frame=cam.read()
    #frameSmall=cv2.resize(frame,(320,180))
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    #outVid.write(frame)
    if cv2.waitKey(50)==ord('q'):
        break
cam.release()

cv2.destroyAllWindows()