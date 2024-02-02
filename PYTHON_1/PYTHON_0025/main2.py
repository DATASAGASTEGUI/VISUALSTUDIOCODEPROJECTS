import os, sys

def opcion1():
    print('OPCION 1')
    print('--------')

def opcion2():
    print('OPCION 2')
    print('--------')

def opcion3():
    print('OPCION 3')
    print('--------')

def salir():
    print('GRACIAS POR SU VISITA')
    os.system('pause')
    sys.exit()
    os.system('cls')

def main():
    # DICCIONARIO QUE MAPEA OPCIONES A FUNCIONES
    menu_dic = {
                '1': opcion1,
                '2': opcion2,
                '3': opcion3,
                '4': salir
               }
    while True:
          # MOSTRAR EL MENU
          os.system("cls")
          print('MENU')
          print('----')
          print("1. OPCION 1")
          print("2. OPCION 2")
          print("3. OPCION 3")
          print("4. SALIR")
          opcion = input('\nINGRESE OPCION? ')
          if opcion in menu_dic:
             os.system("cls");menu_dic[opcion]();os.system("pause")
          else:
             os.system("cls");print('OPCION NO VALIDA');os.system("pause")
          
if __name__ == "__main__":
   main()