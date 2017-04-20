#!usr/bin/env python3
# -*- coding: utf-8 -*-
# list
## list.append(x)
## list.extend(x)
## list.insert(i, x)
## list.remove(x) 删除列表中值为 x 的第一个元素
## 如果没有这样的元素，就会返回一个错误
## list.pop(i)
## list.clear() = del a[:]
## list.index(x)
## list.count(x)
## list.sort(x) 就地排序
## list.reverse(x) 就地倒排
## list .copy() = a[:]

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print(a)

print(a.index(333))

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

print(a.pop())

print(a)

# 把列表当作堆栈使用
stack = [3, 4, 5]
stack.append(6)
print(stack)
print(stack.pop())
print(stack.pop())

# 实现队列
from collections import deque
queue = deque(["Eric", 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
print(queue.popleft())
print(queue.popleft())
print(queue)


# 列表推导式
squares = [x**2 for x in range(10)]
print(squares)

xy = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x!= y]
print(xy)

# 更多列表推导式实例
vec = [-4, -2, 0, 2, 4]
vec1 = [x*2 for x in vec]
vec2 = [x for x in vec if x >= 0]

# apply a function to all the elements
vec3 = [abs(x) for x in vec]
freshfruit = [' banana ', ' loganberry ', ' passion fruit ']
print(freshfruit)

# call a method on each element
freshfruit1 = [weapon.strip() for weapon in freshfruit]
print (freshfruit1)

# create a list of 2-tuples like (number, square)
vec4 = [(x, x**2) for x in range(6)]
print(vec4)

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8,9]]
vec5 = [num for elem in vec for num in elem]
print(vec5)

from math import pi
pi_str_list = [str(round(pi, i)) for i in range(1, 6)]
print(pi_str_list)
