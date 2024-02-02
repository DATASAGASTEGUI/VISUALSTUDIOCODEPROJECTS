import os, json

def ejemplo1():
    # CREAR UN DICCIONARIO VACIO
    data = {}

    # CREAR UNA LISTA VACIA
    data["clientes_lst_dic"] = []

    # AÑADIR UN DICCIONARIO A LA LISTA DONDE CADA DICCIONARIO SERÁ UN CLIENTE
    data["clientes_lst_dic"].append({
    "id_cliente": "C1",
    "nombre": "Sergio",
    "apellidos": "Rojas Espino",
    "edad": 42,
    "importe": 2.55 
    })

    data["clientes_lst_dic"].append({
    "id_cliente": "C2",
    "nombre": "Pedro",
    "apellidos": "Perez Lopez",
    "edad": 25,
    "importe": 8.35
    })

    data["clientes_lst_dic"].append({
    "id_cliente": "C3",
    "nombre": "Guadalupe",
    "apellidos": "Rodriguez Martinez",
    "edad": 32,
    "importe": 12.44
    })

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
         datos_dic = json.load(f)
         datos_lst_dic = datos_dic['clientes_lst_dic']
         for datos_dic in datos_lst_dic:
             print(datos_dic) 

    print('LEER UN ARCHIVO JSON 3')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_dic = json.load(f)
         datos_lst_dic = datos_dic['clientes_lst_dic']
         for datos_dic in datos_lst_dic:
             id_cliente = datos_dic['id_cliente']
             nombre = datos_dic['nombre']
             apellidos = datos_dic['apellidos']
             edad = datos_dic['edad']
             importe = datos_dic['importe']  
             print(id_cliente,';',nombre,';',apellidos,';',edad,';',importe)

    print('OK: LEER')

def ejemplo2():
    data = {'clientes_lst_dic': [
                                  {'id_cliente': 'C1', 'nombre': 'Sergio', 'apellidos': 'Rojas Espino', 'edad': 42, 'importe': 2.55}, 
                                  {'id_cliente': 'C2', 'nombre': 'Pedro', 'apellidos': 'Perez Lopez', 'edad': 25, 'importe': 8.35}, 
                                  {'id_cliente': 'C3', 'nombre': 'Guadalupe', 'apellidos': 'Rodriguez Martinez', 'edad': 32, 'importe': 12.44}
                                ]
           }
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
         datos_dic = json.load(f)
         datos_lst_dic = datos_dic['clientes_lst_dic']
         for datos_dic in datos_lst_dic:
             print(datos_dic) 

    print('LEER UN ARCHIVO JSON 3')
    print('----------------------')
    with open(nra, 'r') as f:
         datos_dic = json.load(f)
         datos_lst_dic = datos_dic['clientes_lst_dic']
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