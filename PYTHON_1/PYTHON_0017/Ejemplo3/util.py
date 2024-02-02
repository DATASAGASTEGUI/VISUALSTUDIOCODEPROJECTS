def cabecera():
    print('%8s  %-10s  %-25s  %-10s  %-10s' % ('IDALUMNO','NOMBRE','APELLIDOS','GRUPO','NACIMIENTO'))
    print('%8s  %-10s  %-25s  %-10s  %-10s' % ('--------','------','---------','-----','----------'))

def cuerpo(alumno_t):
    print('%8d  %-10s  %-25s  %-10s  %-10s' % (alumno_t[0],alumno_t[1],alumno_t[2],alumno_t[3],alumno_t[4]))

def mostrar_registro_1(alumnos_l):
    bandera = True
    try:
        cabecera()
        for alumno_t in alumnos_l:
            cuerpo(alumno_t)
    except:   
        bandera = False
    return bandera

def mostrar_registro_2(alumno_t):
    bandera = True
    try:
        cabecera()
        cuerpo(alumno_t)
    except:   
        bandera = False
    return bandera