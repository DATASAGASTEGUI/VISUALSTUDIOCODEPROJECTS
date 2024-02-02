#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from conexion_mysql import get_conexion
from crud import crear_tabla, existe_tabla, insertar_registro, obtener_registro, buscar_registro, eliminar_registro, actualizar_registro, eliminar_todos_registros
from entrada import numero_entero, cadena_nombre
from util import mostrar_registro_1, mostrar_registro_2

conexion = get_conexion()

alumnos_l = [('Vanessa','Goycochea Ledezma','Tarde','2000-01-01'),
             ('Miguel','Ruiz Rodriguez','Tarde','2000-01-01'),
             ('Carlos','Lescano Parraga','Mañana','2001-01-02'),
             ('María','Jauregu Ledezma','Tarde','2002-02-13'),
             ('Arturo','Roncal Alva','Mañana','2000-02-01'),
             ('Ismael','Prado Bartra','Tarde','2001-01-12'),
             ('Melissa','Vazquez Rios','Mañana','2003-03-01'),
             ('Esther','Rabanal Marconi','Tarde','2000-07-10'),
             ('Roxana','Díaz Gamarra','Tarde','2004-01-01'),
             ('Jose','Cuba Orbegozo','Mañana','2003-07-12')]

def menu():
	while True:
          os.system("cls")
          print('MENU')
          print('----')
          print('(1) CREAR TABLA')
          print('(2) INSERTAR REGISTRO')
          print('(3) MOSTRAR REGISTRO')
          print('(4) ELIMINAR REGISTRO')
          print('(5) ACTUALIZAR REGISTRO')
          print('(6) BUSCAR REGISTRO')
          print('(7) ELIMINAR TODOS REGISTROS')
          print('(0) SALIR')

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
               os.system('cls'),opcion5(),os.system('pause')
          elif opcion == '6':
               os.system('cls'),opcion6(),os.system('pause')
          elif opcion == '7':
               os.system('cls'),opcion7(),os.system('pause')
          elif opcion == '0':
               os.system('cls')
               print('\nGRACIAS POR SU VISITA\n')
               os.system('pause')
               os.system('cls')
               break
          else:pass

def opcion1():
    print('(1) CREAR TABLA')
    print('---------------')
    if conexion != None:
       if not existe_tabla('alumno',conexion):
            if crear_tabla(conexion):
                print('OK: CREAR TABLA')
            else:
                print('ERROR: CREAR TABLA')
       else:
          print("ERROR: YA EXISTE TABLA")
    else:
       print('ERROR: CONEXION')

def opcion2():
    print('(2) INSERTAR REGISTRO')
    print('---------------------')
    if conexion != None:
       if existe_tabla('alumno',conexion):
            for alumno_t in alumnos_l:
                if insertar_registro(alumno_t,conexion):
                   print('OK: INSERTAR REGISTRO')
                else:
                   print('ERROR: INSERTAR REGISTRO')
       else:
          print("ERROR: NO EXISTE TABLA")
    else:
       print('ERROR: CONEXION')   

def opcion3():
    print('(3) MOSTRAR REGISTRO')
    print('--------------------')
    if conexion != None:
       if existe_tabla('alumno',conexion):
          retorno_l = obtener_registro(conexion)
          if retorno_l[0]:
             if len(retorno_l[1]) > 0:
                if mostrar_registro_1(retorno_l[1]):
                    print('OK: MOSTRAR REGISTRO 1')
                else:
                    print('ERROR: MOSTRAR REGISTRO 1')
             else:
                 print('ERROR: LISTA VACIA')
          else:
              print('ERROR: OBTENER REGISTRO')
       else:
          print("ERROR: NO EXISTE TABLA")
    else:
       print('ERROR: CONEXION')   

def opcion4():
    print('(4) ELIMINAR REGISTRO')
    print('---------------------')
    if conexion != None:
        idAlumnoEliminar = numero_entero('INGRESE ID ALUMNO A ELIMINAR? ')
        alumno_t = buscar_registro(idAlumnoEliminar,conexion)
        if alumno_t != None:
           if eliminar_registro(idAlumnoEliminar,conexion):
              print('OK: ELIMINAR REGISTRO')
           else:
              print('ERROR: ELIMINAR REGISTRO')
        else:
           print('ERROR: ALUMNO NO EXISTE')
    else:
        print('ERROR: CONEXION')  

def opcion5():
    print('(5) ACTUALIZAR REGISTRO')
    print('-----------------------')
    if conexion != None:
        idAlumnoActualizar = numero_entero('INGRESE ID ALUMNO A ACTUALIZAR? ')
        alumno_t = buscar_registro(idAlumnoActualizar,conexion)
        if alumno_t != None:
           nombre_nuevo = cadena_nombre('INGRESE NOMBRE NUEVO A ACTUALIZAR? ')
           if actualizar_registro(idAlumnoActualizar,nombre_nuevo,conexion):
              print('OK: ACTUALIZAR REGISTRO')
           else:
              print('ERROR: ACTUALIZAR REGISTRO')
        else:
           print('ERROR: ALUMNO NO EXISTE')
    else:
        print('ERROR: CONEXION')   

def opcion6():
    print('(6) BUSCAR REGISTRO')
    print('-------------------')
    if conexion != None:
        idAlumnoBuscar = numero_entero('INGRESE ID ALUMNO A BUSCAR? ')
        alumno_t = buscar_registro(idAlumnoBuscar,conexion)
        if alumno_t != None:
           if mostrar_registro_2(alumno_t):
              print('OK: MOSTRAR REGISTRO 2') 
           else:
              print('ERROR: MOSTRAR REGISTRO 2')
        else:
           print('ERROR: ALUMNO NO EXISTE')
    else:
        print('ERROR: CONEXION')  

def opcion7():
    print('(7) ELIMINAR TODOS REGISTROS')
    print('----------------------------')
    if conexion != None:
       if eliminar_todos_registros(conexion):
          print('OK: ELIMINAR TODOS REGISTROS')
       else:
          print('ERROR: ELIMINAR TODOS REGISTROS')
    else:
        print('ERROR: CONEXION')  

def main():
    menu()
          
if __name__ == "__main__":
   main()