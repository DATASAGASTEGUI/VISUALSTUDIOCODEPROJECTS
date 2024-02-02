#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re


def ejemplo1():
    cadena = 'Hola Mundo'
    for e in cadena:
        print(e, end='')


def ejemplo2():
    cadena = 'Hola Mundo'
    for i in range(len(cadena)):
        print(cadena[i], end='')


def ejemplo3():
    cadena = 'Hola Mundo'
    n = len(cadena)
    for i in range(n-1, -1, -1):
        print(cadena[i], end='')


def ejemplo4():
    cadena = 'Hola Mundo'
    caracteres_l = list(cadena)
    for e in caracteres_l:
        print(e, end='')


def ejemplo5():
    cadena = 'Hola Mundo'
    for i,e in enumerate(cadena):
        print("%5d  %-5s" % (i,e))


def main():
    os.system("cls")
    ejemplo5()
          
if __name__ == "__main__":
   main()