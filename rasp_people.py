# -*- coding: UTF-8 -*-
#http://qiita.com/Algebra_nobu/items/a488fdf8c41277432ff3
#https://ai-coordinator.jp/opencv-object-detection
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import os
import time
 
# �J�����̋N��
camera = PiCamera()

camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_fullbody.xml)

while(True):
 
    # ����X�g���[������t���[�����擾
    ret, frame = cap.read() 
    
    #���̔F���i�l�j�̎��s
    facerect = f_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    
    #���o�����l���͂ދ�`�̍쐬
    for rect in facerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
        
        text = 'p'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,text,(rect[0],rect[1]-10),font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        
    # �\��
    cv2.imshow("Show FLAME Image", frame) 
 
    # q����������I���B
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()