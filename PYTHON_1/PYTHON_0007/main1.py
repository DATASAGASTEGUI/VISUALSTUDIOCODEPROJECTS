#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def main():
    os.system("cls")
    enteros_l = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
    renteros_l = []
    for i in range(len(enteros_l)):
        if enteros_l[i] not in renteros_l:
           renteros_l.append(enteros_l[i])

    print(renteros_l)
          
if __name__ == "__main__":
   main()
