import os

os.system('cls')

# ENTRADA
nota = int(input('Ingrese Nota? '))
# PROCESO
clasificacion = "Aprobado"
if nota < 5:
   clasificacion = "Desaprobado"
# SALIDA
print(clasificacion)
