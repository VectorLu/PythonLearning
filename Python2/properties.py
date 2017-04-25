__metaclass__ = type

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

if __name__ == '__main__':
    r = Rectangle()
    r.width = 10
    r.height = 5
    print r.size
    r.size = 150, 100
    print r.width, r.height
