import os
import mysql.connector


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
            query = '''CREATE TABLE Comprador ( 
                          id_comprador      INT         NOT NULL AUTO_INCREMENT,
                          nombre            VARCHAR(25) NOT NULL,
                          apellidos         VARCHAR(50) NOT NULL,
                          fecha_nacimiento  DATE        NOT NULL,
                                            PRIMARY KEY (id_comprador)
                       ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4''' # Query create table
            cursor = conexion.cursor()                            # Crear cursor
            cursor.execute(query)                                 # Ejecutar query. No producen resultado en el cursor

            print('OK: CREATE TABLE')
       except:   
            print('ERROR: CREATE TABLE')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')


def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()





