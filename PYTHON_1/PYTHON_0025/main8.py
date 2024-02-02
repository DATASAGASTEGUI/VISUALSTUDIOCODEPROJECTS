import os

español_dic = {
    '1': 'sumar',
    '2': 'restar',
    '3': 'multiplicar',
    '4': 'dividir'
}

ingles_dic = {
    '1': 'add',
    '2': 'subtract',
    '3': 'multiply',
    '4': 'divide'
}

def ejemplo1():
    pass

def main():
    os.system("cls")
    idioma = input('INGRESE IDIOMA (INGLES O ESPAÑOL) ? ')
    if idioma.upper() == 'INGLES':
       resultado_dic = ingles_dic.copy()
    else:
       resultado_dic = español_dic.copy()
    for tupla in list(resultado_dic.items()):
        print('[',tupla[0],']','',tupla[1])
        

    ejemplo1()
          
if __name__ == "__main__":
   main()