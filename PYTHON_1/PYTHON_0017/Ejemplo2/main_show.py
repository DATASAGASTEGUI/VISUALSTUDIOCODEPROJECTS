import os
import mysql.connector

# MOSTRAR SOLO UNA TABLA LA CUAL SE BUSCA EN LA BASE DE DATOS
def ejemplo1():
    conexion = None
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="12345678",
        database="test0001")
    except:
        conexion = None

    if conexion != None:
       print('OK: CONEXION')
       nombre_tabla = 'Comprador'
       try:
            query = f"SHOW TABLES LIKE '{nombre_tabla}'"    # Query show
            cursor = conexion.cursor()                      # Crear cursor
            cursor.execute(query)                           # Ejecutar query. Resultado guardar en el cursor
            tablas_lst_tup = cursor.fetchall()                  # Recuperar todos los resultados guardado en el cursor

            print(tablas_lst_tup)
            print('OK: SHOW')
       except:   
            print('ERROR: SHOW')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

# VERIFICAR SI UNA TABLA EXISTE EN LA BASE DE DATOS
def ejemplo2():
    conexion = None
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="12345678",
        database="test0001")
    except:
        conexion = None

    if conexion != None:
       print('OK: CONEXION')
       nombre_tabla = 'Comprador1'
       try:
            query = f"SHOW TABLES LIKE '{nombre_tabla}'"    # Query show
            cursor = conexion.cursor()                      # Crear cursor
            cursor.execute(query)                           # Ejecutar query. Resultado guardar en el cursor
            tablas_lst_tup = cursor.fetchall()              # Recuperar todos los resultados guardados en el cursor

            if tablas_lst_tup:
               print('SI EXISTE')
            else:
               print('NO EXISTE')

            print('OK: SHOW')
       except:   
            print('ERROR: SHOW')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

# MOSTRAR TODAS LAS TABLAS DE UNA BASE DE DATOS
def ejemplo3():
    conexion = None
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="12345678",
        database="test0001")
    except:
        conexion = None

    if conexion != None:
       print('OK: CONEXION')
       try:
            query = "SHOW TABLES"              # Query show
            cursor = conexion.cursor()         # Crear cursor
            cursor.execute(query)              # Ejecutar query. Resultado guardar en el cursor
            tablas_lst_tup = cursor.fetchall() # Recuperar todos los resultados guardado en el cursor

            if tablas_lst_tup:
               for tabla_tup in tablas_lst_tup:
                   print(tabla_tup[0])
            else:
                print('BASE DE DATOS SIN NINGUNA TABLA')

            print('OK: SHOW')
       except:   
            print('ERROR: SHOW')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

# MOSTRAR EN UN LISTADO TODAS LAS BASES DE DATOS QUE EXISTEN
def ejemplo4():
    conexion = None
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="12345678",
        database="test0001")
    except:
        conexion = None

    if conexion != None:
       print('OK: CONEXION')
       nombre_tabla = 'Comprador'
       try:
            query = 'SHOW DATABASES'                # Query show
            cursor = conexion.cursor()              # Crear cursor
            cursor.execute(query)                   # Ejecutar query. Resultado guardar en el cursor
            basesdatos_lst_tup = cursor.fetchall()  # Recuperar todos los resultados guardado en el cursor

            if basesdatos_lst_tup:
               for basedato_tup in basesdatos_lst_tup:
                   print(basedato_tup[0])
            else:
                print('BASE DE DATOS SIN NINGUNA TABLA')

            print('OK: SHOW')
       except:   
            print('ERROR: SHOW')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

def main():
    os.system("cls")
    #ejemplo1()
    #ejemplo2()
    #ejemplo3()
    ejemplo4()
          
if __name__ == "__main__":
   main()