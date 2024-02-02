#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from alumno import Alumno

def ejemplo1():
    alumno = Alumno('A1','Luis')
    print('IdAlumno: ',alumno.get_idAlumno())
    print('Nombre  : ',alumno.get_nombre())

def ejemplo2():
    alumno = Alumno('A1','Luis')
    print(alumno)

def ejemplo3():
    alumno = Alumno('A1','Luis')
    alumno.set_nombre('Arturo')
    alumno.set_idAlumno('A2')
    print(alumno)

def ejemplo4():
    alumno = Alumno()
    alumno.set_nombre('Luis')
    alumno.set_idAlumno('A1')
    print(alumno)

def ejemplo5():
    alumno = Alumno('A3','Miguel')
    print(alumno)
    del(alumno)
    print(alumno) # Error porque ya no tiene la referencia a un objeto alumno

def ejemplo6():
    alumno = Alumno('A3','Miguel')
    print(alumno)
    print(alumno)
    
if __name__ == "__main__":
   os.system("cls")
   ejemplo6()

'''
Es una buena práctica eliminar los objetos que ya no se usen con el destructor del
'''