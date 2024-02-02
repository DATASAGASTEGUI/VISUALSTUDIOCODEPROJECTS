import re

def numeroReal(mensaje): # 3434 o 234.24
    patron = '[0-9]+||[0-9]+\.[0-9]{1,2}'
    cadena = ''
    while True:
          cadena = input(mensaje)
          correcto = re.fullmatch(patron,cadena)
          if not correcto:
             print("ENTRADA INCORRECTA")
          else:
             break
    return float(cadena)