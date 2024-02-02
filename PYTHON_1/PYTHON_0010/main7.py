#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re

def ejemplo1():
    oracion = "En un puerto italiano al pie de la montaña"
    patron = "[\\s]+"
    roracion = re.sub(patron,'',oracion)
    caracteres_l = list(roracion)
    print(caracteres_l)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()