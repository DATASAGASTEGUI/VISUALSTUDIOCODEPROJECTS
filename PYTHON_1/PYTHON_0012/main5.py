#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    conjunto = {}
    lista = [7, 9, 3, 15]
    conjunto = {*lista}
    print(conjunto) # {9, 3, 15, 7}

def ejemplo2():
    conjunto = {1,2}
    x = 5
    conjunto.add(x)
    print(conjunto) # {1, 2, 5}

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()