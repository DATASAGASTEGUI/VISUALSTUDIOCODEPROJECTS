#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    enteros_l = [1,3,9,3,1]
    print(enteros_l)
    sinduplicados_l = list(set(enteros_l))
    print(sinduplicados_l)

def ejemplo2():
    palabras_l = ['en','un','puerto','italiano','en','un']
    sinduplicados_l = list(set(palabras_l)) 
    print(sinduplicados_l)

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()

