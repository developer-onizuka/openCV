import cv2
print(cv2.__version__)

#def nothing():
#    pass
#cv2.namedWindow('Blended')
#cv2.createTrackbar('BlendValue','Blended',50,100,nothing)

dispW=640
dispH=480
BW=80
BH=60
posX=200
posY=50
dx=1
dy=1
flip=2

cvLogo=cv2.imread('pl.jpg')
cvLogo=cv2.resize(cvLogo,(BW,BH))
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cv Logo Gray', cvLogoGray)
cv2.moveWindow('cv Logo Gray',645,0)

_,BGMask=cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',725,0)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask',FGMask)
cv2.moveWindow('FG Mask',805,0)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',885,0)

#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=28/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)                                 # カメラのFPSを取得
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)                      # カメラの横幅を取得
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)                     # カメラの縦幅を取得

while True:
    ret, frame=cam.read()
    roi=frame[posY:posY+BH,posX:posX+BW].copy()

    roiMasked=cv2.bitwise_and(roi,roi,mask=BGMask)
    cv2.imshow('roiMasked',roiMasked)
    cv2.moveWindow('roiMasked',725,100)
    
    compImage=cv2.add(roiMasked,FG)
    cv2.imshow('compImage',compImage)
    cv2.moveWindow('compImage',885,100)

    #BV=cv2.getTrackbarPos('BlendValue','Blended')/100
    BV=0.3
    BV2=1-BV

    Blended=cv2.addWeighted(roi,BV,cvLogo,BV2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',965,0)

    BlendedMasked=cv2.bitwise_and(Blended,Blended,mask=FGMask)
    cv2.imshow('BlendedMasked',BlendedMasked)
    cv2.moveWindow('BlendedMasked',965,100)

    compFinal=cv2.add(roiMasked,BlendedMasked)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('compFinal',965,200)

    frame[posY:posY+BH,posX:posX+BW]=compFinal
    
    posX=posX+dx
    posY=posY+dy
    if posX<=0 or posX+BW>=dispW:
        dx=dx*(-1)
    if posY<=0 or posY+BH>=dispH:
        dy=dy*(-1)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()