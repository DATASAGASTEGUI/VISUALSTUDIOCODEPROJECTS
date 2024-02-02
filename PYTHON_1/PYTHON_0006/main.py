import os

os.system('cls')

idPersona = ['P06','P12','P23','P14','P55']
nombre = ["Walter", "Arturo", "Jose", "María", "Delly"]
edad = [12, 13, 20, 28, 40]
estatura = [1.43, 1.51, 1.70, 1.85, 1.82]
salario = [245.78924, 2348.31454, 23.15444, 4444.1345156, 24.13541545]
casado = [True, False, True, False, False]
print("%1s  %10s  %-10s  %5s  %10s  %8s  %-10s" % ('N', 'IDPERSONA', 'NOMBRE', 'EDAD', 'ESTATURA', 'SALARIO', 'CASADO'))
print("%1s  %10s  %-10s  %5s  %10s  %8s  %-10s" % ('-', '---------', '------', '----', '--------', '-------', '------'))
for i in range(len(nombre)):
    print("%1d  %10s  %-10s  %5d  %10.2f  %8.2f  %-10s" % ((i+1), idPersona[i], nombre[i], edad[i], estatura[i], salario[i], casado[i]))
