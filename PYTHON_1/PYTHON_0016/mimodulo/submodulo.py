def saludar():
    print("¡Hola desde el submódulo!")

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print("Hola, mi nombre es", self.nombre)