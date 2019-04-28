import align_faces as af
import cv2
import time

cap = cv2.VideoCapture(0)
j=1
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	cv2.imwrite('pic_al_{0}.png'.format(j),al_frame)
	j=j+1
	# Display the resulting frame
	cv2.imshow('frame', frame)
	cv2.imshow('alignedframe', al_frame)
	cv2.waitKey(0) 