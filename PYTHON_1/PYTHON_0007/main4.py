#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def main():
    os.system("cls")
    enteros_l = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
    renteros_l = []
    for x in enteros_l:
        if x == 2:
           enteros_l.remove(x)

    print(enteros_l)
          
if __name__ == "__main__":
   main()