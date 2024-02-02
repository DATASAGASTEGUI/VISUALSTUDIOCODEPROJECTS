from empleado import Empleado

class Supervisor(Empleado):
    def __init__(self,dni,nombre,edad,sexo,rol):
        super().__init__(dni,nombre,edad,sexo)
        self.rol = rol

    def supervisar(self):
        return f'Superviso el trabajo de todos los empleados'
