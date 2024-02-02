from figurageometrica2d import FiguraGeometrica2D
import math

class Cuadrado(FiguraGeometrica2D):

      def __init__(self, lado):
          self.lado = lado

      def perimetro(self):
          return round(2 * self.lado,2)
      
      def area(self):
          return round(math.pow(self.lado,2),2)

      def soy(self):
          return "Cuadrado"
      
      def __str__(self):
          return f'{self.soy()},{self.lado},{self.area()},{self.perimetro()}'