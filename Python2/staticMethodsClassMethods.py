__metaclass__ = type

class MyClass:
    @staticmethod
    def smeth():
        print 'This is a static method'
    # smeth = staticmethod(smeth)

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls
    # cmeth = classmethod(cmeth)

MyClass.smeth()
MyClass.cmeth()

a = MyClass()
a.smeth()
a.cmeth()
