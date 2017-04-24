try:
    x = input('Enter the first number: ')
    y = input('Enter the second numver: ')
    print x/y
except (ZeroDivisionError, TypeError), e:
    print e

print 'Hello, world!'
