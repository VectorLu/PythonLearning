# coding: utf-8
def hanoi(n, A, B, C):
    if 1==n:
        print(A, '-->', C)
    else:
        hanoi(n-1, A, C, B)
        hanoi(1, A, B, C)
        hanoi(n-1, B, A, C)

# 注意input()的返回值是字符串,要强制转换为整型
n = int(input('Please input the layer of the hanoi tower:'))

hanoi(n, 'A', 'B', 'C')
