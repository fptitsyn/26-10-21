#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x = float(input("x: "))
    y = float(input("y: "))

    s1 = a * c
    s2 = x * y

    if s1 < s2:
        print("Кирпич пройдёт")
    else:
        print("Кирпич не пройдёт")
