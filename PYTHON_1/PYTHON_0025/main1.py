import os

# CREAR UN DICCIONARIO
alumno_dic = {}
# AGREGAR ELEMENTOS AL DICCIONARIO
alumno_dic['idAlumno'] = 'A01'
alumno_dic['nombre'] = 'Arturo'
alumno_dic['apaterno'] = 'Roncal'
alumno_dic['edad'] = 23
alumno_dic['estatura'] = 1.72
alumno_dic['esCasado'] = False
alumno_dic['jobis_lst'] = ['Ajedrez', 'Lectura']
alumno_dic['direccion_dic'] = {
                                'calle': 'Thomas Edison 123',
                                'pais': 'España',
                                'ciudad': 'Madrid',
                                'cp': 28034
                              }

def ejemplo1():
    print('OBTENER LAS CLAVES DEL DICCIONARIO')
    print('----------------------------------')
    claves = alumno_dic.keys()
    print('TIPO DATO: ', type(claves)) # <class 'dict_keys'>
    print("CLAVES   : ", list(claves))
    print("CLAVES   : ", claves)
    
    for clave in list(claves):
        print(clave, end='  ')


def ejemplo2():
    print('OBTENER LOS VALORES DEL DICCIONARIO')
    print('-----------------------------------')
    valores = alumno_dic.values()
    print('TIPO DATO: ', type(valores)) # <class 'dict_values'>
    print("VALORES  : ", list(valores))
    print("VALORES  : ", valores)

    for valor in list(valores):
        print(valor, end='  ')

def ejemplo3():
    print('OBTENER PARES CLAVE-VALOR COMO TUPLAS')
    print('-------------------------------------')
    tuplas = alumno_dic.items()
    print('TIPO DATO: ', type(tuplas)) # <class 'dict_items'>
    print("TUPLAS   : ", list(tuplas))
    print("TUPLAS   : ", tuplas)
    
    for tupla in list(tuplas):
        print(tupla, end='  ')
    print()

    print("%-20s %-10s" % ('CLAVE', 'VALOR'))
    print("%-20s %-10s" % ('-----', '-----'))
    for tupla in list(tuplas):
        print("%-20s %-10s" % (tupla[0], tupla[1]))

def ejemplo4():
    print('RECORRER POR LA CLAVE')
    print('---------------------')
    claves = alumno_dic.keys()
    print("%-20s %-10s" % ('CLAVE', 'VALOR'))
    print("%-20s %-10s" % ('-----', '-----'))
    for clave in list(claves):
        print("%-20s %-10s" % (clave, alumno_dic[clave]))

def ejemplo5():
    print('BUSCAR POR LA CLAVE')
    print('-------------------')
    clave = 'direccion_dic' 

    valor1 = alumno_dic[clave] # Peor. Si la clave no existe genera un error  
    print(clave,':',valor1)
    
    valor2 = alumno_dic.get(clave) # Mejor. Si la clave no existe genera un None  
    print(clave,':',valor2)

    clave = 'amaterno' 
    valor3 = alumno_dic.get(clave, 'NO EXISTE') 
    print(clave,':',valor3)

def ejemplo6():
    print('AGREGAR UN NUEVO PAR CLAVE-VALOR')
    print('--------------------------------')
    alumno_dic['amaterno'] = 'Ruiz'
    print(alumno_dic) 

def ejemplo7():
    print('ELIMINAR UN ELEMENTO POR CLAVE')
    print('------------------------------') 
    del alumno_dic['amaterno']
    print(alumno_dic) 

def ejemplo8():
    print('VERIFICAR SI UNA CLAVE EXISTE')
    print('-----------------------------') 
    if 'apaterno' in alumno_dic:
       print('LA CLAVE EXISTE')
    else:
       print("LA CLAVE NO EXISTE")

def ejemplo9():
    print('MODIFICAR UN VALOR')
    print('------------------') 
    alumno_dic['apaterno'] = 'Lescano'
    print(alumno_dic)

def ejemplo10():
    print('COPIAR UN DICCIONARIO: MODIFICAR ORIGIAL MODIFICA LA COPIA')
    print('----------------------------------------------------------') 
    print('ANTES')
    print('-----')
    estudiante_dic = alumno_dic
    print('ALUMNO_DIC    : ', alumno_dic)
    print('ESTUDIANTE_DIC: ', estudiante_dic)
    print('DESPUES')
    print('-------')
    alumno_dic['nombre'] = 'Ramon'
    print('ALUMNO_DIC    : ', alumno_dic)
    print('ESTUDIANTE_DIC: ', estudiante_dic)

def ejemplo11():
    print('LIMPIAR UN DICCIONARIO')
    print('----------------------') 
    alumno_dic.clear()
    print('ALUMNO_DIC: ', alumno_dic)

def ejemplo12():
    print('ACTUALIZAR UN DICCIONARIO')
    print('-------------------------') 
    '''
    alumno1_dic = alumno_dic # Si modifico cualquiera de ellos se refleja en todas
    '''
    
    alumno1_dic = alumno_dic.copy() # En este caso, la modificación en la copia no afecta al diccionario original.
    alumno2_dic = alumno_dic.copy()
    alumno3_dic = alumno_dic.copy()
    alumno4_dic = alumno_dic.copy()

    print('EJEMPLO 1')
    print('---------')
    nuevo_dic = {'apaterno': 'Ismael', 'estatura': 1.61}
    alumno1_dic.update(nuevo_dic)
    print(alumno1_dic)

    print('EJEMPLO 2')
    print('---------')
    nuevo_dic = {'apaterno': 'Ismael', 'direccion_dic': {'pais': 'Portugal'}} # Elimina el diccionario direccion y lo remplaza por este no quiero eso
    alumno2_dic.update(nuevo_dic)
    print(alumno2_dic)
    
    print('EJEMPLO 3')
    print('---------')
    aux_dic = alumno3_dic.get('direccion_dic')
    nuevo_dic = {'ciudad': 'Barcelona'}
    aux_dic.update(nuevo_dic)
    print(aux_dic)
    alumno3_dic.update(aux_dic) # No funciona
    print(alumno3_dic)

    print('EJEMPLO 4')
    print('---------')
    aux_dic = alumno4_dic.get('direccion_dic')
    nuevo_dic = {'ciudad': 'Barcelona'}
    aux_dic.update(nuevo_dic)
    print(aux_dic)
    alumno4_dic['direccion_dic'] = aux_dic # Si funciona
    print(alumno4_dic)

def ejemplo13():
    print('COPIAR UN DICCIONARIO: MODIFICAR ORIGIAL NO MODIFICA LA COPIA')
    print('-------------------------------------------------------------') 
    print('ANTES')
    print('-----')
    # estudiante_dic = alumno_dic.copy() # Usando el método copy()
    # estudiante_dic = dict(alumno_dic) # Usando el constructor dict()
    estudiante_dic = {**alumno_dic} # Usando método de desempaquetado **
    print('ALUMNO_DIC    : ', alumno_dic)
    print('ESTUDIANTE_DIC: ', estudiante_dic)
    print('DESPUES: MODIFICO ORIGINAL')
    print('--------------------------')
    alumno_dic['nombre'] = 'Ramon'
    print('ALUMNO_DIC    : ', alumno_dic)
    print('ESTUDIANTE_DIC: ', estudiante_dic)

def main():
    os.system('cls')
    # ejemplo1()
    # ejemplo2()
    # ejemplo3()
    # ejemplo4()
    # ejemplo5()
    # ejemplo6()
    # ejemplo6(); ejemplo7()
    # ejemplo8()
    # ejemplo9()
    # ejemplo10()
    # ejemplo11()
    # ejemplo12()
    ejemplo13()
          
if __name__ == "__main__":
   main()