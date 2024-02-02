#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1(): # del
    print('EJEMPLO 1: ELIMINAR EL ELEMENTO QUE OCUPA EL INDICE 4')
    enteros_l = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
    del enteros_l[4]
    print(enteros_l) # [2, 1, 2, 3, 6, 7, 6, 4, 8]

def ejemplo2(): # del
    print('EJEMPLO 2: ELIMINAR Y OBTENER EL ELEMENTO QUE OCUPA EL INDICE 4')
    enteros_l = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
    elemento = enteros_l.pop(4)
    print(enteros_l) # [2, 1, 2, 3, 6, 7, 6, 4, 8]
    print(elemento) #0

def ejemplo3(): # del
    print('EJEMPLO 3: ELIMINAR UN ELEMENTO ESPECIFICO EL ELEMENTO 0')
    enteros_l = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
    enteros_l.remove(0)
    print(enteros_l) # [2, 1, 2, 3, 6, 7, 6, 4, 8]

def main():
    os.system("cls")
    ejemplo1()
    ejemplo2()
    ejemplo3()




if __name__ == "__main__":
   main()