#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from circulo import Circulo
from util import Util
import random

def ejemplo1():
    radio = float(input('Ingrese radio? '))
    circulo = Circulo(radio)
    Circulo.cabecera()
    circulo.cuerpo(1)

def ejemplo2():
    radio = float(input('Ingrese radio? '))
    circulo = Circulo()
    circulo.set_radio(radio)
    Circulo.cabecera()
    circulo.cuerpo(1)

def ejemplo3():
    Circulo.cabecera()
    for i in range(100):
        radio = random.uniform(1,100)
        circulo = Circulo(radio)
        circulo.cuerpo((i+1))

def ejemplo4():
    for i in range(100):
        radio = random.uniform(1,100)
        circulo = Circulo(radio)
        print(circulo)

def ejemplo5():
    circulo = Circulo()
    for i in range(100):
        radio = random.uniform(1,100)
        circulo.set_radio(radio)
        print(circulo)

if __name__ == "__main__":
   os.system("cls")
   ejemplo4()