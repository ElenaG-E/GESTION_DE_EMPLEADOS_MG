from empleados import Empleados as id_rut # Importa la clase Empleados sin alias

class Departamento(id_rut):
    def __init__(self, id_depto, nombre, id_rut):  # Corrige la sintaxis del constructor
        self.id_depto = id_depto
        self.nombre = nombre
        self.id_rut = id_rut 