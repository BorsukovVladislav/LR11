#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder(r, h, check):
    s = 2 * math.pi * r * h

    def circle():
        s_circle = math.pi * r ** 2
        return s_circle

    if check == 1:
        return f"Боковая площадь цилиндра: {s}"
    else:
        full_s = s + circle() * 2
        return f"Полная площадь цилиндра: {full_s}"


if __name__ == "__main__":
    a = float(input("Введите радиус цилиндра: "))
    b = float(input("Введите высоту цилиндра: "))
    c = int(input("1 - боковая площадь; 2 - полная площадь: "))

    print(cylinder(a, b, c))
