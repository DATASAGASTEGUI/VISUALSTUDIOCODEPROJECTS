#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    conjunto = {10, 3, 9, 1}
    conjunto.remove(10)
    print(conjunto)

def ejemplo2():
    conjunto = {10, 3, 9, 1}
    conjunto.clear()
    print(conjunto)

def ejemplo3():
    conjunto = {10, 3, 9, 1}
    conjunto_copia = conjunto.copy()
    for e in conjunto_copia:
        conjunto.remove(e)
    print(conjunto)

def ejemplo4():
    conjunto = {10, 3, 9, 3, 1}
    for i in range(len(conjunto)):
        x = conjunto.pop()
        print(x)
    print(conjunto)

def main():
    os.system("cls")
    ejemplo4()
          
if __name__ == "__main__":
   main()