---
layout: post
title: python 类和对象复习(2) self 构造方法 Name Mangling
date: 2019-11-11 21:26:24.000000000 +09:00
tags: python
---

### self 是什么

Python的self相当于C++的this指针。同一个类可以生成无数个对象，当一个对象的方法被调用时，对象会将自身的引用作为第一个参数传给该方法，python就知道需要操作哪个对象的方法了。以下代码为例，

```python
class People:
    def setName(self, name):
        self.name = name
    def intro(self):
        print('My name is %s' % self.name)

A = People()
A.setName('A')    # 这里将name = 'A'传入了实例对象的self.name属性
B.setName('B')

A.intro()    # 这里'()'中为A的隐藏属性，即将A的name属性传入了self.name
B.intro()
```

### Name Mangling

对象的属性方法可以通过'.'来进行访问。如下代码：

```python
class People:
    name = "A"

>>>A = People()
>>>A.name

'A'
```

这里A的name属性是共有的。下面讲一个利用Name Mangling来对实例属性私有化并进行隐藏的例子：

```python
class People:
    __name = "A"

>>>A = People()
>>>A.__name

AttributeError: 'People' object has no attribute '__name'
```
想要访问这个私有属性的方法有两种：
1. 从内部调用该属性，例如通过定义一个函数来将这个属性从内部return出来
2. 使用"_类名__变量名"的方法来访问私有化的属性

```python
>>>A._People__name
'A'
```
