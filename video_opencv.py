import numpy as np
import cv2

cap = cv2.VideoCapture(r"C:\Users\HariChukka\Desktop\python\DSC_0210.MOV")#loading the data , or connecting to input/webcam 

while True:
    ret,frame = cap.read() # ret is throw whether the frame (read has be worked or not) i.e if wabcam is in use by other user and cant load or conncened it throws an error
    cv2.imshow("frame",frame)# imshow to show the r esultant output

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

###########################################################################################################

cap = cv2.VideoCapture(r"D:\Pictures_Shoot\july_2020\Vedios\IMG_2741.MOV")# loading the data 



while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(500,600)) #resize the image/frames output
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):#press q to exit the output/video
        break

cap.release()
cv2.destroyAllWindows()
#####################################################################################
import numpy as np
import cv2

cap = cv2.VideoCapture(r"D:\Pictures_Shoot\july_2020\Vedios\IMG_2741.MOV")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(500,600))

    image=np.zeros(frame.shape,np.uint8)#creating empty numpy array image=np.zeros()like empty canvas
                                    #default black if it is zero shape should be identical to frame mentioned above so frame.shape
                                    #uint is unsigned integer
    cv2.imshow('frame',image)
    

    if cv2.waitKey(1) == ord('q'):#press q to exit the output/video
        break

cap.release()
cv2.destroyAllWindows()
#the rusult of this code is black canvas

##################################################################################################################
import numpy as np
import cv2

cap = cv2.VideoCapture(r"D:\Pictures_Shoot\july_2020\Vedios\IMG_2741.MOV")


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))#orginal width of the frame intially captured #3 is width 4 is height
    height = int(cap.get(4))#cap.get gives the width propert of the frame
    
    

    image=np.zeros(frame.shape,np.uint8)#creating empty numpy array image=np.zeros()like empty canvas
                                    #default black if it is zero shape should be identical to frame mentioned above so frame.shape
                                    #uint is unsigned integer

    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)#i am shrinking the image to half
    image[:height//2,:width//2]= smaller_frame #to past in each quaderents,start from 0 to hight/2 ,0 to width/2
                                            #top left
    image[height//2:,:width//2]= smaller_frame # bottom left
    image[:height//2,width//2:]= smaller_frame #top right
    image[height//2:,width//2:]= smaller_frame # bottom right
    cv2.imshow('frame',image)
    

    if cv2.waitKey(1) == ord('q'):#press q to exit the output/video
        break

cap.release()
cv2.destroyAllWindows()

#o/p video is projected in 4 quadrents (multiple times)
#########################################################################################################################
