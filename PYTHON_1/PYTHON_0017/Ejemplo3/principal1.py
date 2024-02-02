#!/usr/bin/env python
# -*- coding: utf8 -*-

from os import path
import os
import sqlite3
from sqlite3 import Error
from datetime import datetime

def cabecera():
    print('%8s  %-6s  %4s  %8s  %10s  %6s' % ('IDALUMNO','NOMBRE','NOTA','ESTATURA','NACIMIENTO','CASADO'))
    print('%8s  %-6s  %4s  %8s  %10s  %6s' % ('--------','------','----','--------','----------','------'))

def cuerpo(registro_t):
    print('%8s  %-6s  %4s  %8s  %10s  %6s' % (registro_t[0],registro_t[1],registro_t[2],registro_t[3],getFormatoFechoDiaMesAnio(registro_t[4]),registro_t[5]))

def getFormatoFechoDiaMesAnio(fecha_entrada):
    objeto_fecha = datetime.strptime(fecha_entrada,"%Y-%m-%d")
    fecha_salida = objeto_fecha.strftime("%d/%m/%Y")
    return fecha_salida

def crear_tabla():
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE Alumno (
                      idAlumno         INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
                      nombre           VARCHAR(20) NOT NULL,
                      nota             INTEGER     NOT NULL,
                      estatura         DOUBLE      NOT NULL,
                      fecha_nacimiento VARCHAR(10) NOT NULL,
                      casado           BOOLEAN     NOT NULL
                  );''')
    conexion.commit()
    conexion.close()
    print("OK: CREAR TABLA")

def insertar_registro():
    inserts_l = ["INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Carlos',5,1.70,'2000-01-15',true)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Miguel',10,1.65,'1999-02-20',false)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('María',7,1.60,'2000-04-10',true)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('José',8,1.65,'2005-03-23',false)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Alicia',6,1.72,'1972-01-10',true)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Angel',7,1.71,'2000-01-10',true)"]
    
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    for insert in inserts_l:
        cursor.execute(insert)
    conexion.commit()
    conexion.close()
    print("OK: INSERTAR REGISTRO")

def insertar_registro1():
    tuplas_l = [('Carlos',5,1.70,'2000-01-15',1),
                 ('Miguel',10,1.65,'1999-02-20',0),
                 ('María',7,1.60,'2000-04-10',1),
                 ('José',8,1.65,'2005-03-23',0),
                 ('Alicia',6,1.72,'1972-01-10',1),
                 ('Angel',7,1.71,'2000-01-10',1)]
    
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.executemany('''INSERT INTO Alumno (nombre, nota, estatura, fecha_nacimiento, casado)
                          VALUES (?, ?, ?, ?, ?)''',tuplas_l)
    conexion.commit()
    conexion.close()
    print("OK: INSERTAR REGISTRO")

def mostrar_registro():
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Alumno")
    registros_l = cursor.fetchall()
    for registro in registros_l:
        print(registro)
    conexion.close()
    print("OK: MOSTRAR REGISTRO")    

def mostrar_registro1():
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Alumno")
    registros_l = cursor.fetchall() # Lista de elementos de tipo tupla
    cabecera()
    for registro_t in registros_l:
        cuerpo(registro_t)
    conexion.close()
    print("OK: MOSTRAR REGISTRO")   

def eliminar_tabla():
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS Alumno")
    conexion.commit()
    conexion.close()
    print("OK: ELIMINAR_TABLA")   

def eliminar_registro():
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    idAlumnoEliminar = 6
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Alumno WHERE idAlumno = ?",(idAlumnoEliminar))
    conexion.commit()
    conexion.close()
    print("OK: ELIMINAR_REGISTRO")   

def actualizar_registro():
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    idAlumnoActualizar = 2
    nombre_nuevo = 'Arturo'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    cursor.execute('UPDATE Alumno SET nombre = ? WHERE idAlumno = ?', (nombre_nuevo, idAlumnoActualizar))
    conexion.commit()
    conexion.close()
    print("OK: ACTUALIZAR_REGISTRO") 





def main():
    os.system("cls")
    actualizar_registro()
    mostrar_registro1()    
          
if __name__ == "__main__":
   main()