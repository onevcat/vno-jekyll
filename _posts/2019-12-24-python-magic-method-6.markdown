---
layout: post
title: python 魔法方法(6) 描述符，property()函数的原理
date: 2019-12-24 13:48:24.000000000 +09:00
tags: python
---

```python
class MyDesprition:
    def __init__(self, value = None, name = None):
        self.value = value
        self.name  = name
    def __get__(self, instance, owner):
        print("正在获取变量：" + self.name)
        return self.value
    def __set__(self, instance, value):
        print("正在修改变量：" + self.name)
        self.value = value
    def __delete__(self, instance):
        print("正在删除变量：" + self.name + '\n'
              "噢~这个变量没法删除~")

class Test:
    x = MyDesprition(10, 'x')

test = Test()
y = test.x
print(y)
test.x = 8
del test.x
test.x
print(test.x)
```
_
