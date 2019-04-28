import align_faces as af
import cv2
import time
import RPi.GPIO as GPIO
import os
from picamera.array import PiRGBArray
from picamera import PiCamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
cap = PiCamera()
cap.resolution = (2592 , 1944)
cap.framerate = 30
rawCapture = PiRGBArray(cap, size=(2592 , 1944))
j=1
for frame in cap.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# Capture frame-by-frame
	frame = frame.array
	cv2.imwrite('pic_al_{0}.png'.format(j),frame)
	j=j+1
	# Display the resulting frame
	cv2.imshow('frame', frame)
	cv2.waitKey(0)
    rawCapture.truncate(0)

cv2.destroyAllWindows()
