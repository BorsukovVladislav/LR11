#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    f_num = 1
    while True:
        n_num = int(input("Введите число: "))
        if n_num != 0:
            f_num *= n_num
        else:
            break
    return f_num


if __name__ == "__main__":
    print(f"Результат перемножения введённых чисел до нуля: {multiply()}")
