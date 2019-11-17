class Stack:
    def __init__(self, start=[]):
            self.stack = []
            for x in start:
                self.push(x)
    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print('警告，栈为空!')
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]
