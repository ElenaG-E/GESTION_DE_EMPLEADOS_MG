import re
class Empleados:
    def __init__(self, id_rut: str, nombre: str, apepat: str, apemat: str, fecha_nac, fecha_contrato, sueldo, correo: str, telefono: str, direccion, id_rol, id_tipo: str, nom_usuario, password):
        self.id_rut = id_rut
        self.nombre = nombre
        self.apepat = apepat
        self.apemat = apemat
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
    
    def validar_Datos(self):
        if len(self.id_rut) < 3 or 
