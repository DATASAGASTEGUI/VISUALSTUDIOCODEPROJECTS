import os, json

def ejemplo1():
    nra = '.\\VISUALSTUDIOCODEPROJECTS\\PYTHON_1\\PYTHON_0019\\Ejemplo5\\datos.json' # 1
    with open(nra, 'r') as filejson: # 2         
         alumnos_lst = json.load(filejson) # 3
         print(alumnos_lst)
         for alumno in alumnos_lst: # 4
             nombre = alumno['nombre']
             edad = alumno['edad']
             curso = alumno['curso']
    
             print("Nombre:", nombre)
             print("Edad:", edad)
             print("Curso:", curso)
             print()

# 1. Nombre del archivo JSON que deseas leer.
# 2. Abrir el archivo JSON y leer su contenido.
# 3. Ahora puedes acceder a los datos como un diccionario de Python.
# 4. Iterar sobre cada usuario y obtener sus detalles
# -----------------------------------------------------------------------------
        
def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()