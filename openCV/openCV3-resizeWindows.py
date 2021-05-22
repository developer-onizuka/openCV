import cv2
print(cv2.__version__)
dispW=320
dispH=240
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame=cam.read()



    cv2.moveWindow('nanoCam',700,0)
    cv2.imshow('nanoCam',frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameSmall=cv2.resize(frame,(320,240))
    graySmall=cv2.resize(gray,(320,240))

    cv2.moveWindow('BW',0,265)
    cv2.moveWindow('nanoSmall',0,0)
    cv2.imshow('BW',graySmall)
    cv2.imshow('nanoSmall',frameSmall)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()