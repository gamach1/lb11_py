#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiplyyy_numbers():
    product = 1
    while True:
        num = float(input("Введите число (введите 0 для завершения): "))
        if num == 0:
            break
        product *= num
    return product

result = multiplyyy_numbers()
print("Произведение введенных чисел:", result)
