class Counter():
    def __init__(self, name, value):
        self.number = 0
    def __getattr__(self, name):
        self.name = name
        self.flag = True
        return super().__getattr__(self, name)
    def __setattr__(self, name, value):
        if self.flag == True:
            super(
            super().__setattr__(self, name, value)
        else:
            super().__setattr__(self, name, value)

c = Counter()
c.x = 1
print(c.counter)
c.y = 1
print(c.counter)
