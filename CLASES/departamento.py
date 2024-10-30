from empleados import Empleados  # Importa la clase Empleados sin alias 

class Departamento(Empleados):
    def __init__(self, id_depto = 0, nombre = '', id_rut = 0):  # Corrige la sintaxis del constructor
        super().__init__(id_rut)  # Llama al constructor de la clase padre
        self.id_depto = id_depto
        self.nombre = nombre
