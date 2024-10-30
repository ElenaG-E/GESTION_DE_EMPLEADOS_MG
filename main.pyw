from DAL.db import generar_conexion
from DAL.consultas_sql import 
from DAL.db_autor import
print("""
    Seleccione su Opción:
    1.- Consultar Libros
    2.- Consultar Editoriales
    3.- Consultar Autores
    """)
accion = input("Ingresa su opción: ")

if accion == '1':
    generar_conexion('root','','localhost','biblioteca', consulta_1())
elif accion == '2':
    generar_conexion('root','','localhost','biblioteca', consulta_1())
elif accion == '3':
    pass
else:
    print("Saliendo del sistema...")

# Para hace una instancia de clase
# objeto = MiClase()


#Esto es un crud. (CRear) Este es el crud para la clase empleados.
class SistemGestionEmpleados: 
    def __init__(self): 
        self.empleados = {} 
 
    def añadir_empleado(self, id_emp, nombre, posicion): 
        if id_emp in self.employees: 
            print("ID del empleado existe.") 
        else: 
            self.empleados[id_emp] = Empleados(id_emp, nombre, posicion) 
            print("Empleado agregado exitosamente") 
 
    def ver_empleados(self): #VER
        if not self.empleados: 
            print("No se encuentra empleado.") 
            return 
        for emp in self.empleados(): 
            print(emp) 
 
    def eliminar_empleado(self, id_emp): #ELIMINAR
        if emp_id in self.empleados: 
            del self.empleados[id_emp] 
            print("Employee removed successfully.") 
        else: 
            print("Employee ID not found.") 
 
    def menu(self): 
        while True: 
            print("\nSistema de Gestión de Empleados") 
            print("1. Añadir Empleados") 
            print("2. Ver Empleados") 
            print("3. Eliminar Empleados") 
            print("4. Salir") 
            opcion = input("Elegir una opcion: ") 
 
            if opcion == "1": 
                id_emp = input("Ingresar id_emp: ") 
                nombre = input("Ingresar nombre del Empleado: ") 
                posicion = input("Ingresar posicion del Empleado: ") 
                self.añadir_empleado(id_emp, nombre, posicion) 
            elif opcion == "2": 
                self.ver_empleados() 
            elif opcion == "3": 
                emp_id = input("Ingresar id del empleado para eliminar: ") 
                self.eliminar_empleado(emp_id) 
            elif opcion == "4": 
                print("Borrar del Sistema.") 
                break 
            else: 
                print("Opcion invalida. Intente nuevamente") 
 
if __name__ == "__main__": 
    sistema= SistemGestionEmpleados() 
    sistema.menu() 