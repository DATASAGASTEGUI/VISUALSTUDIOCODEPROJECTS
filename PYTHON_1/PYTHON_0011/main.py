import os

def ejemplo1():
    print('FORMAS DE CREAR UNA TUPLA')
    print('=========================')
    print('(1) USANDO PARENTESIS')
    print('---------------------')
    tupla = (1, 2, 3)
    print(tupla)
    print('(2) USANDO LA FUNCION TUPLE()')
    print('-----------------------------')
    lista = [1, 2, 3]
    tupla = tuple(lista)
    print(tupla)
    print('(3) USANDO LA TUPLA VACIA')
    print('-------------------------')
    tupla = ()
    print(tupla)
    print('(4) USANDO LA TUPLA DE UN SOLO ELEMENTO')
    print('---------------------------------------')
    tupla = (1,)
    print(tupla)
    print('(5) EMPAQUETADO DE TUPLAS') #  Puedes crear una tupla mediante el empaquetado, que es cuando agrupas varios valores separados por comas.
    print('-------------------------')
    tupla = 8, 9, 'diez'
    print(tupla)
    print('(6) DESEMPAQUETADO DE TUPLAS') #  Puedes crear una tupla y asignar sus elementos a variables individuales al mismo tiempo.
    print('----------------------------')
    a, b, c = 11, 12, 13
    tupla = a, b, c
    print(tupla)

def obtener_coordenadas():
    latitud = 40.7128
    longitud = -74.0060
    return latitud, longitud

def obtener_nombre_y_edad():
    return 'Juan', 25

def obtener_informacion_persona(nombre, edad, ciudad):
    return nombre, edad, ciudad

def ejemplo2():
    print('FUNCION QUE DEVUELVE TUPLAS')
    print('===========================')
    print('(1) FUNCIONES QUE DEVUELVEN MULTIPLES VALORES')
    print('---------------------------------------------')
    coordenadas = obtener_coordenadas()
    print(coordenadas)  # Imprime (40.7128, -74.0060)
    print('(2) DESCOMPOSICION DE UNA TUPLA EN VARIABLES')
    print('--------------------------------------------')
    nombre, edad = obtener_nombre_y_edad()
    print(nombre)  # Imprime 'Juan'
    print(edad)    # Imprime 25
    nombre, edad = ('Miguel',23)
    print(nombre)  # Imprime 'Juan'
    print(edad)    # Imprime 25
    print('(3) USANDO TUPLAS COMO ARGUMENTOS EN FUNCIONES') #  Puedes crear una tupla al pasar varios valores como argumentos a una función.
    print('----------------------------------------------')
    tupla = divmod(20, 3)  # Retorna (6, 2)
    print(tupla)
    print('(4) FUNCIONES QUE DEVUELVEN TUPLAS PERSONALIZADAS')
    print('-------------------------------------------------')
    informacion = obtener_informacion_persona('Ana', 30, 'Madrid')
    print(informacion)  # Imprime ('Ana', 30, 'Madrid')

def ejemplo3():
    print('OPERACIONES SOBRE UNA TUPLA')
    print('===========================')
    print('(1) INDEXACION Y SEGMENTACION')
    print('-----------------------------')
    tupla = (1, 2, 3, 'cuatro', 5.0)
    print(tupla[0])     # Imprime 1                    Acceder a elementos individuales mediante índices.
    print(tupla[1:4])   # Imprime (2, 3, 'cuatro')     Realizar segmentación para obtener subconjuntos de la tupla.
    print('(2) CONCATENACION') # Unir dos tuplas para crear una nueva tupla.
    print('-----------------')
    tupla1 = (1, 2, 3)
    tupla2 = ('cuatro', 'cinco')
    nueva_tupla = tupla1 + tupla2
    print(nueva_tupla)  # Imprime (1, 2, 3, 'cuatro', 'cinco')
    print('(3) REPETICION') # Repetir una tupla varias veces.
    print('--------------')
    tupla_original = (1, 2, 3)
    tupla_repetida = tupla_original * 2
    print(tupla_repetida)  # Imprime (1, 2, 3, 1, 2, 3)
    print('(4) LONGITUD DE LA TUPLA')
    print('------------------------')
    tupla = (1, 2, 3, 'cuatro', 5.0)
    print(len(tupla))  # Imprime 5
    print('(5) COMPROBACION DE PERTENENCIA') # Verificar si un elemento está presente en la tupla.
    print('-------------------------------')
    tupla = (1, 2, 3, 'cuatro', 5.0)
    print('cuatro' in tupla)  # Imprime True
    print('(6) ITERACION') # Iterar sobre los elementos de la tupla utilizando bucles.
    print('-------------')
    tupla = (1, 2, 3, 'cuatro', 5.0)
    for elemento in tupla:
        print(elemento)
    print('(7) DESEMPAQUETADO DE TUPLA') # Asignar los elementos de una tupla a variables individuales.
    print('---------------------------')
    coordenadas = (40.7128, -74.0060)
    latitud, longitud = coordenadas
    print(latitud)   # Imprime 40.7128
    print(longitud)  # Imprime -74.0060

def ejemplo4():
    pass

def ejemplo5():
    pass

def ejemplo6():
    pass

def ejemplo7():
    pass

def ejemplo8():
    pass

def ejemplo9():
    pass

def ejemplo10():
    pass

def ejemplo11():
    pass

def main():
    os.system("cls")
    #ejemplo1()
    #ejemplo2()
    ejemplo3()
    #ejemplo4()
    #ejemplo5()
    #ejemplo6()
    #ejemplo7()
    #ejemplo8()
    #ejemplo9()
    #ejemplo10()
    #ejemplo11()

if __name__ == "__main__":
   main()