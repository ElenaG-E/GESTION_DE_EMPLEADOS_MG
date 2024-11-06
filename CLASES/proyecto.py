from empleados import Empleados

class Proyecto(Empleados):
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_plazo):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_plazo = fecha_plazo
        self.empleados = []

    def validar_fecha(self):
        # Lógica para validar fechas
        pass

    def agregar_empleado(self, empleado: Empleados):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado al proyecto {self.nombre}")

    def mostrar_empleados(self):
        for emp in self.empleados:
            print(f'{emp.nombre} - {emp.id_rut}')
