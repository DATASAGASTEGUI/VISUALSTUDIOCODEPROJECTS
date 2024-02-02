#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import json

# -----------------------------------------------------------------------------
def ejemplo1():
    nra = '.\\VISUALSTUDIOCODEPROJECTS\\PYTHON_1\\PYTHON_0019\\Ejemplo1\\datos1.json' # 1
    with open(nra, 'r') as filejson: # 2         
         datos = json.load(filejson)

    nombre = datos['nombre'] # 3
    edad = datos['edad']
    direccion = datos['direccion']

    print(f"Nombre: {nombre}") # 4
    print(f"Edad: {edad}")
    print(f"Dirección: {direccion}")

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Imprimir los valores para verificar que se hayan leído correctamente.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def ejemplo2():
    nra = 'PYTHON_0019\\Ejemplo1\\datos2.json' # 1
    with open(nra, 'r') as filejson: # 2         
         datos = json.load(filejson)

    usuarios = datos['usuarios'] # 3

    for usuario in usuarios: # 4
        nombre = usuario['nombre']
        edad = usuario['edad']
        direccion = usuario['direccion']
        hobbies = usuario['hobbies']
    
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Dirección:", direccion)
        print("Hobbies:", hobbies)
        print()

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Iterar sobre cada usuario y obtener sus detalles
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def ejemplo3():
    nra = 'PYTHON_0019\\Ejemplo1\\datos3.json' # 1
    with open(nra, 'r') as filejson: # 2         
         datos = json.load(filejson)

    alumnos = datos['alumnos'] # 3

    for alumno in alumnos: # 4
        nombre = alumno['nombre']
        edad = alumno['edad']
        curso = alumno['curso']
    
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Curso:", curso)
        print()

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Iterar sobre cada usuario y obtener sus detalles
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def ejemplo4():
    nra = 'PYTHON_0019\\Ejemplo1\\datos4.json' # 1
    with open(nra, 'r') as filejson: # 2         
         alumnos = json.load(filejson) # 3

    for alumno in alumnos: # 4
        nombre = alumno['nombre']
        edad = alumno['edad']
        curso = alumno['curso']
    
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Curso:", curso)
        print()

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Iterar sobre cada usuario y obtener sus detalles
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def ejemplo5():
    nra = 'PYTHON_0019\\Ejemplo1\\datos5.json' # 1
    with open(nra, 'r') as filejson: # 2         
         datos = json.load(filejson)

    empleados = datos['empleados'] # 3

    for empleado in empleados: # 4
        idEmpleado = empleado['id']
        nombre = empleado['nombre']
        edad = empleado['edad']
        puesto = empleado['puesto']
        
        print("ID:", idEmpleado)
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Puesto:", puesto)

        proyectos = empleado['proyectos']

        print("Proyectos:")

        for proyecto in proyectos:
            nombreProyecto = proyecto['nombre']
            cliente = proyecto['cliente']
            print(" - Nombre del proyecto:", nombreProyecto)
            print("   Cliente:", cliente)
        
        print()

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Iterar sobre cada usuario y obtener sus detalles
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def ejemplo6():
    nra = 'PYTHON_0019\\Ejemplo1\\datos6.json' # 1
    with open(nra, 'r') as filejson: # 2         
         empleados = json.load(filejson)

    for empleado in empleados: # 4
        idEmpleado = empleado['id']
        nombre = empleado['nombre']
        edad = empleado['edad']
        puesto = empleado['puesto']
        
        print("ID:", idEmpleado)
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Puesto:", puesto)

        proyectos = empleado['proyectos']

        print("Proyectos:")

        for proyecto in proyectos:
            nombreProyecto = proyecto['nombre']
            cliente = proyecto['cliente']
            print(" - Nombre del proyecto:", nombreProyecto)
            print("   Cliente:", cliente)
        
        print()

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Iterar sobre cada usuario y obtener sus detalles
# -----------------------------------------------------------------------------

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()


