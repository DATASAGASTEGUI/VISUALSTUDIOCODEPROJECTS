#!/usr/bin/env python
# -*- coding: utf8 -*-

import os


def ejemplo1():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    print(alumno_d)

def ejemplo2():
    idAlumno = 'A1'
    nombre = 'Luis'
    edad = 23
    estatura = 1.72
    casado = False

    alumno_d = {'idAlumno': idAlumno,
              'nombre': nombre,
              'edad': edad,
              'estatura': estatura,
              'casado': casado}
    print(alumno_d)

def ejemplo3():
    fruta_d = {('manzana','roja'):5, ('manzana','amarilla'):3, ('naranja','mesa'):7, ('naranza','zumo'):8, ('platano','manzano'):5}
    print(fruta_d)

def ejemplo4():
    fruta_d = {1:'Manzana', 2:'Platano', 3:'Naranja'}
    print(fruta_d)

def main():
    os.system("cls")
    ejemplo3()
          
if __name__ == "__main__":
   main()