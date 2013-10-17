#!/usr/bin/python

#Script that connects to the MySQL database and parses data from a table

#Import the mysql.connector library/module
import mysql.connector
from mysql.connector import errorcode

#Connect to the MySQL database, here database = database
cnx = mysql.connector.connect(user='root', host='127.0.0.1', password='password', database='database')

#You must create a Cursor object. It will let you execute all the query you need
cursor = cnx.cursor()

#Select data from the table sample and the column sample_id and print it
select_data = ("""SELECT sample_id FROM sample""")
cursor.execute(select_data)
for (sample_id) in cursor:
  print sample_id

#Closes the cursor
cursor.close()

#Closes the connection to the database
cnx.close()