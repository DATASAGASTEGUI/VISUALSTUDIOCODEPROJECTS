class Transaccion:
      
      def __init__(self,idTransaccion=None,ciudad=None,zona=None,ventas=None,formaPago=None,categoria=None):
          self.__idTransaccion = idTransaccion
          self.__ciudad = ciudad
          self.__zona = zona
          self.__ventas = ventas
          self.__formaPago = formaPago
          self.__categoria = categoria

      def getIdTransaccion(self):
          return self.__idTransaccion
      
      def setIdTransaccion(self, idTransaccion):
          self.__idTransaccion = idTransaccion

      def getCiudad(self):
          return self.__ciudad
      
      def setCiudad(self, ciudad):
          self.__ciudad = ciudad

      def getZona(self):
          return self.__zona
      
      def setZona(self, zona):
          self.__zona = zona

      def getVentas(self):
          return self.__ventas
      
      def setVentas(self, ventas):
          self.__ventas = ventas

      def getFormaPago(self):
          return self.__formaPago
      
      def setFormaPago(self, formaPago):
          self.__formaPago = formaPago

      def getCategoria(self):
          return self.__categoria
      
      def setCategoria(self, categoria):
          self.__categoria = categoria

      def __str__(self):
          return f'[idTransaccion={self.__idTransaccion},ciudad={self.__ciudad},zona={self.__zona},ventas={self.__ventas:.2f},formaPago={self.__formaPago},categoria={self.__categoria}]'
      '''
      def __del__(self):
          print('Objeto eliminado')
          '''

      @staticmethod
      def cabecera():
          print('%13s  %-10s  %-10s  %10s  %-10s  %-20s' % ('IDTRANSACCION','CIUDAD','ZONA','VENTAS','FORMAPAGO','CATEGORIA'))
          print('%13s  %-10s  %-10s  %10s  %-10s  %-20s' % ('-------------','------','----','------','---------','---------'))

      def cuerpo(self):
          print('%13s  %-10s  %-10s  %10.2f  %-10s  %-20s' % (self.__idTransaccion,self.__ciudad,self.__zona,self.__ventas,self.__formaPago,self.__categoria))
      
      def obtenerCsv(self):
          return str(self.__idTransaccion) + ';' + self.__ciudad + ';' + self.__zona + ';' + str(self.__ventas) + ';' + self.__formaPago + ';' + self.__categoria