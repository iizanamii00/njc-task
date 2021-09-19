  
import mysql.connector

con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='movie',
                              auth_plugin='mysql_native_password')
cur = con.cursor()

print(con)

