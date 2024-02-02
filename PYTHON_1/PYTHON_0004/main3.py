import os

os.system('cls')

edad = 18

cadena1 = "Mayor Edad" if edad >= 18 else "Menor Edad"
print("Cadena 1: ", cadena1)

numero1 = 1 if edad >= 18 else 0
print("Numero 1: ", numero1)

cadena2 = "Evaluar: " + "Mayor Edad" if edad >= 18 else "Menor Edad"
print("Cadema 2: ", cadena2)

cadena3 = "Evaluar: " + "1" if edad >= 18 else "0"
print("Cadema 3: ", cadena3)

cadena4 = "Evaluar: " + str(1 if edad >= 18 else 0)
print("Cadema 4: ", cadena4)

print("Numero 2: ", 1 if edad >= 18 else 0)
print("Cadena 5: ", "1" if edad >= 18 else "0")

