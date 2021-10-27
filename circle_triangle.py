# !/usr/bin/env python3
# -*- encoding:utf-8 -*-

import math

if __name__ == "__main__":
    S1 = float(input("Triangle volume: "))
    S2 = float(input("Circle volume: "))

    a = math.sqrt(4 * (S1 / math.sqrt(3)))
    r_c = math.sqrt(S2 / math.pi)
    r = a * math.sqrt(3) / 6
    R = a * math.sqrt(3) / 3

    if r_c <= r:
        print("Окружность может поместиться в треугольнике.")
    else:
        print("Окружность не может поместиться в треугольнике.")
    if r_c >= R:
        print("Треугольник может поместиться в окружности.")
    else:
        print("Треугольник не может поместиться в окружности.")
