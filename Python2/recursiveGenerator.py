def flatten1(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

nestedL = [[[1], 2], 3, 4, [5, [6, 7]], 8]
flattenedList = list(flatten(nestedL))
print flattenedList

'''
There are two reasons why you shouldn't iterate over string-like objects in the flatten function. First, you want to treat string-like objects as atomic values, not as sequences that should be flattened. Second, iterating over them would actually lead to infinite recursion because the first element of a string is another string of length one, and the first element of that string is the string itself!
'''

def flatten2(nested):
    try:
        # 不迭代 string-like 的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested
