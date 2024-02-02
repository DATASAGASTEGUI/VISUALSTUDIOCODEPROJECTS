#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    conjunto = {1, 2, 3, 3}
    print(conjunto) # {1, 2, 3}
    for e in conjunto:
        print(e)

def ejemplo2():
    conjunto = {'Lapiz','Cuaderno','Lapiz','Atlas'}
    print(conjunto) # {'Atlas', 'Lapiz', 'Cuaderno'}  
    for e in conjunto:
        print(e)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()