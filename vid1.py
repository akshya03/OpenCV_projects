import cv2,time
import numpy as np

video=cv2.VideoCapture(0)

"""disply only 1st frame
check,frame=video.read()

#print(check) has only the 1st frame values
#print(frame)

time.sleep(3)
cv2.imshow("Capture",frame)

cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
"""

a=1
while True:
    a+=1
    check,frame=video.read()
    #print(frame)
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture",gray)
    key=cv2.waitKey(1) #generate new frame after 1 every sec
    if key==ord('q'): #if 'q' pressed,window destroyed
        break
    
print(a) #no. of frames
video.release()
cv2.destroyAllWindows()