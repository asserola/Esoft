import cv2
import numpy as np
import ModuleHandTracking as htm
import time
import autopy

wCam, hCam = 640, 480
wScr, hScr = autopy.screen.size()
frameR = 100
smooth = 7
pTime = 0
plocX, plcoY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

detetor = htm.handDetector(maxHands=1)

while True:
    #  1. Find hand Landmark

    success, img = cap.read()
    img = detetor.findHands(img)
    lmList, bbox = detetor.findPosition(img)

    # print(lmList)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # print(x1, y1, x2, y2)

        fingers = detetor.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smooth
            clocY = plcoY + (y3 - plcoY) / smooth

            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 9, (255, 0, 255), cv2.FILLED)
            plocX, plcoY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detetor.findDistance(8, 12, img)

            print(length)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[3]), 9, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
