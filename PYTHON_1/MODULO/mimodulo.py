def saludar(nombre):
    return f"Hola, {nombre}!"

def suma(a, b):
    return a + b

mi_variable = "¡Hola desde mi módulo!"

class MiClase:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial

    def get_valor(self):
        return self.valor

    def set_valor(self, nuevo_valor):
        self.valor = nuevo_valor