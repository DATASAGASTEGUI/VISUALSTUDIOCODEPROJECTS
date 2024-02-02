#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def formardiccionario(lista_key,lista_value):
    keys = lista_key[1:]
    values = lista_value[1:]
    diccionario = {}
    for k,v in zip(keys,values):
        diccionario[k] = v
    return diccionario

def solucion():
    datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    clientesL = datos_clientes.split('\n')
    diccionario_clientes = {}
    lista_key = clientesL[0].split(';')
    for i in range(1,len(clientesL)):
        lista_value = clientesL[i].split(';')
        diccionario = formardiccionario(lista_key,lista_value)
        diccionario_clientes[lista_value[0]] = diccionario
    print(diccionario_clientes)

def main():
    os.system("cls")
    solucion()
          
if __name__ == "__main__":
   main()