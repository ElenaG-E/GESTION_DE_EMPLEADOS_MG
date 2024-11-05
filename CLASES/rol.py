class Roles:
    def __init__(self, id_rol, nombre, permisos):
        self.id_rol = id_rol
        self.nombre = nombre 
        self.permisos = permisos

    def __str__(self):
        return f"ID Rol: {self.id_rol} - Nombre del Rol: {self.nombre} - Permisos: {self.permisos}"