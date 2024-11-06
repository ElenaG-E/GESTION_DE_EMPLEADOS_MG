from proyecto import Proyecto
from empleados import Empleado

class ProyectoEmp:
    def __init__(self, id, proyecto: Proyecto, empleado: Empleado):
        self.id = id
        self.proyecto = proyecto
        self.empleado = empleado

    def asignar_empleado_proyecto(self):
        self.proyecto.agregar_empleado(self.empleado)
        print(f"Empleado {self.empleado.nombre} asignado al proyecto {self.proyecto.nombre}")
