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
### 构造方法

__init__()方法称为构造方法，__init__()只需要实例化一个对象，这个方法就会在对象被创建时自动调用(类似于C的构造函数)。实例化对象是可以传入参数的，这些参数会自动传入__init__()中，可以通过这个方法来自定义对象的初始化操作。

```python
class People():
    def __init__(self, name)
        self.name = name
    def intro(self):
        print('I am %s' % self.name)

>>>A = People("A")
>>>A.intro()
I am A
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

> 问题1

```python
class MyClass:
    name = 'FishC'
    def myFun(self):
        print("Hello FishC!")

>>> MyClass.name
TypeErr: myFun() missing 1 required positional argument: 'self'
>>>
```
这里报错的原因，我们常说的类指的是类定义，当类定义完之后，自然就是类对象。在这个时候，你可以对类的属性（变量）进行直接访问（MyClass.name）。

一个类可以实例化出无数个实例对象，**Python为了区分是哪个实例对象调用了方法，于是要求必须绑定（通过self参数）才可以调用，而未实例化的类对象直接调用方法，因为缺少self参数，所以会报错。

这里有两种解决方案，第一种创建一个实例对象：

```python
P = MyClass()
```
第二种方式为给类MyClass加入self参数：

```python
MyClass.self.MyFun()
```

