import cv2

img1 = cv2.imread(r"C:\Users\HariChukka\Downloads\47 Bhagavad Gita Quotes ideas in 2021 _ gita quotes, bhagavad gita, serve god.jpeg",-1)

img1 = cv2.resize(img1,(300,400))

cv2.imshow("a_man_with_glasses",img1)
print(img1)
print(img1.shape)
##

##img2 = cv2.imread(r"C:\Users\HariChukka\Downloads\47 Bhagavad Gita Quotes ideas in 2021 _ gita quotes, bhagavad gita, serve god.jpeg",0)
##
##img2 = cv2.resize(img2,(300,400))
##
##cv2.imshow("gray_scale_image",img2)

##
img3 = cv2.imread(r"C:\Users\HariChukka\Downloads\47 Bhagavad Gita Quotes ideas in 2021 _ gita quotes, bhagavad gita, serve god.jpeg",-1)

img3 = cv2.resize(img3,(300,400))

cv2.imshow("alpha_image",img3)

 cv2.waitkey(0)

cv2.destroyAllWindows()

img4 =cv2.imread(r"C:\Users\HariChukka\Downloads\47 Bhagavad Gita Quotes ideas in 2021 _ gita quotes, bhagavad gita, serve god.jpeg",0)
img4= cv2.resize(img4,(300,400))
img4=cv2.flip(img4,0)
cv2.imshow(r"C:\Users\HariChukka\Desktop\python\saved_image",img4)
cv2.imwrite("new_image",img4)
k = cv2.waitKey(0)

if k == ord("q"):
            cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite(r"C:\Users\HariChukka\Desktop\python\saved_image",img4)
    cv2.destroyAllWindows()
