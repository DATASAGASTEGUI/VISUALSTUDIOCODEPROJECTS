#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

def ejemplo1():
    enteros_l = [1,2,3,4,5,6,7,8,9]
    sublistas1_l = enteros_l[0:]     # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sublistas2_l = enteros_l[0:5]    # [1, 2, 3, 4, 5]
    sublistas3_l = enteros_l[3:6]    # [4, 5, 6]
    sublistas4_l = enteros_l[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sublistas5_l = enteros_l[3::-1]  # [4, 3, 2, 1] 
    sublistas6_l = enteros_l[8:5:-1] # [9, 8, 7]

    print(sublistas6_l)

def main():
    os.system("cls")
    ejemplo1()
          
if __name__ == "__main__":
   main()