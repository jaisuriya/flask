import mysql.connector

connection = mysql.connector
db = connection.connect(host='localhost', database='testdb',user='root', password='go')

cursor = db.cursor()
cursor.execute('CREATE DATABASE testdb')
cursor.execute('SHOW DATABASES')
for x in cursor:
    print(x)