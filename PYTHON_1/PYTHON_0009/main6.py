#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    
    del alumno_d['casado']
    print(alumno_d)

def ejemplo2():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    alumno_d.clear()
    print(alumno_d)

def ejemplo3():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    for k in list(alumno_d.keys()):
        v = alumno_d.pop(k)
        print(v)
    print(alumno_d)

def ejemplo4():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    for k in list(alumno_d.keys()):
        del alumno_d[k]
    print(alumno_d)

def main():
    os.system("cls")
    ejemplo4()
          
if __name__ == "__main__":
   main()