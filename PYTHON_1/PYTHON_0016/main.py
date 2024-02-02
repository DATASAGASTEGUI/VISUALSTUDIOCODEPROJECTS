#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from mimodulo import submodulo

def ejemplo1():
    submodulo.saludar()

    persona = submodulo.Persona("Juan")
    persona.presentarse()
     

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()