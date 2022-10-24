# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 03:29:58 2022

@author: Kris K
"""

import cv2

img = cv2.imread('download.jpg', -1)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF



if k == 27 :
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('download_copy.jpg', img)
    cv2.destroyAllWindows()
    