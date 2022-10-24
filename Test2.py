# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 03:37:50 2022

@author: Kris K
"""

import cv2

cap = cv2.VideoCapture('livepool_highlights.mp4');
fourcc = cv2.VideoWriter_fourcc(*'MP42')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (426,240))


print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)
    
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', grey)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


        
    
