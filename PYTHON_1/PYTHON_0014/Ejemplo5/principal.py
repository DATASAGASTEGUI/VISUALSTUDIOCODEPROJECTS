#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from circulo import Circulo
import random

def ejemplo1():
    radio = float(input('Ingrese radio? '))
    Circulo.cabecera()
    Circulo.cuerpo(1,radio)

def ejemplo2():
    Circulo.cabecera()
    for i in range(100):
        radio = random.uniform(1,100)
        Circulo.cuerpo((i+1),radio)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()