#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def contar_frecuencia(texto):
    palabras = texto.lower().split()
    #palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def main():
    os.system("cls")
    texto = "Este es un texto de ejemplo. Ejemplo de texto."
    frecuencia_palabras = contar_frecuencia(texto)
    print(frecuencia_palabras)
          
if __name__ == "__main__":
   main()