import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



pTime = 0
cTime = 0
while True:
    success, img = cap.read()
#convert img color to RBG
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

# to detect hand and show connections

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx, cy)

                if id ==0:
                    cv2.circle(img,(cx,cy), 25, (255, 8, 255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handlms, mpHands.HAND_CONNECTIONS)
    # print(results.multi_hand_landmarks)


# to display time frame rate

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN, 3, (255,8,255), 3)



    cv2.imshow('Image', img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break