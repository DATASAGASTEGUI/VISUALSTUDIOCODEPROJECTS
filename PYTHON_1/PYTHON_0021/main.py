import os

def ejemplo1():
    print("ITERAR SOBRE UNA LISTA")
    print("----------------------")
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(fruta)

def ejemplo2():
    print("ITERAR SOBRE UNA CADENA")
    print("-----------------------")
    mensaje = "Hola Mundo"
    for caracter in mensaje:
        print(caracter, end="  ")
    print()
    for caracter in mensaje:
        print(caracter, end=",")
    print()

def ejemplo3():
    print("ITERAR SOBRE UN SERIE DE NUMEROS")
    print("--------------------------------")
    for i in range(5):
        print(i, end=",")
    print()
    for i in range(5):
        print((i+1), end=",")
    print()

def ejemplo4():
    print("ITERAR SOBRE ELEMENTOS E INDICES DE UNA LISTA")
    print("---------------------------------------------")
    frutas = ["manzana", "banana", "cereza"]
    for i, fruta in enumerate(frutas): #Regresa un conjunto de tuplas (0,manzana)(1,banana),(2,cereza)
        print(f"Indice {i}: {fruta}")

def ejemplo5():
    print("ITERAR SOBRE UN DICCIONARIO")
    print("---------------------------")
    persona = {"nombre": "Juan", "edad": 25, "ciudad": "Ejemploville"}
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

def ejemplo6():
    print("ITERAR SOBRE UN RANGO DE NUMEROS")
    print("--------------------------------")
    for i in range(65,91): #[65,90]
        print(i, end=",")
    print()
    for i in range(65,91): #[65,90]
        print(chr(i), end=",")

def main():
    os.system("cls")
    ejemplo1()
    ejemplo2()
    ejemplo3()
    ejemplo4()
    ejemplo5()
    ejemplo6()
          
if __name__ == "__main__":
   main()