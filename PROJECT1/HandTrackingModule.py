#Module for tracking hand and doing other stuff

import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self, mode = False, maxHands = 2, detectionConf = 0.5, trackConf = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionConf
        self.trackConf = trackConf
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,1,self.detectionConf,self.trackConf) #class instance - idk use default values
        self.mpDraw = mp.solutions.drawing_utils #drawing lines between each points in the hand


    def findHands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to rgb for hands to use
        self.result = self.hands.process(imgRGB) # call the object on the obtained RGB

        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks: # different hands 
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) #drawing the points and the connections between them 
        return img
    
    def findPosition(self,img,handNo=0,draw=True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark): #getting information within each of the hands - lm gives x and y co-ordinates, id is index number
                      #values are decimals - we need them in pixels - multiply it with widht and height to get the pixel values
                    h,w,c = img.shape #height width channel
                    cx,cy = int(lm.x*w), int(lm.y*h) #cx and cy, yeayyy
                    lmList.append([id,cx,cy]) # now you get it in terms of pixels
                    if draw:
                        cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED) #radius and color for the first id
                      #we will put them on a list and then do other stuff
        return lmList

# cap = cv2.VideoCapture(0)
#
# mpHands = mp.solutions.hands
# hands = mpHands.Hands() #class instance - idk use default values
# mpDraw = mp.solutions.drawing_utils #drawing lines between each points in the hand
#
# pTime = 0 
# cTime = 0 #previous and current times for frames
#
# while 1:
#     success, img = cap.read()
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to rgb for hands to use
#     result = hands.process(imgRGB) # call the object on the obtained RGB
#     ''' 
#     we will be processing this received results for further uses 
#     '''
#     #check for multiple hands and extract them one by one
#     # print(result.multi_hand_landmarks) #temp check
#
#     if result.multi_hand_landmarks:
#         for handLms in result.multi_hand_landmarks: # different hands 
#             for id,lm in enumerate(handLms.landmark): #getting information within each of the hands - lm gives x and y co-ordinates, id is index number
#                 # print(id,lm) # each id has corresponding land mark - x y and z ...co ordinates
#                 #values are decimals - we need them in pixels - multiply it with widht and height to get the pixel values
#                 h,w,c = img.shape #height width channel
#                 cx,cy = int(lm.x*w), int(lm.y*h) #cx and cy, yeayyy
#                 print(id,cx,cy) # now you get it in terms of pixels
#                 if id == 4:
#                     cv2.circle(img, (cx,cy), 14, (255,0,255), cv2.FILLED) #radius and color for the first id
#                 #we will put them on a list and then do other stuff
#                     
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #drawing the points and the connections between them 
#
#     cTime = time.time()
#     fps = 1/(cTime - pTime)
#     pTime = cTime
#
#     cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_DUPLEX,3,(255,0,255), 3)
#     # printing on the image, string value of the fps, position, font to be used, scale??, colour of the text, thickness
#
#
#
#
#
#     cv2.imshow("Image", img)
#     if(cv2.waitKey(1) == ord('q')):
#         cv2.destroyAllWindows()
#         break
#
#

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0 
    cTime = 0 #previous and current times for frames
    detector = HandDetector()
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









if __name__ == "__main__":
    main()
