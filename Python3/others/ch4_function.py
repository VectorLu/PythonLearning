def concat(*args, sep='/'):
    return sep.join(args)

'''
print(concat('earth', 'mars', 'venus'))
print(concat('earth', 'mars', 'venus', sep='.'))
'''

def make_incrementor(n):
    return lambda x: x + n


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
