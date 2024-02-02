import os

os.system('cls')

print("TIPO ENTERO")
print("-----------")

entero_decimal     = 10
entero_binario     = 0b1010 
entero_octal       = 0o12
entero_hexadecimal = 0xA

print('Tipo Dato: ', type(entero_decimal))
print('Tipo Dato: ', type(entero_binario))
print('Tipo Dato: ', type(entero_octal))
print('Tipo Dato: ', type(entero_hexadecimal))

print("Entero Decimal    : ",entero_decimal)
print("Entero Binario    : ",entero_binario)
print("Entero Octal      : ",entero_octal)
print("Entero Hexadecimal: ",entero_hexadecimal)

print("TIPO REAL")
print("---------")

real1 = 0.0000012345 # Notación Normal
real2 = 1.2345e-6    # Notación Científica

print('Tipo Dato 1: ', type(real1))
print('Tipo Dato 2: ', type(real2))

print("Punto Flotante: ", real1)
print("Punto Flotante: ", real2)

print("TIPO CADENA")
print("-----------")

cadena1 = "Hola Mundo"
cadena2 = 'Hola Mundo'    

print('Tipo Dato: ', type(cadena1))
print('Tipo Dato: ', type(cadena2))

print("Cadena 1: ", cadena1)
print("Cadena 2: ", cadena2)

print("TIPO LOGICO")
print("-----------")

logico1 = True
logico2 = False    

print('Tipo Dato: ', type(logico1))
print('Tipo Dato: ', type(logico2))

print("Logico 1: ", logico1)
print("Logico 2: ", logico2)

print("TIPO CARACTER")
print("-------------")

print("NO EXISTE EL TIPO CARACTER COMO EN JAVA CON CHAR\n\
EN PYTHON SERIA UNA CADENA  DE  UN SOLO CARACTER")


'''
TIPOS DE DATOS
--------------
int
float
str
bool
'''
