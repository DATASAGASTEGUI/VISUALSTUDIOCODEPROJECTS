from figurageometrica2d import FiguraGeometrica2D
import math

class Circulo(FiguraGeometrica2D):
      
      def __init__(self, radio):
          self.radio = radio

      def perimetro(self):
          return round(2 * math.pi * self.radio,2)
      
      def area(self):
          return round(math.pi * math.pow(self.radio,2),2)

      def soy(self):
          return "Circulo"
      
      def __str__(self):
          return f'{self.soy()},{self.radio},{self.area()},{self.perimetro()}'