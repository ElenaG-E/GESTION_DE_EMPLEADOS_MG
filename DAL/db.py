import mysql.connector
from mysql.connector import errorcode

def generar_conexion(user, password, server, consulta):
    config = {
        'user': 'root',
        'password': '',
        'host': server,
        'database': 'gestion_empleados_mg'  # Nombre de tu base de datos
    }
    try:
        print("Intentando conectar a la base de datos...")
        conexion = mysql.connector.connect(**config)
        
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            cursor = conexion.cursor()
            cursor.execute(consulta)
            resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta

            if resultados:
                print("Consulta ejecutada correctamente. Resultados:")
                for registro in resultados:
                    print(registro)
            else:
                print("La consulta no arrojó resultados.")

            cursor.close()
            print("Cursor cerrado.")
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            
        conexion.close()
        print("Conexión cerrada.")
        
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado: usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: la base de datos no existe.")
        else:
            print(f"Error de conexión: {error}")
    else:
        print("Desconexión completada.")

# Ejemplo de uso
consulta = "SELECT * FROM empleados"  # Escribe aquí la consulta que desees ejecutar
generar_conexion("tu_usuario", "tu_contraseña", "localhost", consulta)
