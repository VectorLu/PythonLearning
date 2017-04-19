'''
尽管每个值都有一个相关类型，
但变量名称是无类型的，在执行过程中可以引用任意类型的数据
'''

principle = 1000
rate = 0.05
yearNum = 5
year = 1
while year <= yearNum:
    principle = principle * (1 + rate)
    # print(year, principle)
    print("%3d %0.2f" % (year, principle))
    year += 1
