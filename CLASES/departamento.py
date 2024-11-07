from empleados import Empleados

class Departamento(Empleados):
    def __init__(self, id_depto=0, nombre='', id_rut=0, **kwargs):
        super().__init__(id_rut, **kwargs)
        self.id_depto = id_depto
        self.nombre = nombre
        
    def __str__(self):
        return f"Departamento {self.nombre} - ID Departamento: {self.id_depto}"
