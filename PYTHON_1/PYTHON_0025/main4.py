import os

def ejemplo1():
    traductor_dic = {
       'hello': 'hola',
       'goodbye': 'adiós',
       'thank you': 'gracias'
    }
    claves_lst = list(traductor_dic.keys())
    print("%-12s %-12s" % ('INGLES', 'ESPAÑOL'))
    print("%-12s %-12s" % ('------', '-------'))
    for clave in claves_lst:
        print("%-12s %-12s" % (clave, traductor_dic[clave]))

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()