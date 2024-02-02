import os, json

def ejemplo1():
    jsonAlumnoComillaSimple = {
                                'idAlumno': 'A1',
                                'nombre': 'Miguel',
                                'apaterno': 'Roncal',
                                'edad': 28,
                                'estatura': 1.72,
                                'casado': False,
                                'jobis_lst': ['Ajedrez','Cine'],
                                'direccion': {
                                    'calle': 'Av. Ejercico 123',
                                    'ciudad': 'Madrid',
                                    'pais': 'España',
                                    'cp': 28067
                                }
                              }
    jsonAlumnoComillaDoble = json.dumps(jsonAlumnoComillaSimple) #Poner comillas doble en lugar de comillas simple
    print(jsonAlumnoComillaDoble)

    jsonAlumnoComillaSimple = json.loads(jsonAlumnoComillaDoble)
    print(jsonAlumnoComillaSimple)


def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()