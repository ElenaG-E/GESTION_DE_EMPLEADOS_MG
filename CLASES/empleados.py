from cryptography.fernet import Fernet
import re

class Empleados:

    clave = Fernet.generate_key()
    cipher_suite = Fernet(clave)

    def __init__(self, id_rut, nombre, fecha_nac, fecha_contrato, sueldo, correo, telefono, direccion, id_rol, id_tipo, nom_usuario, password):
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
        self.password = password
    
    def Encriptar_clave(self):
        if self.password:
            return self.cipher_suite.decrypt(self.password.encode().decode())
        return ""
        
    def Validar_datos(self):
        self.nombre = input("Ingresa el nombre del empleado: ")
        self.correo = input("Ingresa el correo: ")
        self.fecha_nac = input("Ingresa fecha_nacimiento: ")
        self.telefono= input("Ingresa el telefono: ")
    
    def __str__(self):
        return f"Empleado: {self.nombre} - Correo: {self.correo} - Fecha_Nac: {self.fecha_nac} - Telefono: {self.telefono}"

    def Encriptar_clave(self):
        if self.password:
            return self.cipher_suite.decrypt(self.password.encode().decode())
        return ""
