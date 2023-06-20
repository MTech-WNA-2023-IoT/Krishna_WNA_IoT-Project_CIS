#Python Program to input data to mysql database
#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="greeshma",user="user",password="PASS",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, switch , its power data
data={'topic':'t','sw1':P1, 'sw2':P2, 'sw3':P3, 'sw4':P4, 'Sensorvalue':50}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO sensordata(topic, Sensorvalue)VALUES(%(name)s,%(int);",data)
#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()
