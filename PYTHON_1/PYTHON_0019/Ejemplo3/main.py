#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import json

def ejemplo1():
    # Nombre del archivo JSON al que deseas agregar datos
    nra = 'PYTHON_0019\\Ejemplo3\\datos.json'

    # Crear un diccionario con los datos a agregar
    nuevo_dato = {
       "nombre": "Carlos García",
       "edad": 32,
       "puesto": "Gerente"
    }

    # Leer el contenido actual del archivo JSON
    with open(nra, 'r') as filejson:
         datos_existentes = json.load(filejson)

    # Agregar el nuevo dato a la lista existente
    datos_existentes.append(nuevo_dato)

    # Escribir el contenido actualizado en el archivo JSON
    with open(nra, 'w') as filejson:
         # Escribir los datos en el archivo JSON
         json.dump(datos_existentes, filejson, indent=4)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()