import os

def ejemplo1():
    print('DIVISION ENTERA')
    print('---------------')
    x = 5 // 3
    print("División Entera: ", x)
    print("Tipos Dato     : ", type(x))

def ejemplo2():
    print('DIVISION REAL')
    print('-------------')
    x = 5 / 3
    print("División Real: ", x)
    print("Tipos Dato   : ", type(x))

def ejemplo3():
    print('POTENCIA')
    print('--------')
    x1 = 2 ** 3
    print("Pontencia 1: ", x1)
    x2 = 2 ** 0.5
    print("Pontencia 2: ", x2)

def ejemplo4():
    print('DIVISION MODULAR')
    print('----------------')
    x1 = 5 % 3
    print("Resto: ", x1)
    x2 = 4 % 2
    print("Resto: ", x2)

def main():
    os.system("cls")
    ejemplo1()
    ejemplo2()
    ejemplo3()
    ejemplo4()
          
if __name__ == "__main__":
   main()