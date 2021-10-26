# !/usr/bin/env python3
# -*- encoding:utf-8 -*-
import math

if __name__ == "__main__":
    S1 = float(input("Square volume: "))
    S2 = float(input("Circle volume: "))

    d = math.sqrt(S2 / math.pi) * 2
    a = math.sqrt(S1)

    if d <= a:
        print("Круг может поместиться в квадрат.")
    else:
        print("Круг не может поместиться в квадрат.")
    if d >= a * math.sqrt(2):
        print("Квадрат может поместиться в круг.")
    else:
        print("Квадрат не может поместиться в круг.")
