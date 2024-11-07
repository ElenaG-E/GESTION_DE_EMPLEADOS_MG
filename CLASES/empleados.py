from cryptography.fernet import Fernet
import re
from tipo_empleado import TipoEmpleados

class Empleados(TipoEmpleados):
    # Generar una clave de cifrado única para cada instancia
    def __init__(self, id_rut=0, nombre='', fecha_nac='', fecha_contrato='', sueldo=0, correo='', telefono=0, direccion='', id_rol=0, id_tipo=0, nom_usuario='', password='', habilitado=''):
        super().__init__(id_tipo, "", [])
        self.id_rut = id_rut
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.fecha_contrato = fecha_contrato
        self.sueldo = sueldo
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.id_rol = id_rol
        self.nom_usuario = nom_usuario
        self.clave = Fernet.generate_key()  # Generar clave aquí
        self.cipher_suite = Fernet(self.clave)
        self.password = self.encriptar_clave(password)
        self.habilitado = habilitado
        self.validar_datos()  # Validar datos al crear el empleado

    def encriptar_clave(self, password):
        """Encripta la contraseña proporcionada."""
        if password:
            return self.cipher_suite.encrypt(password.encode())
        return ""

    def desencriptar_clave(self):
        """Desencripta la contraseña almacenada."""
        if self.password:
            try:
                return self.cipher_suite.decrypt(self.password).decode()
            except Exception as e:
                print(f"Error al desencriptar la contraseña: {e}")
                return ""
        return ""

    def validar_datos(self):
        """Valida el correo y el teléfono del empleado."""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            raise ValueError("Correo no válido.")
        if not re.match(r"\d{9,15}", str(self.telefono)):
            raise ValueError("Teléfono no válido.")

    def __str__(self):
        """Representación en cadena del objeto Empleados."""
        return f"Empleado: {self.nombre} - Correo: {self.correo} - Fecha Nac: {self.fecha_nac} - Teléfono: {self.telefono}"