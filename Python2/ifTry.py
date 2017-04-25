'''
如果知道某段代码可能会导致某种异常，而又不希望程序以堆栈跟踪的形式终止，那么就根据需要添加 `try/except` 或者 `try/finally` 语句（或者它们的组合）进行处理。

有些时候，条件语句可以实现和异常处理同样的功能，但是条件语句可能在自然性和可读性上差血。而从另一方面来看，某些程序中使用 `if/else` 实现会比使用 `try/except` 要好。

假设有一个字典，我们希望打印出存储在特定的键下面的值。如果该键不存在，那么什么也不做。代码可能像下面这样写：
'''

# def describePerson(person):
#     print 'Description of', person['name']
#     print 'Age:', person['age']
#     if 'occupation' in person:
#         print 'Occupation:', person['occupation']

'''
代码非常直观，但是不够简洁。程序会两次查找 `occupation` 键——其中一次用来查看键是否存在（在条件语句中），另一次获得值。

另一个解决方案如下：
'''

def describePerson(person):
    print 'Description of', person['name']
    print 'Age:', person['age']
    try:
        print 'Occupation: ' + person['occupation']
    except KeyError: pass
