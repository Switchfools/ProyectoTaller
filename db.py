import pymysql

connection= pymysql.connect(host='localhost',
	user='root',
	password='12345',
	db='casa')

with connection:
    
    cur = connection.cursor()
    cur.execute("INSERT INTO entradas VALUE('Federico Alvarez','11:23 23/02/2019',1);")
    cur.execute("SELECT * FROM entradas")
    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))

