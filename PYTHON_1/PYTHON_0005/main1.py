import os

def ejemplo1():
    n = int(input('Ingrese n? '))
    i = 1
    while i <= n:
       print(i)
       i += 1

def ejemplo2():
    n = int(input('Ingrese n? '))
    i = 1
    while i <= n:
       print(i, end=" ")
       i += 1

def main():
    os.system("cls")
    ejemplo1()
    ejemplo2()

if __name__ == "__main__":
   main()