from os import path
from crud import Crud
from transacciones import Transacciones
from transaccion import Transaccion
from entrada import Entrada


class Controlador:

      @staticmethod
      def opcion1(nra,transacciones_l):
          transacciones_l.clear()
          if path.exists(nra):
             Crud.leerLlenarListaObjetosTransaccionDesdeArchivoCsv(nra,transacciones_l)
             if transacciones_l != None:
                print('OK: LEER ARCHIVO')
             else:
                print("ERROR: LEER ARCHIVO")
          else:
             print('ERROR: ARCHIVO NO EXISTE')

      @staticmethod
      def opcion2(transacciones_l):
          if transacciones_l != None:
             if len(transacciones_l) > 0:
                transacciones = Transacciones(transacciones_l)
                transacciones.mostrar()
             else:
                print('ERROR: LISTA VACIA')
          else:
             print('ERROR: LEER ARCHIVO')

      @staticmethod
      def opcion3(transacciones_l):
          if transacciones_l != None:
             if len(transacciones_l) > 0:
                idTransaccionBuscar = Entrada.numeroEntero("INGRESE ID TRANSACCION A BUSCAR? ")
                transacciones = Transacciones(transacciones_l)
                transaccionbuscar = transacciones.buscar(idTransaccionBuscar)
                if transaccionbuscar != None:
                   Transaccion.cabecera()
                   transaccionbuscar.cuerpo()
                else:
                    print('ERROR: TRANSACCION NO EXISTE')
             else:
                print('ERROR: LISTA VACIA')
          else:
             print('ERROR: LEER ARCHIVO')

      @staticmethod
      def opcion4(transacciones_l):
          if transacciones_l != None:
             if len(transacciones_l) > 0:
                idTransaccionEliminar = Entrada.numeroEntero("INGRESE ID TRANSACCION A ELIMINAR? ")
                transacciones = Transacciones(transacciones_l)
                transaccioneliminar = transacciones.buscar(idTransaccionEliminar)
                if transaccioneliminar != None:
                   if transacciones.eliminar(idTransaccionEliminar):
                      print('OK: ELIMINAR TRANSACCION')
                   else:
                      print('ERROR: ELIMINAR TRANSACCION')
                else:
                    print('ERROR: TRANSACCION NO EXISTE')
             else:
                print('ERROR: LISTA VACIA')
          else:
             print('ERROR: LEER ARCHIVO')

      @staticmethod
      def opcion5(transacciones_l):
          if transacciones_l != None:
             if len(transacciones_l) > 0:
                idTransaccionActualizar = Entrada.numeroEntero("INGRESE ID TRANSACCION A ACTUALIZAR? ")
                transacciones = Transacciones(transacciones_l)
                transaccionactualizar = transacciones.buscar(idTransaccionActualizar)
                if transaccionactualizar != None:
                   ciudadActualizar = Entrada.cadenaNombre("INGRESE CIUDAD A ACTUALIZAR? ")
                   if transacciones.actualizar(idTransaccionActualizar, ciudadActualizar) != None:
                      print('OK: ACTUALIZAR TRANSACCION')
                   else:
                      print('ERROR: ACTUALIZAR TRANSACCION')
                else:
                    print('ERROR: TRANSACCION NO EXISTE')
             else:
                print('ERROR: LISTA VACIA')
          else:
             print('ERROR: LEER ARCHIVO')

      @staticmethod
      def opcion6(transacciones_l):
          if transacciones_l != None:
                idTransaccionAgregar = Entrada.numeroEntero("INGRESE ID TRANSACCION A AGREGAR? ")
                transacciones = Transacciones(transacciones_l)
                transaccionagregar = transacciones.buscar(idTransaccionAgregar)
                if transaccionagregar == None:
                   ciudad = 'Santander'
                   zona = 'Norte'
                   ventas = 2000.00
                   formaPago = 'Tarjeta'
                   categoria = 'Electrodoméstico'
                   transaccionagregar = Transaccion(idTransaccionAgregar,ciudad,zona,ventas,formaPago,categoria)
                   if transacciones.agregar(transaccionagregar):
                      print('OK: AGREGAR TRANSACCION')
                   else:
                      print('ERROR: AGREGAR TRANSACCION')
                else:
                    print('ERROR: TRANSACCION YA EXISTE')
          else:
             print('ERROR: LEER ARCHIVO')

      @staticmethod
      def opcion7(nra,transacciones_l):
          if path.exists(nra):
             if  Crud.borrarTodasFilasArchivoCsv(nra):
                 if Crud.escribirVaciarListaObjetosTransaccionHaciaArchivoCsv(nra,transacciones_l):
                    print("OK: ESCRIBIR ARCHIVO")
                 else:
                    print('ERROR: ESCRIBIR ARCHIVO')
             else:
                 print("ERROR: BORRAR FILAS ARCHIVO")
          else:
             print('ERROR: ARCHIVO NO EXISTE')