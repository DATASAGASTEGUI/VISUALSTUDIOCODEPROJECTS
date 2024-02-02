#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def main():
    os.system("cls")
    enteros_l = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
    renteros_l = []
    for x in enteros_l:
        if x % 2 != 0:
           renteros_l.append(x)

    print(renteros_l)
          
if __name__ == "__main__":
   main()


