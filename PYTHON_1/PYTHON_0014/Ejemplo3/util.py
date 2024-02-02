def cabecera():
    print('%-8s  %-10s  %8s  %4s  %-6s' % ('IDALUMNO','NOMBRE','ESTATURA','EDAD','CASADO'))
    print('%-8s  %-10s  %8s  %4s  %-6s' % (pintarguiones('IDALUMNO'),pintarguiones('NOMBRE'),pintarguiones('ESTATURA'),pintarguiones('EDAD'),pintarguiones('CASADO')))

def cuerpo(alumno_d):
    print('%-8s  %-10s  %8.2f  %4d  %-6s' % (alumno_d['idAlumno'],alumno_d['nombre'],alumno_d['estatura'],alumno_d['edad'],alumno_d['casado']))

def pintarguiones(cadena):
    s = ''
    for i in range(len(cadena)):
        s = s + '-'
    return s