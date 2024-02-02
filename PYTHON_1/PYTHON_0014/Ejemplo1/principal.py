#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from alumno import Alumno
from alumnos import Alumnos

a1 = Alumno('A1','Luis',1.70,23,True)
a2 = Alumno('A2','Miguel',1.71,24,True)
a3 = Alumno('A3','Carmen',1.72,25,True)
a4 = Alumno('A4','María',1.73,18,False)
a5 = Alumno('A5','Carlos',1.74,21,False)

alumnos_l = [a1,a2,a3,a4,a5]

# MOSTRAR
def ejemplo1():
    alumnos = Alumnos(alumnos_l)
    alumnos.mostrar()

# BUSCAR
def ejemplo2():
    alumnos = Alumnos(alumnos_l)
    idAlumno = input('INGRESE ID DEL ALUMNO A BUSCAR? ')
    alumno = alumnos.buscar(idAlumno)
    if alumno != None:
       Alumno.cabecera()
       alumno.cuerpo()
    else:
       print(f'ERROR: ALUMNO {idAlumno} NO EXISTE')

# ELIMINAR
def ejemplo3():
    alumnos = Alumnos(alumnos_l)
    idAlumno = input('INGRESE ID DEL ALUMNO A ELIMINAR? ')
    bandera = alumnos.eliminar(idAlumno)
    if bandera != False:
       print()
       alumnos.mostrar()
       print(f'\nOK: ALUMNO {idAlumno} SE ELIMINO')
    else:
       print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')

# ACTUALIZAR
def ejemplo4():
    alumnos = Alumnos(alumnos_l)
    idAlumno = input('INGRESE ID DEL ALUMNO A ACTUALIZAR? ')
    alumno = alumnos.buscar(idAlumno)
    if alumno != None:
       print(f'NOMBRE ANTIGUO {alumno.nombre}')
       nombre = input('INGRESE NOMBRE NUEVO? ')
       alumno.nombre = nombre
       alumnos.mostrar()
    else:
       print(f'ERROR: ALUMNO {idAlumno} NO EXISTE')

   
if __name__ == "__main__":
   os.system("cls")
   ejemplo4()
