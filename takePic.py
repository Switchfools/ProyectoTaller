import align_faces as af
import cv2
import time
import subprocess
import faceRecognition as fr
import pymysql
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera

connection= pymysql.connect(host='192.168.0.100',
                            user='rasp',
                            password='0000',
                            db='casa')
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
cap = PiCamera()
cap.resolution = (640, 480)
cap.framerate = 32
rawCapture = PiRGBArray(cap, size=(640, 480))
j=1
GPIO.output(23, GPIO.HIGH)
time.sleep(3)
for frame in cap.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Capture frame-by-frame
    frame = frame.array
    faces,gray = fr.faceDetection(frame)
    # cv2.imwrite('pic2_{0}.png'.format(j),frame)
    #al_frame=af.faceAlign(frame)
    if len(faces) > 0:
        cv2.imwrite('FotosEntrada/foto5.png'.format(j),frame)
        GPIO.output(23, GPIO.LOW)
        break
    j=j+1
    # Display the resulting frame
    #cv2.imshow('frame', frame)
    #cv2.imshow('alignedframe', al_frame)
    rawCapture.truncate(0)

# When everything done, release the capture
#cv2.imshow('frame', frame)
cv2.destroyAllWindows()
subprocess.call(['./upload.sh'])

with connection:
    cur = connection.cursor()
    cur.execute("SELECT * FROM imagenes ORDER BY id DESC LIMIT 1;")
    rows = cur.fetchall()
    id_actual=rows[0]
    for row in rows:
        print("{0}".format(row[0]))
    id_nuevo=int(id_actual[0])+1
    cur.execute("INSERT INTO imagenes VALUES("+str(id_nuevo)+");")
