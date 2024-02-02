#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import random

def ejercicio():
    print('1. LLENAR VECTOR')
    print('----------------')
    paises = ['España','Rusia','Japon','Australia']
    print('2. LLENAR MATRIZ')
    print('----------------')
    nf = 4
    nc = 10
    matriz = []
    for i in range(nf):
        fila = []
        for j in range(nc):
            valor = random.randint(140,210)
            fila.append(valor)
        matriz.append(fila)
    print('3. CALCULAR MEDIA')
    print('-----------------')
    am = 0
    medias = [] 
    for fila in matriz:
        am = 0
        for e in fila:
            am = am + e
        media = am / len(fila)
        medias.append(media)
    print('3. CALCULAR MINIMO Y MAXIMO')
    print('---------------------------')
    minimos = []
    maximos = []
    for fila in matriz:
        minimo = min(fila)
        maximo = max(fila)
        minimos.append(minimo)
        maximos.append(maximo)

    print('4. MOSTRAR VECTOR Y MATRIZ')
    print('--------------------------')
    i = 0
    for fila in matriz:
        print('%-12s  %-45s  %10.2f  %5d  %5d' % (paises[i],fila,medias[i], minimos[i], maximos[i]))
        i += 1

def main():
    os.system("cls")
    ejercicio()
    
          
if __name__ == "__main__":
   main()