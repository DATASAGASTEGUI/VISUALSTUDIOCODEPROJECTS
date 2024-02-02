#!/usr/bin/env python
# -*- coding: utf8 -*-

from alumno import Alumno

class Alumnos:
      def __init__(self,alumnos_l=[]):
          self.alumnos_l = alumnos_l

      def mostrar(self):
          Alumno.cabecera()
          for alumno in self.alumnos_l:
              alumno.cuerpo()

      def buscar(self,idAlumno):
          alumnobuscar = None #Falta de un objeto
          for alumno in self.alumnos_l:
              if alumno.idAlumno == idAlumno:
                 alumnobuscar = alumno
                 break
          return alumnobuscar
      
      def eliminar(self, idAlumno):
          bandera = False
          for i in range(len(self.alumnos_l)):
              if self.alumnos_l[i].idAlumno == idAlumno:
                 del self.alumnos_l[i]
                 bandera = True
                 break
          return bandera       
        