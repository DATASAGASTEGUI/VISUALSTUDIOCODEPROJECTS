import math

class Circulo:
      
      def perimetro(self,radio):
          return 2 * math.pi * radio
      
      def area(self,radio):
          return math.pi * math.pow(radio,2)
      
      @staticmethod
      def cabecera():
          print('%9s  %10s  %10s  %10s' % ('IDCIRCULO','RADIO','PERIMETRO','AREA'))
          print('%9s  %10s  %10s  %10s' % ('---------','-----','---------','----'))

      def cuerpo(self,i,radio):
          print('%9d  %10.2f  %10.2f  %10.2f' % (i,radio,self.perimetro(radio),self.area(radio)))
      
