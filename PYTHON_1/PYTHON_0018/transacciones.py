#!/usr/bin/env python
# -*- coding: utf8 -*-

from transaccion import Transaccion

class Transacciones:
      def __init__(self,transacciones_l=[]):
          self.transacciones_l = transacciones_l

      def mostrar(self):
          Transaccion.cabecera()
          for transaccion in self.transacciones_l:
              transaccion.cuerpo()

      def buscar(self,idTransaccion):
          transaccionbuscar = None #Falta de un objeto
          for transaccion in self.transacciones_l:
              if transaccion.getIdTransaccion() == idTransaccion:
                 transaccionbuscar = transaccion
                 break
          return transaccionbuscar
      
      def eliminar(self, idTransaccion):
          bandera = False
          for i in range(len(self.transacciones_l)):
              if self.transacciones_l[i].getIdTransaccion() == idTransaccion:
                 del self.transacciones_l[i]
                 bandera = True
                 break
          return bandera 
      
      def actualizar(self, idTransaccion,ciudad):
          transaccionactualizar = None #Falta de un objeto
          for transaccion in self.transacciones_l:
              if transaccion.getIdTransaccion() == idTransaccion:
                 transaccion.setCiudad(ciudad)
                 transaccionactualizar = transaccion
                 break
          return transaccionactualizar
      
      def agregar(self,transaccion):
          bandera = True
          try:
              self.transacciones_l.append(transaccion)
          except:
              bandera = False
          return bandera
          
