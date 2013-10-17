#!/usr/bin/python

#Script that connects to the MySQL database and creates a table


#Import the mysql.connector library/module
import mysql.connector
from mysql.connector import errorcode

#Connect to the MySQL database, here database = databaseName, password to mysql = password
cnx = mysql.connector.connect(user='root', host='127.0.0.1', password='password', database='databaseName')

#You must create a Cursor object. It will let you execute all the query you need
cursor = cnx.cursor()

#Create a table named `tableName` with columns example `column`in the database (databaseName)
TABLES = {}
TABLES['tableName'] = ("CREATE TABLE `tableName` (`column1` INT(11) AUTO_INCREMENT, `column2` VARCHAR(255), `column3` VARCHAR(255), PRIMARY KEY (column1))")

#If the table already exists, drop it
cursor.execute("DROP TABLE IF EXISTS `tableName`")

#Execute the create table query
cursor.execute(TABLES['tableName'])


#A commit is needed to make the change in the database
cnx.commit()
#Closes the cursor
cursor.close()
#Closes the connection to the database
cnx.close()