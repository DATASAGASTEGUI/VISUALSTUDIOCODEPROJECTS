import os

os.system('cls')

diccionario = {}
diccionario['idAlumno'] = 'A1'
diccionario['nombre'] = 'Miguel'
diccionario['edad'] = 45
diccionario['estatura'] = 1.72
diccionario['casado'] = True
diccionario['jobis_lst'] = ['Ajedrez', 'Lectura']
diccionario['direccion_dic'] = {
    'calle': 'Av. Ejercito 123',
    'ciudad': 'Madrid',
    'pais': 'España',
    'codigo_postal': 28032
}
diccionario['pais_nacimiento'] = ('Perú')

print(diccionario)

diccionario['pais_nacimiento'] = ('Canada')

print(diccionario)

