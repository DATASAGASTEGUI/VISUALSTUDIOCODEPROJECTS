
import os

def ejemplo1():
    print('FORMAS DISTINTAS COMO CREAR UN CONJUNTO')
    print('=======================================')
    print('(1) USANDO LLAVES')
    print('-----------------')
    # conjunto = {1,2,[3,4]} No es valido no puede haber otro conjunto dentro
    # conjunto = {1,2,{'a':1,'b':2}} No es valido no puede haber otro conjunto dentro
    conjunto1 = {1,2,'hola',1.73,False,'hola'} # False es 0, True es 1 
    print(conjunto1)
    conjunto2 = {'manzana', 'banana', 'cereza', 'manzana'}
    print(conjunto2)
    conjunto3 = {1,3,2,1,4,4,3}
    print(conjunto3)
    print('(1) USANDO LA FUNCION SET')
    print('-------------------------')
    #
    lista = [1,2,3,1]
    conjunto = set(lista)
    print(conjunto)
    #
    cadena = 'Hola Mundo'
    conjunto = set(cadena)
    print(conjunto)
    #
    tupla = (1,2,3,1)
    conjunto = set(tupla)
    print(conjunto)
    #
    diccionario = {'a':1, 'b':2}
    conjunto = set(diccionario)
    print(conjunto)

def ejemplo2():
    print('AGREGAR ELEMENTOS A UN CONJUNTO')
    print('===============================')
    conjunto = {1,2,3}
    conjunto.add(4)
    print(conjunto)

def ejemplo3():
    print('ELIMINAR ELEMENTOS DE UN CONJUNTO')
    print('=================================')
    #
    conjunto = {1,2,3}
    conjunto.remove(3)
    print(conjunto)
    #
    '''
    SI NO EXISTE DA ERROR
    conjunto = {1,2,3}
    conjunto.remove(4)
    print(conjunto) 
    ''' 
    #
    conjunto = {1,2,3}
    conjunto.discard(4) # No genera error por no encontrarlo
    print(conjunto)      

def ejemplo4():
    print('OPERACIONES COMUNES SOBRE CONJUNTOS')
    print('===================================')
    # CREAR CONJUNTOS
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {4, 5, 6, 7, 8}

    # UNION DE CONJUNTOS
    union_set = conjunto1.union(conjunto2)
    print("Unión:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

    # INTERSECCION DE CONJUNTOS
    intersection_set = conjunto1.intersection(conjunto2)
    print("Intersección:", intersection_set)  # Output: {4, 5}

    # DIFERENCIA DE CONJUNTOS
    difference_set = conjunto1.difference(conjunto2)
    print("Diferencia (conjunto1 - conjunto2):", difference_set)  # Output: {1, 2, 3}

    # DIFERENCIA SIMETRICA (ELEMENTOS QUE ESTAN EN UNO DE LOS CONJUNTOS PERO NO EN AMBOS
    symmetric_difference_set = conjunto1.symmetric_difference(conjunto2)
    print("Diferencia simétrica:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

    # Comprobación de subconjunto
    es_subconjunto = {1, 2}.issubset(conjunto1)
    print("{1, 2} es subconjunto de conjunto1:", es_subconjunto)  # Output: True

    # Comprobación de superconjunto
    es_superconjunto = conjunto1.issuperset({1, 2})
    print("conjunto1 es superconjunto de {1, 2}:", es_superconjunto)  # Output: True

    # Agregar elementos a un conjunto
    conjunto1.add(6)
    print("Conjunto1 después de agregar 6:", conjunto1)  # Output: {1, 2, 3, 4, 5, 6}

    # Eliminar elementos de un conjunto
    conjunto1.remove(3)
    print("Conjunto1 después de eliminar 3:", conjunto1)  # Output: {1, 2, 4, 5, 6}

def ejemplo5():
    numeros_lst = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8]
    conjunto_sin_duplicados = set(numeros_lst)
    lista_sin_duplicados = list(conjunto_sin_duplicados)
    print(lista_sin_duplicados)

def ejemplo6():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [3, 4, 5, 6, 7]
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    elementos_comunes = conjunto1.intersection(conjunto2)
    print(elementos_comunes)

def ejemplo7():
    cadena = "programacion"
    conjunto_caracteres = set(cadena)
    cadena_sin_duplicados = ''.join(conjunto_caracteres)
    print(cadena_sin_duplicados)

def ejemplo8():
    cadena1 = "listen"
    cadena2 = "silent"
    conjunto1 = set(cadena1)
    conjunto2 = set(cadena2)
    es_anagrama = conjunto1 == conjunto2
    print("¿Son anagramas?", es_anagrama)

def ejemplo9():
    pass

def ejemplo10():
    pass

def main():
    os.system("cls")
    #ejemplo1()
    #ejemplo2()
    #ejemplo3()
    #ejemplo4()
    #ejemplo5()
    #ejemplo6()
    #ejemplo7()
    ejemplo8()
    #ejemplo9()
    #ejemplo10()
          
if __name__ == "__main__":
   main()

'''
--------------------------------------------------------------------------------
EJERCICIO 1: ELIMINACIÓN DE DUPLICADOS EN UNA LISTA (EJEMPLO5)
Dada una lista de números, crea un conjunto a partir de la  lista  para eliminar
los duplicados y luego imprime la lista sin duplicados.

EJERCICIO 2: COMPROBACIÓN DE ELEMENTOS COMUNES (EJEMPLO6)
Dadas   dos   listas,  encuentra  e  imprime  los  elementos comunes entre ellas
utilizando conjuntos.

EJERCICIO 3: ELIMINACIÓN DE ELEMENTOS DUPLICADOS EN UNA CADENA (EJEMPLO7)
Dada una cadena, crea un conjunto a partir de los caracteres de la  cadena  para
eliminar los caracteres duplicados y luego imprime la cadena sin duplicados.

EJERCICIO 4: VERIFICACIÓN DE ANAGRAMAS (EJEMPLO8)
Dadas dos cadenas, verifica si son anagramas (contienen  los  mismos  caracteres
pero en diferente orden) utilizando conjuntos.
--------------------------------------------------------------------------------
'''