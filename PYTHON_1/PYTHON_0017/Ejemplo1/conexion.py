import os, mysql.connector

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
    else:
       print('ERROR: CONEXION')

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()