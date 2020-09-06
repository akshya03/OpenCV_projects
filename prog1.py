import cv2
import numpy as np

img=cv2.imread("profile pic.jpg",1)
#cascade classifier obj
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#print(img)
#print(img.shape)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=15)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    
#reize to half its size
#half_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
resized_img=cv2.resize(img,(600,600))

cv2.imshow("Legend",resized_img)

cv2.waitKey(2000)
#cv2.waitKey(0)
cv2.destroyAllWindows()