from cryptography.fernet import Fernet
import re
from prettytable import prettytable
from tipo_empleado import TipoEmpleados #seudonimo  #Preguntar al profe porque se ve en verde

table = prettytable.PrettyTable()

class Empleados(TipoEmpleados):
    clave = Fernet.generate_key()
    cipher_suite = Fernet(clave)

    def __init__(self, id_rut = 0, nombre = '', fecha_nac = '', fecha_contrato = '', sueldo = 0, correo = '', telefono = 0, direccion = '', id_rol = 0, id_tipo = 0, nom_usuario = '', password = ''):
        self.id_rut = id_rut
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.fecha_contrato = fecha_contrato
        self.sueldo = sueldo
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.id_rol = id_rol
        self.id_tipo = id_tipo
        self.nom_usuario = nom_usuario
        self.password = self.encriptar_clave(password)
    
    def encriptar_clave(self, password):
        if password:
            return self.cipher_suite.encrypt(password.encode())
        return ""
    
    def desencriptar_clave(self):
        if self.password:
            return self.cipher_suite.decrypt(self.password).decode()
        return ""

    def validar_datos(self):
        # Valida datos básicos sin solicitar entrada
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            raise ValueError("Correo no válido.")
        if not re.match(r"\d{9,15}", self.telefono):
            raise ValueError("Teléfono no válido.")

    def __str__(self):
        return f"Empleado: {self.nombre} - Correo: {self.correo} - Fecha Nac: {self.fecha_nac} - Teléfono: {self.telefono}"
