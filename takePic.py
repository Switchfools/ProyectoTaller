import align_faces as af
import cv2
import time
import subprocess
import faceRecognition as fr
import pymysql
from picamera.array import PiRGBArray
from picamera import PiCamera

connection= pymysql.connect(host='192.168.0.100',
                            user='raspberry',
                            password='0000',
                            db='casa')
cap = PiCamera()
cap.resolution = (640, 480)
cap.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
j=1
time.sleep(3)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# Capture frame-by-frame
    frame = frame.array
    faces,gray = fr.faceDetection(frame)
    # cv2.imwrite('pic2_{0}.png'.format(j),frame)
    #al_frame=af.faceAlign(frame)
    if len(faces) > 0:
        cv2.imwrite('FotosEntrada/foto5.png'.format(j),frame)
        break
    j=j+1
    # Display the resulting frame
    #cv2.imshow('frame', frame)
    #cv2.imshow('alignedframe', al_frame)
    rawCapture.truncate(0)

# When everything done, release the capture
cap.release()
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
