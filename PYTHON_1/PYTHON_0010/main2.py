#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    cadena = 'Hola Mundo'
    print(cadena)
    cadenai = ''
    for e in cadena:
        cadenai = e + cadenai
    print(cadenai)

def ejemplo2():
    cadena = 'Hola Mundo'
    cadenai = cadena[::-1]
    print(cadena)
    print(cadenai)

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()