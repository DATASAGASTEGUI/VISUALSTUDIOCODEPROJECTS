#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import csv
from transaccion import Transaccion

def ejemplo1():
    ficherocsv = open('PYTHON_0018\\transaccion.csv')
    while True:
          lineacorrecta = ficherocsv.readline()
          if lineacorrecta:
             print(lineacorrecta,end='')
          else:
             break
    ficherocsv.close

def ejemplo2():
    nra = 'PYTHON_0018\\transaccion.csv'
    with open(nra, 'r') as ficherocsv:                        # Abrir archivo en modo lectura
         lectorcsv = csv.reader(ficherocsv, delimiter=';')    # Crear un objeto lector de csv
         #print(list(lectorcsv))
         for fila in lectorcsv:                               # Iterar sobre las filas del archivo
             idTransaccion = fila[0]                          # Cada fila es una lista de valores separados por comas
             ciudad = fila[1]                                 # Accede a los valores por su índice
             zona = fila[2]
             ventas = fila[3]
             formaPago = fila[4]
             categoria = fila[5]
             print(F'{idTransaccion},{ciudad},{zona},{ventas},{formaPago},{categoria}')                            # Hacer algo con los valores

def ejemplo3():
    nra = 'PYTHON_0018\\transaccion.csv'
    #transaccion = None
    with open(nra, 'r') as ficherocsv:                       
         lectorcsv = csv.reader(ficherocsv, delimiter=';')   
         i = 0 
         Transaccion.cabecera()
         print('Tamaño: ',len(lectorcsv))
         for fila in lectorcsv:    
             if i != 0:                         
                idTransaccion = fila[0]                         
                ciudad = fila[1]                                 
                zona = fila[2]
                ventas = float(fila[3].strip())
                formaPago = fila[4]
                categoria = fila[5]
                transaccion = Transaccion(idTransaccion,ciudad,zona,ventas,formaPago,categoria)
                transaccion.cuerpo()
             i = i + 1  

def ejemplo4():
    nra = 'PYTHON_0018\\probando.csv'
    try:
        with open(nra, 'w', newline='') as ficherocsv:   # Abrir el archivo en modo escritura con truncado
             escritorcsv = csv.writer(ficherocsv)        # Crear un escritor CSV
             escritorcsv.writerow([])                    # Escribir una fila vacía para eliminar todos los datos           
             print('OK')
    except:
             print('ERROR')
 
def main():
    os.system("cls")
    ejemplo4()
          
if __name__ == "__main__":
   main()