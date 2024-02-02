import os

os.system('cls')

# ENTRADA
nota = int(input('Ingrese Nota? '))
# PROCESO
if nota < 5:
   clasificacion = "Desaprobado"
else:
    clasificacion = "Aprobado" 
# SALIDA
print(clasificacion)
