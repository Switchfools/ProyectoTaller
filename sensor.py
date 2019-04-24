import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)
GPIO.add_event_detect(4, GPIO.RISING)  # add rising edge detection on a channel
nuevo_estado = "ALARMA OFF"
#time.sleep(4)

while True:
    f = open("Valentina.txt","a")
    time.sleep(1)

    if GPIO.event_detected(4):
      print('Button pressed')
      nuevo_estado ="ALARMA ON"
      GPIO.output(23, GPIO.HIGH)
      #os.system('python3 /home/pi/Documents/ProyectoTaller/takePic.py')
      
    else:
      nuevo_estado ="ALARMA OFF"
      GPIO.output(23, GPIO.LOW)
    print(nuevo_estado)
    f.write(str(nuevo_estado)+'/n')
    f.close()
    time.sleep(1)
    




