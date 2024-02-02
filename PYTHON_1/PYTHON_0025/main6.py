import os
from entrada import numeroReal

def case1():
    n1 = numeroReal('INGRESE NUMERO 1 ? ')
    n2 = numeroReal('INGRESE NUMERO 2 ? ')
    suma = n1 + n2
    print("SUMA: ", suma)

def case2():
    n1 = numeroReal('INGRESE NUMERO 1 ? ')
    n2 = numeroReal('INGRESE NUMERO 2 ? ')
    resta = n1 - n2
    print("RESTA: ", resta)

def case3():
    n1 = numeroReal('INGRESE NUMERO 1 ? ')
    n2 = numeroReal('INGRESE NUMERO 2 ? ')
    multiplicacion = n1 * n2
    print("MULTIPLICACION: ", multiplicacion)

def case4():
    n1 = numeroReal('INGRESE NUMERADOR ? ')
    n2 = numeroReal('INGRESE DENOMINADOR ? ')
    if n2 != 0:
       division = n1 / n2
       print("DIVISION: ", division)
    else:
       print("DIVISION ENTRE CERO")
    

def case5():
    n1 = numeroReal('INGRESE BASE ? ')
    n2 = numeroReal('INGRESE EXPONENTE ? ')
    potencia = n1 ** n2
    print("POTENCIA: ", potencia)

def default():
    print("OPERACION NO EXISTE")

switch_dic = {
    '+':  case1,
    '-':  case2,
    '*':  case3,
    '/':  case4,
    '**': case5
}

'''
def switch_case(operando_clave):
    funcion_case = switch_dic.get(operando_clave, default)
    return funcion_case
'''

def main():
    os.system("cls")
    clave = input('INGRESE OPERACION (+ - * / **)? ')
    funcion_case = switch_dic.get(clave, default)
    funcion_case()
          
if __name__ == "__main__":
   main()