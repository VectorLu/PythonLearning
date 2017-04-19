#!usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):  # NOTE: Write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print(" ")

def fib2(n): # NOTE: return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print(__name__)
if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
