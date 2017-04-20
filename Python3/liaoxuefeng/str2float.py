# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    print(eval(s))
    return reduce(map,[eval(s)])

print('str2float(\'123.456\') =', str2float('123.456'))
