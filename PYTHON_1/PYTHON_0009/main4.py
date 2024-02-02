#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    alumno_d = {'idAlumno': 'A1',
              'nombre': 'Luis',
              'edad': 23,
              'estatura': 1.72,
              'casado': False}
    alumno_d['ciudad'] = 'Madrid'
    print(alumno_d)

def ejemplo2():
    meses_l = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    meses_d = {}
    for clave,valor in zip (meses_l,range(0,12,1)):
        meses_d[clave] = valor 
    print(meses_d)  

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()