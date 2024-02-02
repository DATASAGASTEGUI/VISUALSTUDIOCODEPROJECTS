#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    tupla = (1, 2, 3, 4, 5)

    for e in tupla:
        print(e,end=' ')

    print()

    for i in range(len(tupla)):
        print(tupla[i],end=' ')

    print()

    for i,e in enumerate(tupla):
        print(f'Indice {i}, Valor {e}')

def ejemplo2():
    tupla = (('a', 1), ('b', 2), ('c', 3))

    for e in tupla:
        print(e,end=' ')

    print()

    for i in range(len(tupla)):
        print(tupla[i],end=' ')

    print()

    for i,e in enumerate(tupla):
        print(f'Indice {i}, Valor {e}')

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()