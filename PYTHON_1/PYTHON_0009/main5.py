#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    cadena = "hose:casa,one:uno,computer:computadora,tabel:tabla"
    diccionario = {}
    lista1 = cadena.split(',')
    for e in lista1:
        clave,valor = e.split(':')
        diccionario[clave] = valor
    print(diccionario)
    clave = 'tabel'
    valor = diccionario.get(clave)
    if valor != None:
       print(valor)
    else:
       print('NO SE ENCUENTRA LA CLAVE')


def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()