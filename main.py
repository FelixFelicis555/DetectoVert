import cv2 as cv
import mediapipe as mp
capturing_image = cv.VideoCapture(0)
Hands = mp.solutions.hands
hands = Hands.Hands()
Draw = mp.solutions.drawing_utils
while True:
    success, img = capturing_image.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            Draw.draw_landmarks(img, handLms, Hands.HAND_CONNECTIONS)
    cv.imshow("Image", img)
    cv.waitKey(1)