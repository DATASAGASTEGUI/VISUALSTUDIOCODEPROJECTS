#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from util import cabecera, cuerpo
from crud import mostrar, eliminar, buscar

alumnos_l = [{'idAlumno':'A1', 'nombre':'Luis',   'estatura':1.70,'edad':23,'casado':True},
             {'idAlumno':'A2', 'nombre':'Miguel', 'estatura':1.71,'edad':24,'casado':True},
             {'idAlumno':'A3', 'nombre':'Carmen', 'estatura':1.72,'edad':25,'casado':True},
             {'idAlumno':'A4', 'nombre':'María',  'estatura':1.73,'edad':18,'casado':False},
             {'idAlumno':'A5', 'nombre':'Carlos', 'estatura':1.74,'edad':21,'casado':False}]

def mostrar1():
    for i in range(len(alumnos_l)):
        print(alumnos_l[i]['idAlumno'])
        print(alumnos_l[i]['nombre'])
        print(alumnos_l[i]['estatura'])
        print(alumnos_l[i]['edad'])
        print(alumnos_l[i]['casado'])

 
def menu():
    while True:
        os.system("cls")
        print('MENU')
        print('----')
        print('1. MOSTRAR TODOS LOS ALUMNOS')
        print('2. BUSCAR UN ALUMNO POR SU ID')
        print('3. ELIMINAR UN ALUMNO POR SU ID')
        print('4. ACTUALIZAR NOMBRE DE UN ALUMNO')
        print('0. SALIR')

        opcion = input('\nINGRESE OPCION? ')

        if   opcion == '1':
             os.system('cls'),opcion1(),os.system('pause')
        elif opcion == '2':
             os.system('cls'),opcion2(),os.system('pause')
        elif opcion == '3':
             os.system('cls'),opcion3(),os.system('pause')
        elif opcion == '4':
             os.system('cls'),opcion4(),os.system('pause')
        elif opcion == '0':
             os.system('cls'),print('GRACIAS POR SU VISITA'),os.system('pause')
             break
        else:
            pass

def opcion1():
    print('1. MOSTRAR TODOS LOS ALUMNOS')
    print('----------------------------\n')
    mostrar(alumnos_l)
    print()

def opcion2():
    print('2. BUSCAR UN ALUMNO POR SU ID')
    print('-----------------------------\n')
    idAlumno = input('IGRESE ID ALUMNO A BUSCAR? ')
    alumno_d = buscar(idAlumno,alumnos_l)
    if alumno_d != {}:
       print(),cabecera()
       cuerpo(alumno_d)
    else:
       print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')
    print()

def opcion3():
    print('3. ELIMINAR UN ALUMNO POR SU ID')
    print('-------------------------------\n')
    idAlumno = input('INGRESE ID DEL ALUMNO A ELIMINAR? ')
    bandera = eliminar(idAlumno,alumnos_l)
    if bandera != False:
       print(),mostrar(alumnos_l)
       print(f'\nOK: ALUMNO {idAlumno} SE ELIMINO')
    else:
       print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')
    print()

def opcion4():
    print('3. ACTUALIZAR NOMBRE DE UN ALUMNO')
    print('---------------------------------\n')
    idAlumno = input('INGRESE ID DEL ALUMNO A ACTUALIZAR? ')
    alumno_d = buscar(idAlumno,alumnos_l)
    if alumno_d != {}:
       print(f'\nNOMBRE ANTIGUO {alumno_d["nombre"]}')
       nombre = input('\nINGRESE NOMBRE NUEVO? ')
       alumno_d["nombre"] = nombre
       print(), mostrar(alumnos_l)
    else:
       print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')
    print()
    
def main():
    menu()
    
if __name__ == "__main__":
   main()