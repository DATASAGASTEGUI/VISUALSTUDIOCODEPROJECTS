#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    cadena = 'Hola Mundo'
    subcadena = 'Hola'
    aux = cadena[0:len(subcadena)]
    if subcadena == aux:
       print('SI')
    else:
       print('NO')
    

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()