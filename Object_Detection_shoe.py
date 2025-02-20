#obeject detection/Template Matching

import numpy as np
import cv2

img =cv2.resize(cv2.imread(r"C:\Users\HariChukka\Desktop\python\soccer_practice.jpg",0),(0,0),fx=0.5,fy=0.5)
template= cv2.resize(cv2.imread(r"C:\Users\HariChukka\Desktop\python\shoe.png",0),(0,0),fx=0.5,fy=0.5)

height,width=template.shape#2D array h,w


#methods available in algorithems copy from doc and run over all to find the best one
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()#this to draw rectangle on this rather on orginal
    result = cv2.matchTemplate(img2,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0]+width,location[1]+height)
    cv2.rectangle(img2,location,bottom_right,255,5)#255 black clr, 5 tickness of line
    cv2.imshow("matchframe",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()












    #https://www.youtube.com/watch?v=T-0lZWYWE9Y&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=7
    
