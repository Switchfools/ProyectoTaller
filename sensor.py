import RPi.GPIO as GPIO
import time
import os

os.system( '#!/bin/bash' )
os.system( 'source ~/.profile' )
os.system( 'workon cv' )

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)
nuevo_estado = "ALARMA OFF"
time.sleep(4)

while True:
    f = open("Valentina.txt","a")
    time.sleep(1)

    if GPIO.input(4) == 1:
      nuevo_estado ="ALARMA ON"
      os.system('python live.py')
      
    else:
      nuevo_estado ="ALARMA OFF"
      
    print(nuevo_estado)
    f.write(str(nuevo_estado)+'/n')
    f.close()
    time.sleep(1)
    




