import os, json

def ejemplo1():
    # CREAR UNA LISTA VACIA
    data = []

    # AÑADIR UN DICCIONARIO A LA LISTA DONDE CADA DICCIONARIO SERÁ UN CLIENTE

    cliente_dic = {} # Crear un diccionario vacio
    cliente_dic["id_cliente"] = "C1"
    cliente_dic["nombre"] = "Sergio"
    cliente_dic["apellidos"] = "Rojas Espino"
    cliente_dic["edad"] = 42
    cliente_dic["importe"] = 2.55 
    
    data.append(cliente_dic)

    cliente_dic = {} # Crear un diccionario vacio
    cliente_dic["id_cliente"] =  "C2"
    cliente_dic["nombre"] = "Pedro"
    cliente_dic["apellidos"] = "Perez Lopez",
    cliente_dic["edad"] =  25
    cliente_dic["importe"] = 8.35

    data.append(cliente_dic)

    cliente_dic = {} # Crear un diccionario vacio
    cliente_dic["id_cliente"] = "C3"
    cliente_dic["nombre"] = "Guadalupe"
    cliente_dic["apellidos"] ="Rodriguez Martinez"
    cliente_dic["edad"] =  32
    cliente_dic["importe"] = 12.44

    data.append(cliente_dic)

    print(data)

    # NOMBRE Y RUTA DEL ARCHIVO JSON
    nra = '.\\PYTHON_0019\\Ejemplo6\\data.json'

    # ESCRIBIR UN ARCHIVO JSON
    with open(nra, 'w') as f:
         json.dump(data, f, indent=4)

    print('OK: ESCRIBIR')

    print('LEER UN ARCHIVO JSON 1')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_lst_dic = json.load(f)
         print(datos_lst_dic)

    print('LEER UN ARCHIVO JSON 2')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_lst_dic = json.load(f)
         for datos_dic in datos_lst_dic:
             print(datos_dic) 

    print('LEER UN ARCHIVO JSON 3')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_lst_dic = json.load(f)
         for datos_dic in datos_lst_dic:
             id_cliente = datos_dic['id_cliente']
             nombre = datos_dic['nombre']
             apellidos = datos_dic['apellidos']
             edad = datos_dic['edad']
             importe = datos_dic['importe']  
             print(id_cliente,';',nombre,';',apellidos,';',edad,';',importe)

    print('OK: LEER')

def ejemplo2():
    data = [
             {'id_cliente': 'C1', 'nombre': 'Sergio', 'apellidos': 'Rojas Espino', 'edad': 42, 'importe': 2.55}, 
             {'id_cliente': 'C2', 'nombre': 'Pedro', 'apellidos': ('Perez Lopez',), 'edad': 25, 'importe': 8.35}, 
             {'id_cliente': 'C3', 'nombre': 'Guadalupe', 'apellidos': 'Rodriguez Martinez', 'edad': 32, 'importe': 12.44}
           ]
    print(data)

    # NOMBRE Y RUTA DEL ARCHIVO JSON
    nra = '.\\PYTHON_0019\\Ejemplo6\\data.json'

    # ESCRIBIR UN ARCHIVO JSON
    with open(nra, 'w') as f:
         json.dump(data, f, indent=4)

    print('OK: ESCRIBIR')

    print('LEER UN ARCHIVO JSON 1')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_json = json.load(f)
         print(datos_json)

    print('LEER UN ARCHIVO JSON 2')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_lst_dic = json.load(f)
         for datos_dic in datos_lst_dic:
             print(datos_dic) 

    print('LEER UN ARCHIVO JSON 3')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_lst_dic = json.load(f)
         for datos_dic in datos_lst_dic:
             id_cliente = datos_dic['id_cliente']
             nombre = datos_dic['nombre']
             apellidos = datos_dic['apellidos']
             edad = datos_dic['edad']
             importe = datos_dic['importe']  
             print(id_cliente,';',nombre,';',apellidos,';',edad,';',importe)


def main():
    os.system("cls")
    #ejemplo1()
    ejemplo2()
          
if __name__ == "__main__":
   main()