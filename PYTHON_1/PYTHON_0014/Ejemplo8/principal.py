#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from empleado import Empleado
from supervisor import Supervisor
from conserje import Conserje

def ejemplo1():
    e1 = Empleado('111A','Luis',24,'H')
    print(e1.presentarse())

def ejemplo2():
    s1 = Supervisor('222A','Carmen',25,'M','Supervisor')
    print(s1.presentarse())
    print(s1.supervisar())

def ejemplo3():
    c1 = Conserje('333A','María',35,'M')
    print(c1.presentarse())
    print(c1.apoyar())

if __name__ == "__main__":
   os.system("cls")
   ejemplo3()