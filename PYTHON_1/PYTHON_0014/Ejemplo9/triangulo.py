from figurageometrica2d import FiguraGeometrica2D
import math

class Triangulo(FiguraGeometrica2D):

      def __init__(self, base, altura):
          self.base = base
          self.altura = altura

      def perimetro(self):
          return round(3 * self.base,2)
      
      def area(self):
          return round(self.base * self.altura / 2,2)

      def soy(self):
          return "Triangulo"
      
      def __str__(self):
          return f'{self.soy()},{self.base},{self.altura},{self.area()},{self.perimetro()}'