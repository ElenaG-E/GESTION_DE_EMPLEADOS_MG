import mysql.connector
from mysql.connector import errorcode

try:
        cnx= mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="",
            database="gestion"
        )
        
        cursor = cnx.cursor()
        #cursor.execute("SHOW DATABASES")
        cursor.execute("SELECT * FROM usuarios;")
        for base in cursor:
            print(base)
        #cnx.closed

except mysql.connector.Error:
      print("Ocurrió un error al conectar la base de datos")