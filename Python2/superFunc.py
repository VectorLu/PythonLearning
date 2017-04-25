__metaclass__ = type # super() 只在新式类中起作用

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'

b = Bird()
b.eat()
b.eat()
print "---------------"

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squaqk!'
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
