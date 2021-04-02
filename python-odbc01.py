#!/usr/bin/python3

# https://wiki.python.org/moin/ODBC
import pyodbc 

# driver comes from this page
# https://wiki.python.org/moin/ODBCDrivers

conn = pyodbc.connect('DRIVER={MariaDB};User=root;Password=mysecretpassword;Server=127.0.0.1;Port=3306')
cursor = conn.cursor()                                            
cursor.execute("CREATE DATABASE Demo;")                                   

cursor.execute("SHOW DATABASES;")                                      

result = cursor.fetchall()                                              

print(result)
