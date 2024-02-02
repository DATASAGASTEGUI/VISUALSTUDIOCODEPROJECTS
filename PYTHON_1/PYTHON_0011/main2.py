#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    tupla1 = (1, 2, 3)
    elemento = 4
    # tupla1 = tupla1 + elemento # Error no se puede modificar
    tupla2 = tupla1 + (elemento,)
    print(tupla2) # (1, 2, 3, 4)

def ejemplo2():
    tupla1 = (('a',1),('e',2), ('i',3), ('o',4))
    elemento = ('u',5)
    tupla2 = tupla1 + (elemento,)
    print(tupla2) # (('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5))

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()