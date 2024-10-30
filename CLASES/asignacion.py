class Asignacion:
    def __init__(self, IDASIG, ID_DEPTO, ID_RUT):
        self.IDASIG = IDASIG  # Unique assignment ID
        self.ID_DEPTO = ID_DEPTO  # Department ID
        self.ID_RUT = ID_RUT  # Employee ID (RUT)

    def validar_asignacion(self):
        # Code to validate the assignment (e.g., check if the employee 
        # already belongs to another department)
        pass  # Placeholder for validation logic

    def asignacion(self):
        # Code to perform the assignment logic (e.g., updating database records)
        pass  # Placeholder for assignment logic
