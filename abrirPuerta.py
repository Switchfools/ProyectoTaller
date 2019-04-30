import pymysql
import os
import RPi.GPIO as GPIO
import time
connection= pymysql.connect(host='192.168.0.100',
                            user='rasp',
                            password='0000',
                            db='casa')

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM entradas ORDER BY fecha DESC LIMIT 1;")
        rows = cur.fetchall()
        fecha_actual=rows[0]
        fecha_actual=fecha_actual[1]
        print(fecha_actual)

while(True):
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM entradas ORDER BY fecha DESC LIMIT 1;")
        rows = cur.fetchall()
        fecha_nueva=rows[0]
        fecha_nueva=fecha_nueva[1]
        persona=rows[0]
        persona=persona[0]

    if(fecha_actual!=fecha_nueva):
        if(persona!='Desconocido'):
            print('Puerta abierta')
            GPIO.output(24, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(24, GPIO.LOW)
    
        else:
            print('Acceso no autorizado')
            GPIO.output(22, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(22, GPIO.LOW)
        fecha_actual=fecha_nueva
        os.system('./rm.sh') 
        break