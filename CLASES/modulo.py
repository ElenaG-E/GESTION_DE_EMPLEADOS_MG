from rol import Roles

class Modulos(Roles):
    def __init__(self, id_modulo=0, nombre=' ', id_rol=0, nombre_rol=' '):
        super().__init__(id_rol, nombre_rol)  # Llama al constructor de la clase Roles
        self.id_modulo = id_modulo
        self.nombre = nombre

    def mostrar_modulo(self):
        print(f"ID Módulo: {self.id_modulo}, Nombre: {self.nombre}")
        self.mostrar_rol()  # También puedes mostrar el rol si es necesario