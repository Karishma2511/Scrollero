import cv2 as cv
import numpy as np
import pyautogui
capture = cv.VideoCapture(0)
lower_blue= np.array([78,158,124])
upper_blue = np.array([138,255,255])
prev_y = 0
while True:
    ret,frame = capture.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv,lower_blue,upper_blue)
    contours, hierarchy =cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv.contourArea(c)
        if area > 500:
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('space')
            prev_y =y
    cv.imshow('WEBCAM',frame)
    if cv.waitKey(10) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()