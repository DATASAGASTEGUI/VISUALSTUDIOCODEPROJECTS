import os
import csv

def ejemplo1():
    nra = '.\\VISUALSTUDIOCODEPROJECTS\\PYTHON_1\\PYTHON_0018\\Ejemplo1\\Trabajador.csv'
    try:
       with open(nra, 'r') as ficherocsv:  
            lectorcsv = csv.reader(ficherocsv, delimiter=';')   
            for fila in lectorcsv: 
                print(fila)
    except:
            print('ERROR: LECTURA') 

def ejemplo2():
    transacciones_lst = []
    #nra = 'F:\\TRABAJANDO\\PROJECTS___PYTHON\\VISUALSTUDIOCODEPROJECTS\\PYTHON_1\\PYTHON_0018\\Ejemplo1\\Trabajador.csv'
    nra = '.\\VISUALSTUDIOCODEPROJECTS\\PYTHON_1\\PYTHON_0018\\Ejemplo1\\Trabajador.csv'
    try:
              with open(nra, 'r') as ficherocsv:                       
                   lectorcsv = csv.reader(ficherocsv, delimiter=';')   
                   i = 0 
                   print('%-12s %-10s %-10s %10s %18s %-16s' % ('IDTRABAJADOR','NOMBRE','APELLIDO','ANTIGUEDAD','HORASTRABAJADAS','TIPOTRABAJADOR'))
                   print('%-12s %-10s %-10s %10s %18s %-16s' % ('------------','------','--------','----------','---------------','--------------'))
                   for fila in lectorcsv:  
                       if i != 0: 
                          idTrabajador = fila[0].strip()
                          nombre = fila[1].strip()
                          apellido = fila[2].strip()
                          antiguedad = fila[3].strip()
                          horasTrabajadas = fila[4].strip()
                          tipoTrabajador = fila[5].strip()
                          print('%-12s %-10s %-10s %10s %18s %-16s' % (idTrabajador,nombre,apellido,antiguedad,horasTrabajadas,tipoTrabajador))
                       i = i + 1
    except:
              print('ERROR: LECTURA') 

def main():
    os.system("cls")
    ejemplo2()
          
if __name__ == "__main__":
   main()

