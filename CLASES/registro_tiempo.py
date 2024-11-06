from empleados import Empleado

class RegistroTiempo:
    def __init__(self, id_reg_tiem, empleado: Empleado, fecha, cant_horas, descripcion, hora_extra, observacion):
        self.id_reg_tiem = id_reg_tiem
        self.empleado = empleado
        self.fecha = fecha
        self.cant_horas = cant_horas
        self.descripcion = descripcion
        self.hora_extra = hora_extra
        self.observacion = observacion

    def validacion_cant_horas(self):
        # Lógica para validar cantidad de horas
        if self.cant_horas < 0:
            raise ValueError("Cantidad de horas no puede ser negativa")
        print(f"Horas trabajadas: {self.cant_horas}")
