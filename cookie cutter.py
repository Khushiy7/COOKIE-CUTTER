import cv2 as cv
import os
from cvzone import HandTrackingModule, overlayPNG
import numpy as np

folderpath='C:\Users\KIIT\Desktop\Code\frames\img1.jpeg'
mylist = os.listdir(folderpath)
graphic=[cv.imread(f'{folderpath}/{imPath}') for imPath in mylist]
intro =graphic[0]
kill =graphic[1]
winner =graphic[2]
cam = cv.VedioCapture(0)
detector =HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)
#sets the minimum confidence threshold for the detection
cv.imshow('cookie cutter',cv.resize(intro,(0,0),fx=0.69,fy=0.69))

sqr_img = cv.imread('C:\Users\KIIT\Desktop\Code\frames\img2.png')
mlsa =  cv.imread('C:\Users\KIIT\Desktop\Code\img\mlsa.png')
while True:
    cv.imshow('cookie cutter',cv.resize(intro,(0,0),fx=0.69,fy=0.69))
    if cv.waitkey(1) & 0xFF==ord('q'):
        break
    TIMER_MAX = 45
    TIMER = TIMER_MAX
    maxMove = 200
    font = cv.FONT_HERSHEY_SIMPLEX
    cap = cv.VedioCapture(0)
    frameheight = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    framewidth = cap.get(cv.CAP_PROP_FRAME_WIDTH)
 
gameOver = False
NotWon =True

capture = cv.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=2, detectionCon=0.77)
## max hands for no of hands we need to detect
## detectionCon for percentage of error we can allow. Range is from 0 to 1

while True:
    isTrue, frame = capture.read()
    hands, img = detector.findHands(frame, flipType=True)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

    cv.imshow('Video', frame)


    if(cv.waitKey(20) & 0xFF==ord('q')):
        break

capture.release()
cv.destroyAllWindows() 
