import os
import mysql.connector


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
       try:
            query = 'SELECT * FROM Comprador'    # Query create table
            cursor = conexion.cursor()           # Crear cursor
            cursor.execute(query)                # Ejecutar query. Resultado en el cursor
            comprador_lst = cursor.fetchall()    # Recuperar todos los resultados guardado en el cursor

            print(comprador_lst)
            print('OK: SELECT')
       except:   
            print('ERROR: SELECT')
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