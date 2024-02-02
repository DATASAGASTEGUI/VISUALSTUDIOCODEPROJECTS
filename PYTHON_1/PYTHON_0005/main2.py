import os

os.system('cls')
a = 0
while True:
    numero = int(input('Ingrese número entero positivo? ')) #Negativo termina
    if numero < 0:
       break
    else:
       a = a + numero

print('Suma : ', a)