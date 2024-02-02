from aifc import Error
import csv
from transaccion import Transaccion
import os
import stat


class Crud:

      @staticmethod
      def leerLlenarListaObjetosTransaccionDesdeArchivoCsv(nra,transacciones_l):
          try:
              with open(nra, 'r') as ficherocsv:                       
                   lectorcsv = csv.reader(ficherocsv, delimiter=';')   
                   i = 0 
                   for fila in lectorcsv:    
                       if i != 0:                         
                          idTransaccion = int(fila[0].strip())                       
                          ciudad = fila[1]                                 
                          zona = fila[2]
                          ventas = float(fila[3].strip())
                          formaPago = fila[4]
                          categoria = fila[5]
                          transaccion = Transaccion(idTransaccion,ciudad,zona,ventas,formaPago,categoria)
                          transacciones_l.append(transaccion)
                       i = i + 1
          except:
              transacciones_l = None

      @staticmethod
      def escribirVaciarListaObjetosTransaccionHaciaArchivoCsv(nra,transacciones_l):
          bandera = True
          try:
              with open(nra, "w", newline='') as ficherocsv:
                   escritorcsv = csv.writer(ficherocsv)
                   elemento = 'IDTRANSACCION;CIUDAD;ZONA;VENTAS;FORMAPAGO;CATEGORIA'
                   escritorcsv.writerow([elemento])
                   for transaccion in transacciones_l:
                       elemento = transaccion.obtenerCsv()
                       escritorcsv.writerow([elemento])
          except:
              bandera = False
          return bandera
      

      @staticmethod
      def borrarTodasFilasArchivoCsv(nra):
          bandera = True
          try:
              with open(nra, 'w', newline='') as ficherocsv:   # Abrir el archivo en modo escritura con truncado
                   escritorcsv = csv.writer(ficherocsv)        # Crear un escritor CSV
                   escritorcsv.writerow([])                    # Escribir una fila vacía para eliminar todos los datos           
          except Error:
                   bandera = False
          return bandera
