# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import time
import faceRecognition as fr
import align_faces as af

cap = cv2.VideoCapture(0)
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")
mouthCascade = cv2.CascadeClassifier("cascades/haarcascade_mcs_mouth.xml")

# faces,faceID=fr.labels_for_training_data('trainingImages/')
# face_recognizer=fr.train_classifier(faces,faceID)
# face_recognizer.save('trainingData.yml')
# face_recognizer=cv2.face.LBPHFaceRecognizer_create()

i=0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# # Detect faces in the image
	# faces = faceCascade.detectMultiScale(
	# 	gray,
	# 	scaleFactor=1.3,
	# 	minNeighbors=5,
	# 	minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	# )
	faces,gray = fr.faceDetection(frame)
	# eyes = eyeCascade.detectMultiScale(
	# 	gray,
	# 	scaleFactor=1.3,
	# 	minNeighbors=5,
	# 	minSize=(30, 30)
	# 	#flags = cv2.CV_HAAR_SCALE_IMAGE
	# )
	# mouth = mouthCascade.detectMultiScale(
	# 	gray,
	# 	scaleFactor=1.3,
	# 	minNeighbors=5,
	# 	minSize=(30, 30)
	# 	#flags = cv2.CV_HAAR_SCALE_IMAGE
	# )

	print("Found {0} faces!".format(len(faces)))
	if len(faces) > 0:
		i=i+1
		if i ==10:
			j=1
			for (x, y, w, h) in faces:
				crop_img = af.faceAlign(frame)
				cv2.imwrite('cara{0}.png'.format(j),crop_img)
				j=j+1
			cv2.imwrite('foto.png',frame)
			break
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	# for (x, y, w, h) in eyes:
	# 	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	# for (x, y, w, h) in mouth:
	# 	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.imshow('frame', frame)
cv2.destroyAllWindows()