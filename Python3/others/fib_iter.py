class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self    # 本身就是迭代对象，返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 10000:
            raise StopIteration();
        return self.a

for n in Fib():
    print(n)
