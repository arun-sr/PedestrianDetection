# -*- coding: utf-8 -*-

import cv2

video_src = 'pedestrians.avi'

cap = cv2.VideoCapture(video_src)

pedestrian_cascade = cv2.CascadeClassifier('pedestrian.xml')

while True:
    ret, img = cap.read()
	
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pedestrian = pedestrian_cascade.detectMultiScale(gray,1.3,2)
    
    for(a,b,c,d) in pedestrian:
        cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,210),4)
    
    cv2.imshow('video', img)
    
    #if cv2.waitKey(33) == 27 or 0xFF == ord('q'):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
