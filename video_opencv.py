import numpy as np
import cv2

cap = cv2.VideoCapture(r"C:\Users\HariChukka\Desktop\python\DSC_0210.MOV")

while True:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
