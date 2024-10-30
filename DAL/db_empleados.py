from datetime import datetime
import mysql.connector
from mysql.connector import errorcode


def generar_conexion(servidor, usuario, contrasena, base_datos):
    config = {
        'host': servidor,
        'user': usuario,
        'password': contrasena,
        'database': base_datos
    }
    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa.")
        return conexion
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado: usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: la base de datos no existe.")
        else:
            print(err)
        return None

def listado_empleados(servidor, usuario, contrasena, base_datos):
    conexion = generar_conexion(servidor, usuario, contrasena, base_datos)
    
    if conexion is not None:  # Verifica que la conexión se estableció correctamente
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                SELECT 
                    e.ID_RUT,
                    e.SUELDO,
                    e.NOM_USUARIO,
                    t.TIPO,
                    r.ID_ROL,
                    r.PERMISOS
                FROM empleados e
                JOIN tipo_empleado t ON e.ID_TIPO = t.ID_TIPO
                JOIN roles r ON e.ID_ROL = r.ID_ROL;
            """)
            
            print(f"ID_RUT    -    SUELDO   -    NOM_USUARIO    -    TIPO   -    ID_ROL  -   PERMISOS")
            print("=============================================================================================")
            for (id_rut, sueldo, nom_usuario, tipo, id_rol, permisos) in cursor:
                print(f"{id_rut} - {sueldo} - {nom_usuario} - {tipo} - {id_rol} - {permisos}")
                print("---------------------------------------------------------------------------------------------")
        except mysql.connector.Error as err:
            print("Error en la consulta:", err)
        finally:
            cursor.close()
            conexion.close()  # Asegúrate de cerrar la conexión siempre
            print("Conexión cerrada.")
    else:
        print("No se pudo establecer la conexión a la base de datos.")

# Ejemplo de uso



listado_empleados("localhost", "root", "", "gestion_empleados_mg")

def obtener_autor_seudonimo(servidor, usuario, contrasena, base_datos, seudonimo):
    conexion = generar_conexion(servidor, usuario, contrasena, base_datos)
    cursor = conexion.cursor()
    cursor.execute(f"""
        SELECT 
            A.nombre_autor,
            A.seudonimo_autor,
            P.gentilicio_pais,
            A.fecha_nac,
            A.fecha_def
        FROM autor A
        JOIN paises P ON A.codigo_pais = P.codigo_pais
        WHERE A.seudonimo_autor LIKE '%{seudonimo}%'
        """)
    
    for (nombre_autor,seudonimo_autor,gentilicio_pais,fecha_nac,fecha_def) in cursor:
        print(f"""
            Nombre: {nombre_autor}
            Seudónimo: {seudonimo_autor}
            Nacionalidad: {gentilicio_pais}
            Fecha de Nacimiento: {datetime.strftime(fecha_nac, '%d/%m/%Y')}
            Fecha de Defunción: {datetime.strftime(fecha_def, '%d/%m/%Y')}
        """)
                    
    cursor.close()
    conexion.close()

def crear_autor(user,password,server,database,autor):
    conexion = generar_conexion(user,password,server,database)
    cursor = conexion.cursor()
    cursor.execute(f"""
        INSERT INTO autor (nombre_autor,seudonimo_autor,codigo_pais) VALUES (
            'Federico De las Mercedew',
            'Quico',
            'AFG'
        )
        """)