import cv2
import mediapipe as mp
import time 

cap  = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils #drawing the face
faceDetection = mpFaceDetection.FaceDetection(0.75) 

pTime = 0
while 1:
    success, img = cap.read()
    img = cv2.resize(img, (960, 540)) 
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id,detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection) #drawing tool by mediapipe
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih,iw,ic = img.shape
            bbox = int(bboxC.xmin*iw), int(bboxC.ymin*ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img,bbox,(255,0,255),2)


    cTime = time.time()

    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-20), cv2.FONT_ITALIC,1,(255,0,255),2)
    cv2.imshow("Image", img)
    if(cv2.waitKey(1) == ord('q')):
        cv2.destroyAllWindows()
        break

