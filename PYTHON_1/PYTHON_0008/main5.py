#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import random

def ejercicio12():
    print('1. LLENAR MATRIZ')
    print('----------------')
    nf = 9
    nc = 9
    matriz = []
    for i in range(nf):
        fila = []
        for j in range(nc):
            valor = random.randint(500,900)
            fila.append(valor)
        matriz.append(fila)
    print('2. MOSTRAR MATRIZ')
    print('-----------------')
    for fila in matriz:
        print(fila)
    print('3. MOSTRAR NUMEROS DIAGONAL')
    print('---------------------------')
    vector = []
    for i,j in zip(range(nf-1,-1,-1),range(0,9,1)):
        valor = matriz[i][j]
        vector.append(valor)
        print(valor,end='  ')
    
    minimo = min(vector)
    maximo = max(vector)
    media = sum(vector) / len(vector)

    print()

    print('Mínimmo: ', minimo)
    print('Máximo : ', maximo)
    print('Media  : ', round(media,2))



def main():
    os.system("cls")
    ejercicio12()
          
if __name__ == "__main__":
   main()