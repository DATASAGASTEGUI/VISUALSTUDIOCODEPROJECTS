class Alumno:
      def __init__(self,idAlumno=None,nombre=None):
          self.__idAlumno = idAlumno
          self.__nombre = nombre

      def set_idAlumno(self,idAlumno):
          self.__idAlumno = idAlumno

      def set_nombre(self,nombre):
          self.__nombre = nombre

      def get_idAlumno(self):
          return self.__idAlumno
      
      def get_nombre(self):
          return self.__nombre
      
      def __str__(self):
          return f'idAlumno={self.__idAlumno},nombre={self.__nombre}'
      
      def __del__(self):
          print('Acabas de eliminar el objeto')
      
      