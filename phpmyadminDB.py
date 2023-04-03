#Python Program to input data to mysql database
#(c) Sai Shibu
#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="IoTDataBase",user="krishna",password="KRISHNA",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, name, age and place
data={'topic':10,'data':45}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO mqttdata(topic, data)VALUES(%(topic)s,%(data)s);",data)
#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()
