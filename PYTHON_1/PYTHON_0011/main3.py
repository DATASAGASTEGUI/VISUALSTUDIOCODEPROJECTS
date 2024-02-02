#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    tupla1 = (('a', 1), ('e', 2), ('i', 3), ('o', 4))
    lista1 = list(tupla1)
    print(lista1) # [('a', 1), ('e', 2), ('i', 3), ('o', 4)]
    indice1 = lista1.index(('o', 4))
    del lista1[indice1]
    lista1.append(('o',5))
    print(lista1)
    tupla1 = tuple(lista1)
    print(tupla1)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()