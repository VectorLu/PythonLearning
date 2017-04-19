#!usr/bin/env python3
# -*- coding: utf-8 -*-

def fiboGenerator(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

f = fiboGenerator(6)
for i in f:
    print(i)
