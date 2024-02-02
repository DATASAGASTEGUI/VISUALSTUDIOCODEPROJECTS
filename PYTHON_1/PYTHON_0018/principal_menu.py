import os
from controlador import Controlador as C

transacciones_l = []
nra = 'PYTHON_0018\\transaccion1.csv'

def menu():
	while True:
          os.system("cls")
          print('MENU')
          print('----')
          print('(1) CARGAR LISTA CON OBJETOS TRANSACCION DESDE ARCHIVO CSV')
          print('(2) MOSTRAR LISTA DE TRANSACCIONES')
          print('(3) BUSCAR EN LA LISTA UNA TRANSACCION')
          print('(4) ELIMINAR UNA TRANSACCION DE LA LISTA')
          print('(5) ACTUALIZAR UNA TRANSACCION EN LA LISTA')
          print('(6) AGREGAR UNA TRANSACCION A LISTA')
          print('(7) DESCARGAR LISTA CON OBJETOS TRANSACCION HACIA ARCHIVO CSV')
          print('(0) SALIR')

          opcion = input('\nINGRESE OPCION? ')

          if   opcion == '1':
               os.system('cls'),C.opcion1(nra,transacciones_l),os.system('pause')
          elif opcion == '2':
               os.system('cls'),C.opcion2(transacciones_l),os.system('pause')
          elif opcion == '3':
               os.system('cls'),C.opcion3(transacciones_l),os.system('pause')
          elif opcion == '4':
               os.system('cls'),C.opcion4(transacciones_l),os.system('pause')
          elif opcion == '5':
               os.system('cls'),C.opcion5(transacciones_l),os.system('pause')
          elif opcion == '6':
               os.system('cls'),C.opcion6(transacciones_l),os.system('pause')
          elif opcion == '7':
               os.system('cls'),C.opcion7(nra,transacciones_l),os.system('pause')
          elif opcion == '0':
               os.system('cls')
               print('\nGRACIAS POR SU VISITA\n')
               os.system('pause')
               os.system('cls')
               break
          else:pass

def main():
    menu()
          
if __name__ == "__main__":
   main()