import cv2
import time
import HandTrackingModule as htm
from cvzone.SerialModule import SerialObject


cap = cv2.VideoCapture(0)
arduino = SerialObject("/dev/cu.usbmodem14201",9600,1)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []


        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)


        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        if (totalFingers == 1):
            arduino.sendData([1])
        elif (totalFingers == 2):
            arduino.sendData([2])
        elif (totalFingers == 3):
            arduino.sendData([3])
        elif (totalFingers == 4):
            arduino.sendData([4])
        elif (totalFingers == 5):
            arduino.sendData([5])

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.imshow("Image", img)
    cv2.waitKey(1)