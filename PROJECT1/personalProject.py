import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
pTime = 0 
cTime = 0 #previous and current times for frames
detector = htm.HandDetector()
while 1:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_DUPLEX,3,(255,0,255), 3)
    # printing on the image, string value of the fps, position, font to be used, scale??, colour of the text, thickness
    cv2.imshow("Image", img)
    if(cv2.waitKey(1) == ord('q')):
        cv2.destroyAllWindows()
        break
