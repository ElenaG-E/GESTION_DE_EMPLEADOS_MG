class Roles:
    def __init__(self, id_rol: int, nombre: str, permisos: list):
        if not isinstance(id_rol, int) or id_rol < 0:
            raise ValueError("ID Rol debe ser un número entero positivo.")
        if not nombre:
            raise ValueError("El nombre del rol no puede estar vacío.")
        if not isinstance(permisos, list):
            raise ValueError("Los permisos deben ser una lista.")
        
        self.id_rol = id_rol
        self.nombre = nombre
        self.permisos = permisos

    def __str__(self):
        return f"ID Rol: {self.id_rol} - Nombre del Rol: {self.nombre} - Permisos: {self.permisos}"

    def agregar_permiso(self, permiso: str):
        if permiso not in self.permisos:
            self.permisos.append(permiso)

    def eliminar_permiso(self, permiso: str):
        if permiso in self.permisos:
            self.permisos.remove(permiso)