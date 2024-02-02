import math

class Circulo:
      def perimetro(radio):
          return 2 * math.pi * radio
      
      def area(radio):
          return math.pi * math.pow(radio,2)
      
      def cabecera():
          print('%9s  %10s  %10s  %10s' % ('IDCIRCULO','RADIO','PERIMETRO','AREA'))
          print('%9s  %10s  %10s  %10s' % ('---------','-----','---------','----'))

      def cuerpo(i,radio):
          print('%9d  %10.2f  %10.2f  %10.2f' % (i,radio,Circulo.perimetro(radio),Circulo.area(radio)))
      
