class Empleado(object):
      def __init__(self,dni,nombre,edad,sexo):
          self.dni = dni
          self.nombre = nombre
          self.edad = edad
          self.sexo = sexo

      def presentarse(self):
          return f'Hola, me llamo {self.nombre}'

      
    