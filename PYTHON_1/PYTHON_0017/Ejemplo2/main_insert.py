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
       comprador_lst = ['Miguel','Lopez Lescano','2010-01-01']
       try:
            query = "INSERT INTO Comprador (nombre,apellidos,fecha_nacimiento) VALUES (%s, %s, %s)" 
            valores = (comprador_lst[0],comprador_lst[1],comprador_lst[2])                           # Query insert
            cursor = conexion.cursor()                                                               # Crear cursor
            cursor.execute(query,valores)                                                            # Ejecutar query. No producen resultado en el cursor
            conexion.commit()                                                                        # Confirmar los cambios de los datos en la base de datos
            
            print('FILAS AFECTADAS: ', cursor.rowcount)
            print('OK: INSERT')
       except:   
            print('ERROR: INSERT')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

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
       comprador_lst_lst = [
                             ['Miguel','Lopez Lescano','2010-01-01'],
                             ['Carlos','Roncal Alva','2009-02-15'],
                             ['Carla','Rodriguez Cuba','2008-03-20'],
                             ['Arturo','Rabanal Paredes','2011-04-21'],
                             ['Silvia','Vitteri Gonzalez','2007-05-05']
                           ]
       try:
            query = "INSERT INTO Comprador (nombre,apellidos,fecha_nacimiento) VALUES (%s, %s, %s)"  # Query insert
            cursor = conexion.cursor()                                                               # Crear cursor
            for comprador_lst in comprador_lst_lst:
                valores = (comprador_lst[0],comprador_lst[1],comprador_lst[2])                           
                cursor.execute(query,valores)                                                        # Ejecutar query. No producen resultado en el cursor

            conexion.commit()                                                                        # Confirmar los cambios de los datos en la base de datos    
            print('FILAS AFECTADAS: ', cursor.rowcount) 
            print('OK: INSERT')
       except:   
            print('ERROR: INSERT')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

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
       comprador_lst_lst = [
                             ['Miguel','Lopez Lescano','2010-01-01'],
                             ['Carlos','Roncal Alva','2009-02-15'],
                             ['Carla','Rodriguez Cuba','2008-03-20'],
                             ['Arturo','Rabanal Paredes','2011-04-21'],
                             ['Silvia','Vitteri Gonzalez','2007-05-05']
                           ]
       try:
            query = "INSERT INTO Comprador (nombre,apellidos,fecha_nacimiento) VALUES (%s, %s, %s)"  # Query insert
            cursor = conexion.cursor()                                                               # Crear cursor
            for comprador_lst in comprador_lst_lst:
                cursor.execute(query,comprador_lst)                                                  # Ejecutar query. No producen resultado en el cursor 

            conexion.commit()                                                                        # Confirmar los cambios de los datos en la base de datos    
            print('FILAS AFECTADAS: ', cursor.rowcount) 
            print('OK: INSERT') 
       except:   
            print('ERROR: INSERT')
       finally:
            cursor.close()
            conexion.close()
    else:
       print('ERROR: CONEXION')

def main():
    os.system("cls")
    ejemplo3()
          
if __name__ == "__main__":
   main()