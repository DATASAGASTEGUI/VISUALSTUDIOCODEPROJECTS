import os

def ejemplo1():
    empleados_dic = {
        'E01': {'nombre': 'Elena', 'cargo': 'Desarrollador', 'salario': 60000},
        'E02': {'nombre': 'Carlos', 'cargo': 'Diseñador', 'salario': 55000},
        'E03': {'nombre': 'Arturo', 'cargo': 'Gerente', 'salario': 75000}
    }
    claves_lst = list(empleados_dic.keys())
    print("%-12s %-10s %-14s %10s" % ('IDEMPLEADO','NOMBRE','CARGO','SALARIO'))
    print("%-12s %-10s %-14s %10s" % ('----------','------','-----','-------'))
    for clave in claves_lst:
        registro_dic = empleados_dic[clave]
        print("%-12s %-10s %-14s %10d" % (clave,registro_dic['nombre'],registro_dic['cargo'],registro_dic['salario']))


def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()