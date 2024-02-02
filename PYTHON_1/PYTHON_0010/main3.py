#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re

def ejemplo1():
    cadena = 'Hola Mundo'
    patron = "[aeiouáéíóú]"
    print(cadena)
    for e in cadena:
        if re.fullmatch(patron, e):
           cadena = cadena.replace(e,'x')

def ejemplo2():
    cadena = 'Hola Mundo'
    patron = "[aeiouáéíóú]"
    print(cadena)
    cadena = re.sub(patron,'x',cadena)
    print(cadena)


def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()