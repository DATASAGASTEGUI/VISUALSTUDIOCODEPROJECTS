#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def cabecera(elemento):
    cadena = elemento.upper()
    lista = cadena.split(';')
    print('%-10s  %-21s  %-25s  %-10s  %10s' % (lista[0],lista[1],lista[2],lista[3],lista[4]))
    print('%-10s  %-21s  %-25s  %-10s  %10s' % ('---','------','-----','--------','---------'))

def cuerpo(elemento):
    lista = elemento.split(';')
    print('%-10s  %-21s  %-25s  %-10s  %10.2f' % (lista[0],lista[1],lista[2],lista[3],float(lista[4])))
    
def solucion():
    datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    clientesL = datos_clientes.split('\n')
    cabecera(clientesL[0])
    for i in range(1,len(clientesL)):
        cuerpo(clientesL[i])

def main():
    os.system("cls")
    solucion()
          
if __name__ == "__main__":
   main()