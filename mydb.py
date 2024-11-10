# install mysql on computer 
# pip install mysql
#pip install mysql-connector
# pip install mysql-connector-python
import mysql.connector

database=mysql.connector.connect(
     host = 'localhost',
     user='root',
     passwd='Password123',
)

# prepare cursor obj
cursorobject=database.cursor()

# crate database 
cursorobject.execute("CREATE DATABASE ELDERCO")

print(" DB DONE ")