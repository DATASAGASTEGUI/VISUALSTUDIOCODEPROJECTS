#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def interseccion():
    a = {1,2,3,4}
    b = {1,2,5,6}
    interseccion = a & b
    print(interseccion) # {1, 2}

def union():
    a = {1,2,3,4}
    b = {1,2,5,6}
    union = a | b
    print(union) # {1, 2, 3, 4, 5, 6}

def diferencia():
    a = {1,2,3,4}
    b = {1,2,5,6}
    diferencia = a - b
    print(diferencia) # {3, 4}

def inclusion():
    a = {1,2,3,4}
    b = {1,2,5,6}
    inclusion = a >= b # a incluye b
    print(inclusion) # False

    a = {1,2}
    b = {1,2,5,6}
    inclusion = b >= a # b incluye a
    print(inclusion) # True

def disjuntos(): # No tienen elementos en común
    a = {1,2}
    b = {1,2,5,6}
    print(a.isdisjoint(b)) # Falso

    a = {1,2}
    b = {5,6}
    print(a.isdisjoint(b)) # True
def main():
    os.system("cls")
    disjuntos()
          
if __name__ == "__main__":
   main()