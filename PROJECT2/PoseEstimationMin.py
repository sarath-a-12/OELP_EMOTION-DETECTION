import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture('1.mp4')

while 1:
    success, img = cap.read()
    cv2.imshow("Image",img)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (70,50), cv2.FONT_ITALIC,)

    cv2.waitKey(1)
