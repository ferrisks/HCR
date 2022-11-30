import cv2
import time
import os 
import tensorflow 
import pytesseract

clear = lambda:os.system('clear')

vid = cv2.VideoCapture(0)
found_text = False
while found_text == False:
    frame = vid.read()
    cv2.imshow('frame',frame)
