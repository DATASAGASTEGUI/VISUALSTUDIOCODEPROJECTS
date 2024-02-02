#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re

def ejemplo1():
    cadena = 'Direccion Prado 124 Bloque 3, Piso 1 C'
    patron = "[0-9]+"
    print(cadena)
    rcadena = re.sub(patron,'',cadena)
    print(rcadena)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()