#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re

def ejemplo1():
    texto = "Este es un texto de ejemplo. Ejemplo de texto."
    oracion = re.sub('\\.','',texto)
    print(oracion)
    palabras_l = oracion.lower().split()
    frecuencia = {}
    for palabra in palabras_l:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    print(frecuencia)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()