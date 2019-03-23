import cv2
import time
import faceRecognition as fr
import datetime
import pymysql
import numpy as np

connection= pymysql.connect(host='192.168.0.100',
	user='cliente',
	password='0000',
	db='casa')

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')

name={0:"Federico Alvarez",1:"Valentina Parra",2:"Felipe Noguera",3:"Nicolas Vergara"}#creating dictionary containing names for each label

pic_color = cv2.imread('cara1.png')
pic_gray = cv2.cvtColor(pic_color,cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
pic = clahe.apply(pic_gray)
#compute a Laplacian filter to find the borders.
Borders=cv2.Laplacian(pic, ddepth=3)
label,confidence=face_recognizer.predict(Borders)#predicting the label of given image
print("confidence:",confidence)
print("label:",label)
predicted_name=name[label]
if(confidence<40):#If confidence less than 60 then don't print predicted face text on screen
	print(predicted_name+ ' ' + datetime.datetime.now().isoformat(timespec='minutes'))
	cv2.imshow('winname', pic_color)
	with connection:
		cur = connection.cursor()
		# cur.execute("INSERT INTO entradas VALUE("+predicted_name+","+datetime.datetime.now().isoformat(timespec='minutes')+","+str(label)+");")
		cur.execute("INSERT INTO entradas VALUE('"+predicted_name+"','"+datetime.datetime.now().isoformat(timespec='minutes')+"',"+str(label)+");")
		cur.execute("SELECT * FROM entradas")
		rows = cur.fetchall()

		for row in rows:
			print("{0} {1} {2}".format(row[0], row[1], row[2]))
	cv2.waitKey(0)#Waits indefinitely until a key is pressed
    #cv2.destroyAllWindows
else:
	print("No esta autorizado")
