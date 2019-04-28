import pymysql
import os
connection= pymysql.connect(host='192.168.0.100',
                            user='rasp',
                            password='0000',
                            db='casa')

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
    
        else:
            print('Acceso no autorizado')
        fecha_actual=fecha_nueva
        os.system('.~/home/pi/Documents/ProyectoTaller/rm.sh') 
        break
