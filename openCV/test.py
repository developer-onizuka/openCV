import numpy as np
import cv2

#cam = cv2.VideoCapture('myCam.avi')
cam=cv2.VideoCapture('myCam.avi')
#while True:
#    ret, frame = cam.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#    cv2.imshow('frame',gray)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


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


