# Importa el módulo que creaste
import mimodulo, os

os.system('cls')

# Usa las funciones y variables del módulo
print(mimodulo.saludar("Juan"))
print(mimodulo.suma(5, 3))
print(mimodulo.mi_variable)

# Crea una instancia de la clase MiClase
mi_instancia = mimodulo.MiClase(valor_inicial=10)

# Utiliza métodos de la clase
print("Valor inicial:", mi_instancia.get_valor())

# Modifica el valor usando el método set_valor
mi_instancia.set_valor(20)

# Imprime el nuevo valor
print("Nuevo valor:", mi_instancia.get_valor())