import os
import mysql.connector

# ALTERAR LA TABLA PARA AÑADIR UNA NUEVA COLUMNA
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
       nombre_columna = 'fecha_nacimiento'
       tipo_columna = 'DATE'
       try:
            query = F"ALTER TABLE {nombre_tabla} ADD COLUMN {nombre_columna} {tipo_columna}" # Query alter table
            cursor = conexion.cursor()                                                       # Crear cursor
            cursor.execute(query)                                                            # Ejecutar query. No producen resultado en el cursor
            conexion.commit()                                                                # Confirmar los cambios

            print('OK: ALTER TABLE')
       except:   
            print('ERROR: ALTER TABLE')
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