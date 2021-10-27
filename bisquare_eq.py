#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b * b - 4 * a * c

if D > 0:
    t1 = (-b - sqrt(D)) / (2 * a)
    t2 = (-b + sqrt(D)) / (2 * a)
    print(-sqrt(t1), sqrt(t1), -sqrt(t2), sqrt(t2))
elif D == 0:
    t = -b / (2 * a)
    print(-sqrt(t), sqrt(t))
else:
    print("No roots.")

