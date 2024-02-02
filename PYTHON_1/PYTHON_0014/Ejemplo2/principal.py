#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, re

alumnos_l = [{'idAlumno':'A1', 'nombre':'Luis',    'estatura':1.70,'edad':23,'casado':True},
             {'idAlumno':'A2', 'nombre':'Miguel',  'estatura':1.71,'edad':24,'casado':False},
             {'idAlumno':'A3', 'nombre':'Carmen',  'estatura':1.72,'edad':25,'casado':True},
             {'idAlumno':'A4', 'nombre':'María',   'estatura':1.73,'edad':18,'casado':False},
             {'idAlumno':'A5', 'nombre':'Carlos',  'estatura':1.74,'edad':21,'casado':False},
             {'idAlumno':'A6', 'nombre':'Arturo',  'estatura':1.71,'edad':24,'casado':False},
             {'idAlumno':'A7', 'nombre':'Gerson',  'estatura':1.70,'edad':21,'casado':False},
             {'idAlumno':'A8', 'nombre':'Asier',   'estatura':1.72,'edad':23,'casado':True},
             {'idAlumno':'A9', 'nombre':'Vanessa', 'estatura':1.73,'edad':21,'casado':False},
             {'idAlumno':'A10','nombre':'Melissa', 'estatura':1.74,'edad':22,'casado':True}]

def mostrar1():
    for i in range(len(alumnos_l)):
        print(alumnos_l[i]['idAlumno'])
        print(alumnos_l[i]['nombre'])
        print(alumnos_l[i]['estatura'])
        print(alumnos_l[i]['edad'])
        print(alumnos_l[i]['casado'])

def mostrar():
    cabecera()
    for alumno_d in alumnos_l:
        cuerpo(alumno_d)

def buscar(idAlumno):
    alumnobuscar_d = {}
    for alumno_d in alumnos_l:
        if alumno_d['idAlumno'] == idAlumno:
           alumnobuscar_d = alumno_d
           break
    return alumnobuscar_d

def eliminar(idAlumno):
    bandera = False
    for indice,alumno_d in enumerate(alumnos_l):
        if alumno_d['idAlumno'] == idAlumno:
           del alumnos_l[indice]
           bandera = True
           break
    return bandera   
           
def cabecera():
    print('%-8s  %-10s  %8s  %4s  %-6s' % ('IDALUMNO','NOMBRE','ESTATURA','EDAD','CASADO'))
    print('%-8s  %-10s  %8s  %4s  %-6s' % (pintarguiones('IDALUMNO'),pintarguiones('NOMBRE'),pintarguiones('ESTATURA'),pintarguiones('EDAD'),pintarguiones('CASADO')))

def cuerpo(alumno_d):
    print('%-8s  %-10s  %8.2f  %4d  %-6s' % (alumno_d['idAlumno'],alumno_d['nombre'],alumno_d['estatura'],alumno_d['edad'],alumno_d['casado']))

def pintarguiones(cadena):
    s = ''
    for i in range(len(cadena)):
        s = s + '-'
    return s

def listaIdAlumno(cadena):
    lista = cadena.split('-')
    for i in lista:
        pass

def validarSintaxiRangoIdAlumno(cadena):
    correcto = re.fullmatch('A[0-9]+-A[0-9]+', cadena)
    return correcto

def validarValoresRangoIdAlumno(cadena):
    bandera = False
    cadenar = re.sub('A','',cadena)
    lista = cadenar.split('-')
    if int(lista[0]) < int(lista[1]):
       bandera = True
    return bandera

def listaRango(cadena):
    cadenar = re.sub('A','',cadena)
    lista = cadenar.split('-')
    return lista

def menu():
    while True:
        os.system("cls")
        print('MENU')
        print('----')
        print('1. MOSTRAR TODOS LOS ALUMNOS')
        print('2. BUSCAR UN ALUMNO POR SU ID')
        print('3. ELIMINAR UN ALUMNO POR SU ID')
        print('4. ACTUALIZAR NOMBRE DE UN ALUMNO')
        print('5. BUSCAR UN RANGO DE ID DE ALUMNOS')
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
        elif opcion == '5':
             os.system('cls'),opcion5_1(),os.system('pause')
        elif opcion == '0':
            break
        else:
            pass

def opcion1():
    print('1. MOSTRAR TODOS LOS ALUMNOS')
    print('----------------------------\n')
    mostrar()
    print()

def opcion2():
    print('2. BUSCAR UN ALUMNO POR SU ID')
    print('-----------------------------\n')
    idAlumno = input('IGRESE ID ALUMNO A BUSCAR? ')
    alumno_d = buscar(idAlumno)
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
    bandera = eliminar(idAlumno)
    if bandera != False:
       print(),mostrar()
       print(f'\nOK: ALUMNO {idAlumno} SE ELIMINO')
    else:
       print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')
    print()

def opcion4():
    print('3. ACTUALIZAR NOMBRE DE UN ALUMNO')
    print('---------------------------------\n')
    idAlumno = input('INGRESE ID DEL ALUMNO A ACTUALIZAR? ')
    alumno_d = buscar(idAlumno)
    if alumno_d != {}:
       print(f'\nNOMBRE ANTIGUO {alumno_d["nombre"]}')
       nombre = input('\nINGRESE NOMBRE NUEVO? ')
       alumno_d["nombre"] = nombre
       print(), mostrar()
    else:
       print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')
    print()

def opcion5():
    print('5. BUSCAR UN RANGO DE ID DE ALUMNOS')
    print('-----------------------------------\n')
    rangoIdAlumno = input('IGRESE RANGO DE ID ALUMNOS A BUSCAR? ')
    if validarSintaxiRangoIdAlumno(rangoIdAlumno):
       if validarValoresRangoIdAlumno(rangoIdAlumno):
          lista = listaRango(rangoIdAlumno)
          print(),cabecera()
          for i in range(int(lista[0]),int(lista[1])+1):
              idAlumno = 'A' + str(i)
              alumno_d = buscar(idAlumno)
              if alumno_d != {}:
                  cuerpo(alumno_d)
              else:
                  print(f'\nERROR: ALUMNO {idAlumno} NO EXISTE')
                  print()
       else:
          print('ERROR: VALORES RANGO NO VALIDO')
    else:
       print('ERROR: SINTAXIS RANGO NO VALIDO')
    print()

def opcion5_1():
    print('5. BUSCAR UN RANGO DE ID DE ALUMNOS')
    print('-----------------------------------\n')
    rangoIdAlumno = input('IGRESE RANGO DE ID ALUMNOS A BUSCAR? ')
    if validarSintaxiRangoIdAlumno(rangoIdAlumno):
       if validarValoresRangoIdAlumno(rangoIdAlumno):
          lista = listaRango(rangoIdAlumno)
          alumnosrango_l = []
          for i in range(int(lista[0]),int(lista[1])+1):
              idAlumno = 'A' + str(i)
              alumno_d = buscar(idAlumno)
              if alumno_d != {}:
                 alumnosrango_l.append(alumno_d)
          if alumnosrango_l != []:
             print(),cabecera()
             for alumno_d in alumnosrango_l:
                 cuerpo(alumno_d) 
          else:
             print('ERROR: LISTA VACIA')
       else:
          print('ERROR: VALORES RANGO NO VALIDO')
    else:
       print('ERROR: SINTAXIS RANGO NO VALIDO')
    print()
    
def main():
    menu()
    
if __name__ == "__main__":
   main()