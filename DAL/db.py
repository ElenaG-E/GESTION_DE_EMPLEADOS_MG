import mysql.connector
from _mysql_connector import errorcode

# Connect to server
def generar_conexion():
    config={
        "user": user,
        "password": password,
    }

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * FROM libro")

# Fetch one result
for filas in cur:
    print(filas)

# Close connection
cnx.close()