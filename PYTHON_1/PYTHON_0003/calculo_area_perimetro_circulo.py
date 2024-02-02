import os, math

os.system('cls')

# ENTRADA
radio = float(input('Ingrese Radio? '))
# PROCESO
area = math.pi * math.pow(radio,2)
perimetro = 2 * math.pi * radio
# SALIDA
print('Radio    : ', radio)
print('Area     : ', round(area,2))
print('Perimetro: ', round(perimetro,2))