class People:
    def setName(self, name):
        self.name = name
    def intro(self):
        print('My name is %s' % self.name)

A = People()
B = People()
A.setName('A')
B.setName('B')

A.intro()
B.intro()
