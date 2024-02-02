#!/usr/bin/env python
# -*- coding: utf8 -*-

from os import path
import os
import sqlite3
from sqlite3 import Error
from datetime import datetime

nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'

def cabecera():
    print('%8s  %-6s  %4s  %8s  %10s  %6s' % ('IDALUMNO','NOMBRE','NOTA','ESTATURA','NACIMIENTO','CASADO'))
    print('%8s  %-6s  %4s  %8s  %10s  %6s' % ('--------','------','----','--------','----------','------'))

def cuerpo(registro_t):
    print('%8s  %-6s  %4s  %8s  %10s  %6s' % (registro_t[0],registro_t[1],registro_t[2],registro_t[3],getFormatoFechoDiaMesAnio(registro_t[4]),registro_t[5]))

def getFormatoFechoDiaMesAnio(fecha_entrada):
    objeto_fecha = datetime.strptime(fecha_entrada,"%Y-%m-%d")
    fecha_salida = objeto_fecha.strftime("%d/%m/%Y")
    return fecha_salida

def get_conexion():
    try:
        if path.exists(nra):
            conexion = sqlite3.connect(nra)
        else:
            conexion = None
        return conexion
    except Error:
        return None

def mostrar_registro(conexion):
    bandera = True
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Alumno")
        registros_l = cursor.fetchall() # Lista de elementos de tipo tupla
        cabecera()
        for registro_t in registros_l:
            cuerpo(registro_t)
        conexion.close()
    except Error:
        bandera = False
    return bandera

def existe_tabla(conexion,nombre_tabla):
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nombre_tabla,))
    resultado = cursor.fetchone()

    conexion.close()

    if resultado is not None:
        return True
    else:
        return False

def ejemplo1():
    conexion = get_conexion()
    if conexion != None:
       if(mostrar_registro(conexion)):
           print("OK: QUERY") 
       else:
           print("ERROR: QUERY")
    else:
       print("ERROR: CONEXION")

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()