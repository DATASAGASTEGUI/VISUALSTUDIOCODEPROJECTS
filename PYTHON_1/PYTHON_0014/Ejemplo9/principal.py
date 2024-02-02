#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import random
from circulo import Circulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from triangulo import Triangulo
from figurageometrica2d import FiguraGeometrica2D

f = ['Triangulo', 'Cuadrado', 'Circulo', 'Rectangulo'];
fgs = []

def ejemplo1():
    n = int(input('INGRESE LA CANTIDAD DE OBJETOS A CREAR? '))
    for i in range(n):
        j = random.randint(0,3)
        if f[j] == 'Circulo':
           radio = round(random.uniform(1,100),2)
           circulo = Circulo(radio)
           fgs.append(circulo)
        elif f[j] == 'Cuadrado':
           lado = round(random.uniform(1,100),2)
           cuadrado = Cuadrado(lado)
           fgs.append(cuadrado)
        elif f[j] == 'Rectangulo':
           largo = round(random.uniform(1,100),2)
           ancho = round(random.uniform(1,100),2)
           rectangulo = Rectangulo(largo,ancho)
           fgs.append(rectangulo)
        elif f[j] == 'Triangulo':
           base = round(random.uniform(1,100),2)
           altura = round(random.uniform(1,100),2)
           triangulo = Triangulo(base, altura)
           fgs.append(triangulo)

    print('EJEMPLO 1')
    for fg in fgs:
        print(fg)

    print('EJEMPLO 2')
    for fg in fgs:
        if isinstance(fg,Circulo):
           print(fg)   

    print('EJEMPLO 3')
    for fg in fgs:
        print(fg.numeroDimension())  

def ejemplo2():
    n = int(input('INGRESE LA CANTIDAD DE OBJETOS A CREAR? '))
    fg = FiguraGeometrica2D()
    for i in range(n):
        j = random.randint(0,3)
        if f[j] == 'Circulo':
           radio = round(random.uniform(1,100),2)
           fg = Circulo(radio)
        elif f[j] == 'Cuadrado':
           lado = round(random.uniform(1,100),2)
           fg = Cuadrado(lado)
        elif f[j] == 'Rectangulo':
           largo = round(random.uniform(1,100),2)
           ancho = round(random.uniform(1,100),2)
           fg = Rectangulo(largo,ancho)
        elif f[j] == 'Triangulo':
           base = round(random.uniform(1,100),2)
           altura = round(random.uniform(1,100),2)
           fg = Triangulo(base, altura)
        fgs.append(fg) 

    '''
    for fg in fgs:
        print(fg) 
    '''

    for i in range(len(fgs)):
        fg = fgs[i]
        print(fg)

    for fg in fgs:
        if isinstance(fg,Rectangulo):
           print(fg)

if __name__ == "__main__":
   os.system("cls")
   ejemplo2()