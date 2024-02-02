import math

class Circulo:
      def __init__(self,radio=None):
          self.__radio = radio

      def get_radio(self):
          return self.__radio
      
      def set_radio(self, radio):
          self.__radio = radio

      def perimetro(self):
          return 2 * math.pi * self.__radio
      
      def area(self):
          return math.pi * math.pow(self.__radio,2)
      
      @staticmethod
      def cabecera():
          print('%9s  %10s  %10s  %10s' % ('IDCIRCULO','RADIO','PERIMETRO','AREA'))
          print('%9s  %10s  %10s  %10s' % ('---------','-----','---------','----'))

      def cuerpo(self,i):
          print('%9d  %10.2f  %10.2f  %10.2f' % (i,self.get_radio(),self.perimetro(),self.area()))
      
      def __str__(self):
          return f'radio={round(self.__radio,2)},area={round(self.area(),2)},perimetro={round(self.perimetro(),2)}'
      
      def __del__(self):
          print('Objeto eliminado')