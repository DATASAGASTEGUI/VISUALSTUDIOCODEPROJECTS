import os
import mysql.connector

# ACTUALIZAR UN REGISTRO
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
       nombre_nuevo = 'Delly'
       id_comprador_actualizar = 4
       try:
            query = F"UPDATE Comprador SET nombre = '{nombre_nuevo}' WHERE id_comprador = {id_comprador_actualizar}"  # Query update  
            cursor = conexion.cursor()                                                                                # Crear cursor
            cursor.execute(query)                                                                                     # Ejecutar query. No producen resultado en el cursor
            conexion.commit()                                                                                         # Confirmar los cambios

            print('FILAS AFECTADAS: ', cursor.rowcount) 
            print('OK: UPDATE')
       except:   
            print('ERROR: UPDATE')
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