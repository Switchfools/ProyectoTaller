
import cv2
import time
import faceRecognition as fr

faces,faceID=fr.labels_for_training_data('trainingImages/')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save('trainingData.yml')
