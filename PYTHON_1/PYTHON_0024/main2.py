import os

# FUNCION ASOCIADA A CADA CASO
def caso_1():
    return "Caso 1"

def caso_2():
    return "Caso 2"

def caso_3():
    return "Caso 3"

def caso_por_defecto():
    return "Caso por defecto"

# DICCIONARIO CON CLAVES Y FUNCIONES ASOCIADAS
switch_dict = {
    1: caso_1,
    2: caso_2,
    3: caso_3,
}

def main():
    os.system("cls")
    valor = int(input("Ingrese caso (1,2,3,4)? "))
    if(valor == 1 or valor == 2 or valor == 3):
       funcion = switch_dict.get(valor)() 
    else:
       funcion = caso_por_defecto()
    print('Resultado: ', funcion)
          
if __name__ == "__main__":
   main()