#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import random

def ejercicio5():
    print('1. LLENAR MATRIZ')
    print('----------------')
    nf = 6
    nc = 10
    matriz = []
    for i in range(nf):
        fila = []
        for j in range(nc):
            valor = random.randint(0,1000)
            fila.append(valor)
        matriz.append(fila)

    print('2. MOSTRAR MATRIZ')
    print('-----------------')
    for fila in matriz:
        print(fila)

    print('3. POSICION TANTO MAXIMO COMO MINIMO')
    print('------------------------------------')
    maximo = matriz[0][0]
    minimo = matriz[0][0]

    maxi = 0
    maxj = 0

    mini = 0
    minj = 0

    for i in range(nf):
        for j in range(nc):
            if matriz[i][j] > maximo:
               maximo = matriz[i][j]
               maxi = i
               maxj = j
            if matriz[i][j] < minimo:
               minimo = matriz[i][j]
               mini = i
               minj = j

    print(f"Máximo {maxi},{maxj} = {maximo}")
    print(f"Mínimo {mini},{minj} = {minimo}")
              

def main():
    os.system("cls")
    ejercicio5()
          
if __name__ == "__main__":
   main()