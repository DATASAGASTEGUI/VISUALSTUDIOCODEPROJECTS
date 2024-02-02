import os
import mysql.connector

# ELIMINAR SOLO UN REGISTRO DE LA TABLA
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
       id_comprador = 5
       try:
            query = F"DELETE FROM Comprador WHERE id_comprador = {id_comprador}" # Query delete (eliminar todos los registros de la tabla)
            cursor = conexion.cursor()                                           # Crear cursor
            cursor.execute(query)                                                # Ejecutar query. No producen resultado en el cursor
            conexion.commit()                                                    # Confirmar los cambios

            print('FILAS AFECTADAS: ', cursor.rowcount) 
            print('OK: DELETE')
       except:   
            print('ERROR: DELETE')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

# ELIMINAR TODOS LOS REGISTROS DE UNA TABLA
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
       try:
            query = "TRUNCATE TABLE Comprador" # Query truncate table (eliminar todos los registros de la tabla)
            cursor = conexion.cursor()         # Crear cursor
            cursor.execute(query)              # Ejecutar query. No producen resultado en el cursor
            conexion.commit()                  # Confirmar los cambios

            print('FILAS AFECTADAS: ', cursor.rowcount) 
            print('OK: TRUNCATE TABLE')
       except:   
            print('ERROR: TRUNCATE TABLE')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')


def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()