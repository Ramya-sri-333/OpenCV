###### corner detection in a chessboard

import numpy as np
import cv2

#load the image
img = cv2.imread(r"C:\Users\HariChukka\Desktop\python\chessboard.png")

img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)#reduce the size of the image
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #COVERT INTO GRAY SCALE

#display the image
cv2.imshow("Chessboard",img)
cv2.waitKey(0)# 0 press any key to close
cv2.destroyAllWindows()

###################################################
#NOW RUN OVER THIS CONER DETECTION ALGORITHEM

import numpy as np
import cv2

#load the image
img = cv2.imread(r"C:\Users\HariChukka\Desktop\python\chessboard.png")

img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)#reduce the size of the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #COVERT INTO GRAY SCALE

#DETECT CORNERS Algorithem
corners= cv2.goodFeaturesToTrack(gray,100,0.01,10)
# 100 is the number of best corners to identify,0.01 is the
#quality of the corney i.e algorithem is not sure if itis a exact
#corner or not (like the degree of confidence the program has )
#if the o/p is not expected then increas number like 0.5
#10 is the distance between two corners.if there are really close it will igonore one iteam.it can be 20 as well


#the ouput of corners is float do convert into int

corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x:int(x),np.random.randint(0,255,size = 3)))
        cv2.line(img,corner1,corner2,color,1)
#display the image
cv2.imshow("Chessboard",img)
cv2.waitKey(0)# 0 press any key to close
cv2.destroyAllWindows()
