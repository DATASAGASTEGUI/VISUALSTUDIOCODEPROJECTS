import mysql.connector

def get_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        database="tienda")
    except:
        conexion = None
    return conexion

    