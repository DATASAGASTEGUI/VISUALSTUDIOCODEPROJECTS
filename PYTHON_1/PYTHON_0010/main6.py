#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    oracion = "En un puerto italiano al pie de la montaña"
    palabras_l = oracion.split()
    print(palabras_l)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()