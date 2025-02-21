import numpy as np
import cv2


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 


while True:
    ret,frame = cap.read()#load thevideo into frames
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert the frames into gray scale
    faces = face_cascade.detectMultiScale(gray,1.3,5)# detect all the faces in the frame
    
    for (x,y,w,h) in faces:#loop throught all the faces in the frame
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)#draw a rectangles around the face
        roi_gray = gray[y:y+w,x:x+w]#figure out the are in the actual image that represent our face 
        roi_color= frame[y:y+h,x:x+w]# reference to original frame in color
        eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)#we find the eyes on the face ,find the location of eyes
        for (ex,ey,ew,eh) in eyes :
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
































    



cap.release()
cv2.destroyAllWindows()
