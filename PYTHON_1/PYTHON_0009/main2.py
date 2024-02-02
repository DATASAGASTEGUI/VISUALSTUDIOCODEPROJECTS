#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

alumno_d = {'idAlumno': 'A1',
            'nombre': 'Luis',
            'edad': 23,
            'estatura': 1.72,
            'casado': False}

fruta_d = {('manzana','roja'):5, ('manzana','amarilla'):3, ('naranja','mesa'):7, ('naranza','zumo'):8, ('platano','manzano'):5}

fruta1_d = {1:'Manzana', 2:'Platano', 3:'Naranja'}

def ejemplo1():
    print('RECORRER POR CLAVE')
    print('------------------')
    for clave in alumno_d:
        print(clave)


def ejemplo2():
    print('RECORRER POR VALOR')
    print('------------------')
    for clave in alumno_d:
        print(alumno_d[clave])


def ejemplo3():
    print('RECORRER POR TUPLAS')
    print('--------------------')
    alumno_di = alumno_d.items()
    print(alumno_di)
    for e in alumno_di:
        print(e)

def ejemplo4():
    print('RECORRER POR KEY-VALUE')
    print('----------------------')
    alumno_di = alumno_d.items()  # dic-item: lista de tuplas
    for clave, valor in alumno_di:
        print('%-10s %-3s %-10s' % (clave, ':', valor))

def ejemplo5():
    print('RECORRER POR KEY-VALUE')
    print('----------------------')
    fruta_di = fruta_d.items()  # dic-item: lista de tuplas
    for clave, valor in fruta_di:
        print('%-30s %-3s %-10s' % (clave, ':', valor))
    print()
    for clave, valor in fruta_di:
        print('%-10s %-10s %-3s %-10s' % (clave[0], clave[1], ':', valor))

def ejemplo6():
    print('RECORRER POR KEY-VALUE')
    print('----------------------')
    fruta1_di = fruta1_d.items()  # dic-item: lista de tuplas
    for clave, valor in fruta1_di:
        print('%-3s %-3s %-10s' % (clave, ':', valor))

def main():
    os.system("cls")
    ejemplo6()


if __name__ == "__main__":
    main()
