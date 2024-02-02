from util import cabecera, cuerpo


def crear_tabla(conexion):
    bandera = True
    try:
       sql = '''CREATE TABLE Alumno ( 
                    idAlumno          INT         NOT NULL AUTO_INCREMENT,
                    nombre            VARCHAR(25) NOT NULL,
                    apellidos         VARCHAR(50) NOT NULL,
                    grupo             VARCHAR(50) NOT NULL,
                    fecha_nacimiento  DATE        NOT NULL,
                                      PRIMARY KEY (idAlumno)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4''' # Sentencia sql crear tabla
       cursor = conexion.cursor()                           # Crear el cursor
       cursor.execute(sql)                                  # Ejecutar la sentencia sql
       conexion.commit()                                    # Confirmar los cambios
    except:
        bandera = False
    return bandera

def existe_tabla(tabla, conexion):
    bandera = True
    try:
        sql = f'SELECT * FROM {tabla}'
        cursor = conexion.cursor()
        cursor.execute(sql)
        alumnos_l = cursor.fetchall()
        conexion.commit()
    except:   
        bandera = False
    return bandera

def insertar_registro(alumno_t,conexion):
    bandera = True
    try:
        sql = "INSERT INTO Alumno (nombre, apellidos, grupo, fecha_nacimiento) VALUES (%s, %s, %s, %s)"
        valores = (alumno_t[0],alumno_t[1],alumno_t[2],alumno_t[3])
        cursor = conexion.cursor()
        cursor.execute(sql,valores)
        conexion.commit()
    except: 
        bandera = False
    return bandera

def obtener_registro(conexion):
    retorno_l = []
    alumnos_l = []
    bandera = True
    try:
        sql = 'SELECT * FROM Alumno'
        cursor = conexion.cursor()
        cursor.execute(sql)
        alumnos_l = cursor.fetchall()
        conexion.commit()
    except:   
        bandera = False
    retorno_l.append(bandera)
    retorno_l.append(alumnos_l)
    return retorno_l

def eliminar_registro(idAlumnoEliminar,conexion):
    bandera = True
    try:
        sql = F"DELETE FROM Alumno WHERE idAlumno = {idAlumnoEliminar}"
        cursor = conexion.cursor()
        cursor.execute(sql)
    except:   
        bandera = False
    return bandera

def eliminar_todos_registros(conexion):
    bandera = True
    try:
        sql = "DELETE FROM Alumno"
        cursor = conexion.cursor()
        cursor.execute(sql)
    except:   
        bandera = False
    return bandera

def buscar_registro(idAlumnoBuscar,conexion):
    alumno_t = ()
    try:
        sql = f"SELECT * FROM Alumno WHERE idAlumno = {idAlumnoBuscar}"  
        cursor = conexion.cursor()
        cursor.execute(sql)
        alumno_t = cursor.fetchone()
        conexion.commit()
    except:
        alumno_t = None
    return alumno_t

def actualizar_registro(idAlumnoActualizar,nombre_nuevo,conexion):
    bandera = True
    try:
        sql = "UPDATE Alumno SET nombre = ? WHERE idAlumno = ?"
        valores = (nombre_nuevo, idAlumnoActualizar)
        cursor = conexion.cursor()
        cursor.execute(sql,valores)
    except:   
        bandera = False
    return bandera




















def existe_tabla_1(tabla, conexion):
    bandera = False
    try:
        sql = 'SHOW TABLES LIKE %s',(tabla,)
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros_l = cursor.fetchone()
        if registros_l:
           bandera = True
    except:   
        bandera = False
    return bandera





    inserts_l = ["INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Carlos',5,1.70,'2000-01-15',true)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Miguel',10,1.65,'1999-02-20',false)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('María',7,1.60,'2000-04-10',true)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('José',8,1.65,'2005-03-23',false)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Alicia',6,1.72,'1972-01-10',true)",
                 "INSERT INTO Alumno (nombre,nota,estatura,fecha_nacimiento,casado) VALUES ('Angel',7,1.71,'2000-01-10',true)"]
    
    nra = 'PYTHON_0015\\Ejemplo1\\instituto.db'
    conexion = sqlite3.connect(nra)
    cursor = conexion.cursor()
    for insert in inserts_l:
        cursor.execute(insert)
    conexion.commit()
    conexion.close()
    print("OK: INSERTAR REGISTRO")
