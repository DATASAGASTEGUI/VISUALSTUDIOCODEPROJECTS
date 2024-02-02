from figurageometrica2d import FiguraGeometrica2D

class Rectangulo(FiguraGeometrica2D):

      def __init__(self, largo, ancho):
          self.largo = largo
          self.ancho = ancho

      def perimetro(self):
          return round(2 * self.largo + 2 * self.ancho,2)
      
      def area(self):
          return round(self.largo * self.ancho,2)
      
      def soy(self):
          return "Rectangulo"
      
      def __str__(self):
          return f'{self.soy()},{self.largo},{self.ancho},{self.area()},{self.perimetro()}'