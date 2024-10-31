import cv2
from pprint import pprint
import sys
import numpy
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    print(ret)
    print(list(frame))
    for el in frame:
        for i in el:
            print(i,end='')
    cv2.imshow('camera', frame)
    cv2.waitKey(1)
    break