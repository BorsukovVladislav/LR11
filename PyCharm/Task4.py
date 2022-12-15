#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите число: ")


def test_input(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def str_to_int(n):
    return int(n)


def print_int(n):
    print(n, type(n))


if __name__ == "__main__":
    ent_n = get_input()
    print(ent_n, type(ent_n))
    if test_input(ent_n):
        str_to_int(ent_n)
        print_int(str_to_int(ent_n))
    else:
        print(f"Невозможно преобразовать к целочисленному типу {ent_n}")
