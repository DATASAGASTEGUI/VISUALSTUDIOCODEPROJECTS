#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    claves_l = list(alumno_d.keys())
    print(list(claves_l))

def ejemplo2():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    valores_l = list(alumno_d.values())
    print(list(valores_l))

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()