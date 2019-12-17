---
layout: post
title: python 魔法方法 (5) 属性访问
date: 2019-12-16 11:28:24.000000000 +09:00
tags: python
---

整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

#### 属性访问操作，getattr()，setattr()以及delattr()函数

通常可以通过(.)操作符的形式去访问对象的属性。

```python
>>> class C:
    def __init__(self):
        self.x = 'RED'

>>> c = C()
>>> c.x
'RED'
>>> getattr(c, 'x', '没有这个属性')
'RED'
>>> getattr(c, 'y', '没有这个属性')
'没有这个属性'
>>> setattr(c, 'y', 'YELLOW')
>>> getattr(c, 'y', '没有这个属性')
'YELLOW'
>>> delattr(c. 'x')
>>> c.x
AttributeError: 'C' object has no attribute 'x'
```

#### property()函数

代码如下，

```python
calss C:
    def __init__(self, size = 10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)
```

程序实现如下，

```python
>>> c = C()
>>> c.x
10
>>> c.x = 12
>>> c.x
12
>>> c.size
12
>>> del c.x
>>> c.size
AttributeError: 'C' object has no attribute 'size'
```

关于属性访问，有对应的魔法方法来管理，通过对这些魔法方法的重写，可以随心所欲地控制对象的属性访问。

下表列举了属性相关的魔法方法。

| 魔法方法                           | 含义                                       |
|------------------------------------|--------------------------------------------|
| \_\_getattr\_\_(self, name)        | 定义当用户试图获取一个不存在的属性时的行为 |
| \_\_getattribute\_\_(self, name)   | 定义当该类的属性被访问时的行为             |
| \_\_setattr\_\_(self, name, value) | 定义当一个属性被设置时的行为               |
| \_\_delattr\_\_(self, name)        | 定义当一个属性被删除时的行为               |

```python
class C:
    def __getatrribute__(self, name):
        print('getattribute')
        # 使用super()调用object基类的__getattribute__()方法
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print('setattr')
        super().__delattr__(name)

    def __getattr__(self, name):
        print('getattr')
```

程序实现如下，

```python
>>> c = C()
>>> c.x
getattribute  #首先该类的属性被访问
getattr       #然后用户试图获取一个不存在的属性
>>> c.x = 1
setattr       #定义当一个属性被设置时
>>> c.x
getattriburte
1
>>> del c.x   #当一个属性被删除时
delattr
>>> setattr(c, 'y', 'Yellow')
setattr
```

#### 属性相关魔法方法的死循环陷阱

代码为例，写一个矩形类，默认有宽和高两个属性；如果为一个叫square的属性赋值，那么说明这是一个正方形，值就是正方形的边长，此时宽和高都应该等于边长。

```python
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            self.name = value

    def getArea(self):
        return self.width * self.height
```
这个代码会出现无限递归，问题出在在第一次执行初始化方法时，`self.width = width`调用了\_\_setattr\_\_()方法，在进入\_\_setattr\_\_()后，执行`self.width = value`再次调用了\_\_setattr\_\_()方法，继而陷入无限递归。

解决这个问题有两个办法：

1. 使用super()函数来调用基类的\_\_setattr\_\_()<br>
代码如下，<br>
```python
super().__setattr__(name, value)
```
2. 另一种方法就是给特殊属性\_\_dict\_\_赋值。对象有一个特殊的属性，成为\_\_dict\_\_，它的作用是以字典的形式显示出当前对象的所有属性以及相对应的值：<br>
```python
>>> r1.__dict__
{'height': 10, 'width': 10}
```
代码如下，

```python
else:
    self.__dict__[name] = value
```

一般，第一种方法更为常用，即使用super()函数来调用基类的\_\_setattr\_\_()。

> 问题(1)，推断以下代码会显示什么？

```python
>>> class C:
        def __getattr__(self, name):
            print(1)
        def __getattribute__(self, name):
            print(2)
        def __setattr__(self, name, value):
            print(3)
        def __delattr__(self, name):
            print(4)

>>> c = C()
>>> c.x = 1
# 位置1， 请问这里会显示什么？
>>> print(c.x)
# 位置2， 请问这里会显示什么？
```

位置1，在c实例化后，由于对c的x属性进行了设置，所以调用了\_\_setattr\_\_()方法，所以打印3。

位置2，因为要访问实例c的x属性，所以会调用\_\_getattribute\_\_()方法，由于改写了该方法，所以只打印2，而且由于未设定返回值，所以打印None。

> 问题(2)，推断一下代码会显示什么？

```python
>>> class C:
        def __getatrr__(self, name):
            print(1)
            return super().__getattr__(name)
        def __getattribute__(self, name)
            print(2)
            return super().__getattribute__(name)
        def __setattr__(self, name, value):
            print(3)
            super().__setattr__(name, value)
        def __delattr__(self, name):
            print(4)
            super().__delattr__(name)

>>> c = C()
>>> c.x
```
显示，
```python
2
1
AtrributeError: 'super' object has no attribute '__getattr__'
```
分析：<br>
首先c.x会先调用\_\_getattribute\_\_()魔法方法，打印2；然后调用super().\_\_getattribute\_\_()，找不到属性名x，因此会紧接着调用\_\_getattr\_\_()，于是打印1；但是需要注意的是，super()并没有\_\_getattr\_\_()，下面为super的方法：
```python
>>> dir(super)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', ''__lt__, '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__self_class__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__thisclass__']
```

> 问题(3) 指出下面代码的问题，

```python
class Counter:
    def __init__(self):
        self.counter = 0
    def __setattr__(self, name, value):
        self.counter += 1
        super().__setattr__(name, value)
    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)
```
下面来分析一下程序运行，首先当代码执行到`self.counter = 0`，由于初始化方法中没有counter这个属性，所以会调用`__setattr__()`方法，但是由于在初始化方法中并没有定义self.counter属性，所以在`__selfattr__()`执行的`self.counter += 1`就无法正确实现`+= 1`。

> 问题(4) 按要求重写魔法方法：当访问一个不存在的属性时，不报错切提示"该属性不存在！"

```python
>>> class Demo:
        def __getattr__(self, name):
            return '该属性不存在'


>>> demo = Demo()
>>> demo.x
`该属性不存在！`
```

> 问题(5) 编写Demo类，使得下面代码可以正常运行：

```python
>>> demo = Demo()
>>> demo.x
'FishC'
>>> demo.x = "X-man"
>>> demo.x
'X-man'
```
代码如下：

```python
>>> class Demo:
        def __getattr__(self, name):
            self.name = 'FishC'
            return self.name
```

>**问题(6) 编写一个Counter类，用于实时监测对象有多少个属性。**

```python
>>> c = Counter()
>>> c.x = 1
>>> c.counter
1
>>> c.y = 1
>>> c.z = 1
>>> c.counter
3
>>> del c.x
>>> c.counter
2
```

代码如下，

```python
class Counter():
    def __init__(self):
        super().__setattr__('counter', 0)  # 调用基类的不用添加self指针了

    def __setattr__(self, name, value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(name)
```







