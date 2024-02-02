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
            query = 'SELECT * FROM Cliente'    # Query create table
            cursor = conexion.cursor()         # Crear cursor
            cursor.execute(query)              # Ejecutar query. Resultado en el cursor
            clientes_lst = cursor.fetchall()   # Recuperar todos los resultados guardado en el cursor

            print(clientes_lst)
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

'''
DESCARGAR EL DRIVER DE LA CONEXION DE PYTHON CON MYSQL

pip install mysql-connector-python

ACTUALIZAR EL GESTOR DE PAQUETES DE PYTHON
python.exe -m pip install --upgrade pip

[
    (1, 'Juan', 25, Decimal('50000.00'), 3), 
    (2, 'María', 30, Decimal('75000.00'), 5), 
    (3, 'Pedro', 22, Decimal('40000.00'), 2), 
    (4, 'Ana', 35, Decimal('90000.00'), 7), 
    (5, 'Luis', 28, Decimal('60000.00'), 2), 
    (6, 'Juan', 25, Decimal('60000.00'), 1), 
    (7, 'Ana', 25, Decimal('90000.00'), 7), 
    (8, 'Ismael', 28, Decimal('75000.00'), 2), 
    (9, 'María', 30, Decimal('40000.00'), 2), 
    (10, 'Liz', 30, Decimal('50000.00'), 5)
]
'''