#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import random

def ejemplo1():
    print('EJEMPLO 1')
    print('---------')
    nfilas = int(input("Ingrese el número de filas de la matriz: "))
    ncolumnas = int(input("Ingrese el número de columnas de la matriz: ")) 
    matriz = [] 
    for i in range(nfilas):
        fila = []
        for j in range(ncolumnas):
            valor = int(input(f'Ingrese elemento [{i},{j}] = ')) 
            fila.append(valor)
        matriz.append(fila)

def ejemplo2():
    print('EJEMPLO 2')
    print('---------')
    nfilas = int(input("Ingrese el número de filas de la matriz: "))
    ncolumnas = int(input("Ingrese el número de columnas de la matriz: ")) 
    matriz = [] 
    for i in range(nfilas):
        fila = []
        for j in range(ncolumnas):
            valor = random.randint(1,6)
            fila.append(valor)
        matriz.append(fila)

    for fila in matriz:
        print(fila)

def main():
    os.system("cls")
    ejemplo2()

if __name__ == "__main__":
   main()