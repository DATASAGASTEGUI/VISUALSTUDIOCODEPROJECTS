#!/usr/bin/env python
# -*- coding: utf8 -*-

class Alumno:
      def __init__(self,idAlumno,nombre,estatura,edad,casado):
          self.idAlumno = idAlumno
          self.nombre = nombre
          self.estatura = estatura
          self.edad = edad
          self.casado = casado

      def __str__(self):
          #return '{}  {}  {}  {}  {}'.format(self.idAlumno,self.nombre,self.estatura,self.edad,self.casado)
          #return f'{self.idAlumno}  {self.nombre}  {self.estatura}   {self.edad}  {self.casado}'
          return self.idAlumno + '  ' + self.nombre + '  ' + str(self.estatura) + '  ' + str(self.edad) + '  ' + str(self.casado)
      
      @staticmethod
      def cabecera():
          print('%-8s  %-10s  %8s  %4s  %-6s' % ('IDALUMNO','NOMBRE','ESTATURA','EDAD','CASADO'))
          print('%-8s  %-10s  %8s  %4s  %-6s' % (Alumno.pintarguiones('IDALUMNO'),Alumno.pintarguiones('NOMBRE'),Alumno.pintarguiones('ESTATURA'),Alumno.pintarguiones('EDAD'),Alumno.pintarguiones('CASADO')))

      def cuerpo(self):
          print('%-8s  %-10s  %8.2f  %4d  %-6s' % (self.idAlumno,self.nombre,self.estatura,self.edad,self.casado))
  
      @staticmethod
      def pintarguiones(cadena):
          s = ''
          for i in range(len(cadena)):
              s = s + '-'
          return s