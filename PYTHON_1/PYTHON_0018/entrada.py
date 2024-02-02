import re


class Entrada:

      @staticmethod
      def numeroEntero(s_mensaje):
         patron = "[0-9]+"
         s_numeroentero = ""
         i_numeroentero = 0
         while True:
            s_numeroentero = input(s_mensaje)
            b_correcto = re.fullmatch(patron, s_numeroentero)
            if not b_correcto:
                  print("ERROR: ENTRADA INCORRECTA")
            if b_correcto:
                  break
         i_numeroentero = int(s_numeroentero)
         return i_numeroentero

      @staticmethod
      def cadenaNombre(s_mensaje):
         patron = "[a-zA-ZñÑáéíóúÁÉÍÓÚ]+"
         s_nombre = ""
         while True:
            s_nombre = input(s_mensaje)
            b_correcto = re.fullmatch(patron, s_nombre)
            if not b_correcto:
                  print("ERROR: ENTRADA INCORRECTA")
            if b_correcto:
                  break
         return s_nombre
