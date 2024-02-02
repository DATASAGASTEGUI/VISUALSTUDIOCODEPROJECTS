import os

os.system('cls')

# ENTRADA
a = 5
b = '6'
# PROCESO - SALIDA
if isinstance(a,int) and isinstance(b,int):
   suma = a + b
   print('Suma: ', suma)
else:
   print("NO SE PUEDEN SUMAR")

print("Tipo a: ", type(a))
print("Tipo b: ", type(b))