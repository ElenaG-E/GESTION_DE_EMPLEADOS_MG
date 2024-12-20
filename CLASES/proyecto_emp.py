from GESTION.CLASES.empleados import Empleados
from GESTION.CLASES.proyecto import Proyecto

class ProyectoEmp(Empleados, Proyecto):
    def __init__(self, id_proyemp, id_proyecto, id_rut):
        self.id_proyemp = id_proyemp
        self.id_proyecto = id_proyecto
        self.id_rut = id_rut

    def __str__(self):
        return f"ProyectoEmp(id_proyemp={self.id_proyemp}, id_proyecto={self.id_proyecto}, id_rut={self.id_rut})"
    
