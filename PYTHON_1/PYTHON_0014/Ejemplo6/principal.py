#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from circulo import Circulo
import random

def ejemplo1():
    radio = float(input('Ingrese radio? '))
    circulo = Circulo()
    Circulo.cabecera()
    circulo.cuerpo(1,radio)

def ejemplo2():
    circulo = Circulo()
    Circulo.cabecera()
    for i in range(100):
        radio = random.uniform(1,100)
        circulo.cuerpo((i+1),radio)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()