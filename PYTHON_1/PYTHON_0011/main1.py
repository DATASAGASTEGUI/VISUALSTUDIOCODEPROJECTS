#!/usr/bin/env python
# -*- coding: utf8 -*-

import os


def ejemplo1():
    tupla = (1, 2, 3, 'a', 'b', 'c')
    print(tupla)


def ejemplo2():
    tupla = tuple(range(1, 6))
    print(tupla)


def ejemplo3():
    lista = [1, 2, 3, 4, 5]
    tupla = tuple(lista)
    print(tupla)

def ejemplo4():
    diccionario = {'a': 1, 'b': 2, 'c': 3}
    tupla = tuple(diccionario.items())
    print(tupla) # (('a', 1), ('b', 2), ('c', 3))

def ejemplo5():
    cadena = 'Hola Mundo'
    tupla = tuple(cadena)
    print(tupla) # ('H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o')

def main():
    os.system("cls")
    ejemplo3()

if __name__ == "__main__":
    main()
