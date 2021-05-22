import cv2
print(cv2.__version__)
dispW=640
dispH=480
centerW=int(dispW/2)
centerH=int(dispH/2)
flip=2
from adafruit_servokit import ServoKit
myKit=ServoKit(channels=16)
pan=60
tilt=120
myKit.servo[0].angle=pan
myKit.servo[1].angle=tilt

#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得
face_cascade=cv2.CascadeClassifier('/media/hisayuki/76B9-990C/toptechboy/pyPro/cascade/face.xml')
eye_cascade=cv2.CascadeClassifier('/media/hisayuki/76B9-990C/toptechboy/pyPro/cascade/eye.xml')

while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        gray_face=gray[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(gray_face,1.3,5)
        for (xEye,yEye,wEye,hEye) in eyes:
            cv2.rectangle(frame,(x+xEye,y+yEye),(x+xEye+wEye,y+yEye+hEye),(0,255,0),2)
            cv2.circle(frame,(int(x+xEye+wEye/2),int(y+yEye+hEye/2)),16,(0,0,255),-1)
        xPos=int((x+x+w)/2)
        yPos=int((y+y+h)/2)
        #cv2.line(frame,(0,yPos),(dispW,yPos),(0,255,0),1)
        #cv2.line(frame,(xPos,0),(xPos,dispH),(0,255,0),1)

        if xPos < centerW-int(dispW*0.1):
            pan=pan+2
        elif xPos > centerW+int(dispW*0.1):
            pan=pan-2
        else:
            print("centerW is true.")
        if yPos < centerH-int(dispH*0.1):
            tilt=tilt+2
        elif yPos > centerH+int(dispH*0.1):
            tilt=tilt-2
        else:
            print("centerH is true.")
        if pan > 180:
            pan = 180
        elif pan < 0:
            pan = 0
        if tilt > 180:
            tilt = 180
        elif tilt < 0:
            tilt = 0
        myKit.servo[0].angle=pan
        myKit.servo[1].angle=tilt
        break  

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()