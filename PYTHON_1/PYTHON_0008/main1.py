#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    print('EJEMPLO 1')
    print('---------')
    matriz = [[0, 1, 2], 
              [3, 4, 5]]

    nfilas = len(matriz)
    ncolumnas = len(matriz[0])

    print('RRECORRER POR INDICE')
    print('--------------------')
    for i in range(nfilas):
        for j in range(ncolumnas):  
            print("%5d" % (matriz[i][j]), end="")
        print()
    print('RECORRER POR ELEMENTO')
    print('---------------------')
    for fila in matriz:
        for e in fila:
            print("%5d" % (e), end="")
        print()
    print('RECORRER POR FILA')
    print('-----------------')
    for fila in matriz:
        print(fila)

    print('IMPRIMIR LA MATRIZ COMPLETA')
    print('---------------------------')
    print(matriz)

def main():
    os.system("cls")
    ejemplo1()

if __name__ == "__main__":
   main()