from departamento import Departamento
from empleados import Empleado

class Asignacion:
    def __init__(self, id_asig=0, id_depto=0, id_rut=0):
        self.id_asig = id_asig
        self.id_depto = id_depto
        self.id_rut = id_rut

    def validar_asignacion(self, db):
        """Validates an assignment.

        Args:
            db: A database session.

        Raises:
            ValueError: If the employee or department doesn't exist or if the employee is already assigned to another department.
        """

        # Check if the employee and department exist
        empleado = db.query(Empleado).get(self.id_rut)
        departamento = db.query(Departamento).get(self.id_depto)
        if not empleado or not departamento:
            raise ValueError("Empleado o departamento no encontrado.")

        # Check for concurrent assignments
        existing_assignments = db.query(Asignacion).filter_by(id_rut=self.id_rut).filter(Asignacion.id_asig != self.id_asig).all()
        if existing_assignments:
            raise ValueError("El empleado ya está asignado a otro departamento.")

    def asignar(self, db):
        """Assigns an employee to a department.

        Args:
            db: A database session.

        Raises:
            Exception: If an error occurs during the assignment process.
        """

        try:
            self.validar_asignacion(db)

            # Create a new assignment record
            new_asignacion = Asignacion(
                id_asig=self.id_asig,
                id_depto=self.id_depto,
                id_rut=self.id_rut
            )

            db.session.add(new_asignacion)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception("Error al asignar empleado: {}".format(str(e)))