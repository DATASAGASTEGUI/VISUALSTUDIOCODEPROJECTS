from util import cabecera, cuerpo

def mostrar(alumnos_l):
    cabecera()
    for alumno_d in alumnos_l:
        cuerpo(alumno_d)

def buscar(idAlumno,alumnos_l):
    alumnobuscar_d = {}
    for alumno_d in alumnos_l:
        if alumno_d['idAlumno'] == idAlumno:
           alumnobuscar_d = alumno_d
           break
    return alumnobuscar_d

def eliminar(idAlumno,alumnos_l):
    bandera = False
    for indice,alumno_d in enumerate(alumnos_l):
        if alumno_d['idAlumno'] == idAlumno:
           del alumnos_l[indice]
           bandera = True
           break
    return bandera  