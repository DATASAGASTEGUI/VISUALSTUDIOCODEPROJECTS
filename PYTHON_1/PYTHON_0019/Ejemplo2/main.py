#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import json

# -----------------------------------------------------------------------------
def ejemplo1():
    # Crear un diccionario con los datos
    datos = {
        "nombre": "Juan Pérez",
        "edad": 30,
        "puesto": "Desarrollador"
    }

    # Nombre del archivo JSON en el que deseas escribir
    nra = 'PYTHON_0019\\Ejemplo2\\datos1.json'

    # Abrir el archivo JSON en modo escritura
    with open(nra, 'w') as filejson:
         # Escribir los datos en el archivo JSON
         json.dump(datos, filejson)
# -----------------------------------------------------------------------------   

# -----------------------------------------------------------------------------
def ejemplo2():
    # Crear un diccionario con los datos
    datos = [
    {
        "nombre": "Juan Pérez",
        "edad": 30,
        "puesto": "Desarrollador"
    },
    {
        "nombre": "María Gómez",
        "edad": 35,
        "puesto": "Diseñadora"
    }
    ]

    # Nombre del archivo JSON en el que deseas escribir
    nra = 'PYTHON_0019\\Ejemplo2\\datos2.json'

    # Abrir el archivo JSON en modo escritura
    with open(nra, 'w') as filejson:
         # Escribir los datos en el archivo JSON
         json.dump(datos, filejson)
# -----------------------------------------------------------------------------   

# -----------------------------------------------------------------------------
def ejemplo3():
    # Crear un diccionario con los datos
    datos = {
    "empresa": "Acme Inc.",
    "empleados": [
        {
            "id": 1,
            "nombre": "Juan Pérez",
            "edad": 30,
            "puesto": "Desarrollador",
            "proyectos": [
                {
                    "nombre": "Proyecto A",
                    "cliente": "Empresa X"
                },
                {
                    "nombre": "Proyecto B",
                    "cliente": "Empresa Y"
                }
            ]
        },
        {
            "id": 2,
            "nombre": "María Gómez",
            "edad": 35,
            "puesto": "Diseñadora",
            "proyectos": [
                {
                    "nombre": "Proyecto C",
                    "cliente": "Empresa Z"
                },
                {
                    "nombre": "Proyecto D",
                    "cliente": "Empresa W"
                }
            ]
        }
    ]
    }

    # Nombre del archivo JSON en el que deseas escribir
    nra = 'PYTHON_0019\\Ejemplo2\\datos3.json'

    # Abrir el archivo JSON en modo escritura
    with open(nra, 'w') as filejson:
         # Escribir los datos en el archivo JSON con indentación para mayor legibilidad
         json.dump(datos, filejson, indent=4)
# -----------------------------------------------------------------------------   

def main():
    os.system("cls")
    ejemplo3()
          
if __name__ == "__main__":
   main()


