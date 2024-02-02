#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re

def ejemplo1():
    oracion = "En un puerto italiano al pie de la montaña"
    cadena = re.sub('[\\s]+','',oracion)
    letras_l = list(cadena)
    letrasdistintas_l = []
    for e in letras_l:
        if e not in letrasdistintas_l:
           letrasdistintas_l.append(e)

    print(letrasdistintas_l)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()