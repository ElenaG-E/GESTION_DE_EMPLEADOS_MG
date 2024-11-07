from rol import Roles
from typing import List, Optional

class TipoEmpleados(Roles):
    def __init__(self, id_tipo: int, tipo: str, id_rol: int = 0, nombre_rol: str = '', permisos: Optional[List[str]] = None):
        super().__init__(id_rol, nombre_rol, permisos or [])
        if not isinstance(id_tipo, int) or id_tipo < 0:
            raise ValueError("ID Tipo debe ser un número entero positivo.")
        if not tipo:
            raise ValueError("El tipo de empleado no puede estar vacío.")

        self.id_tipo = id_tipo
        self.tipo = tipo

    def __str__(self):
        return f"ID Tipo: {self.id_tipo} - Tipo de Empleado: {self.tipo} - Permisos: {self.permisos}"

    def cambiar_tipo(self, nuevo_tipo: str):
        
        if not nuevo_tipo:
            raise ValueError("El nuevo tipo no puede estar vacío.")
        self.tipo = nuevo_tipo