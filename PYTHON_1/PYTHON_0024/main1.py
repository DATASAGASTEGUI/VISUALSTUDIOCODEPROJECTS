import os

def switch_case(valor):
 if valor == 1:
    return "Caso 1"
 elif valor == 2:
    return "Caso 2"
 elif valor == 3:
    return "Caso 3"
 else:
    return "Caso por defecto"

def main():
    os.system("cls")
    valor = int(input("Ingrese caso (1,2,3,4)? "))
    print('Resultado: ', switch_case(valor))
    
if __name__ == "__main__":
   main()