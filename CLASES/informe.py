from empleados import Empleado

class Informe:
    def __init__(self, id_inf, empleado: Empleado, fecha_hora, reporte):
        self.id_inf = id_inf
        self.empleado = empleado
        self.fecha_hora = fecha_hora
        self.reporte = reporte

    def generar_informe(self):
        # Lógica para generar informe
        print(f"Informe generado para el empleado {self.empleado.nombre}")

    def exportar_informe(self, formato):
        # Lógica para exportar informe en el formato especificado
        print(f"Informe exportado en formato {formato}")

