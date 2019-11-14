---
layout: post
title: python 类和对象复习 (3) 继承 super函数 多重继承 钻石继承
date: 2019-11-13 21:34:24.000000000 +09:00
tags: python
---

### 继承

继承的语法为：

```python
class DerivedClassName(BaseClassName):
```
注意的是，如果子类中定义了与父类相同的**方法或者属性**，会自动覆盖父类的方法或者属性。

例如如下代码：

```python
import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def move(self):
        self.x -= 1
        print(`我的位置是: `, self.x, self. y)

class Carp(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃")
            self.hungry = False
        else:
            print("不吃")
```
运行代码后，在Carp和Shark类中分别调用```move()```方法，观察是否能运行。

```python
>>>fish = Fish()
>>>fish.move()
我的位置是：5 10
>>>shark = Shark()
>>>shark.move()
ArributeError: 'Shark' object has no atrribute 'x'
```

分析原因就是因为在Shark类中，重新定义了构造方法，覆盖了父类Fish的move()方法。

解决方法有两个：

方法1. 在定义Shark的构造方法时，调用未绑定的父类方法
```python
class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True
```
或者
```python
calss Shark(Fish):
    def __init__(self):
        Fish.__init__(shark)
        self.hungry = True
```
需要注意的是，这个self并不是父类Fish的实例对象，而是子类的实例对象，而题目所谓的未绑定的父类方法意思就是，并不绑定父类的实例对象，而是直接使用子类的实例对象。

方法2. 使用super函数

super 函数能够自动找到基类的方法，而不需要给出任何基类的名字，会自动找出所有基类以及对应的方法。用法如下：


```python
class Shark(Fish):
    super().__init__()
    self.hungry = True
```

### 多重继承

多重继承的语法是：
```python
class DerivedClassName(Base1, Base2, Base3):
```
举个例子：
```python
class Base1:
    def foo1(self):
        print("foo1")
class Base2:
    def foo2(self):
        print("foo2")
class C(Base1, Base2):
    pass

>>>c = C()
>>>c.foo1()
foo1
>>>c.foo2()
foo2
```

值得注意的是多重继承问题尽量避免使用，会出现钻石继承问题。

### 钻石继承

钻石继承是多重继承的陷阱，如下代码：

```python
class A():
   def __init__(self):
       print("进入A…")
       print("离开A…")

class B(A):
   def __init__(self):
       print("进入B…")
       A.__init__(self)
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")

>>> d = D()
进入D…
进入B…
进入A…
离开A…
离开B…
进入C…
进入A…
离开A…
离开C…
离开D…
```
如下图所示:
![figure1](/assets/201911/20191113.png)

因为从D类继承的方式有通过A类为基类的B类，以及通过A类为基类的C类两个方式继承。这样在调用D类时，就会两个词进入A类。如果这时加入计数器会**发生计数错误的情况**。

解决钻石继承的方法可以使用Method Resolution Order(MRO) 方法解析顺序的方法，以及C3算法。

**MRO顺序，就是在避免同一类被调用多次的前提下，使用广度优先和左到右的原则去寻找需要的属性和方法。**

C3算法确保同一个类只会被搜寻一次，如果一个属性或者方法在D类中没有被找到，Python就会搜索B类，然后搜索C类，如果都没有找到，会继续搜索B的基类A，如果还没有找到会抛出'AttributeError'异常。

```python
 #方法为类.__mro__获得MRO的顺序
>>>D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
 #object是所有类的基类
```

或者利用super函数解决。

```python
class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")

>>> d = D()
进入D…
进入B…
进入C…
进入A…
离开A…
离开C…
离开B…
离开D…
```

> 注意1：构造方法不能return值，否则报错

```python
TypeError: __init__() should return None, not 'str'
```

> 注意2：当子类方法覆盖了父类方法时，不会删除父类方法，只是该子类看不到父类方法了而已

> 注意3：当我们想故意覆盖掉父类的方法时，可以定义一个方法直接pass掉，如下：

```python
class Bird:
    def fly(self):
        print("fly")

class Penguin(Bird):
    def fly(self):
        pass
```

> 练习：定义一个点（Point）类和直线（Line）类，使用getLen方法可以获得直线长度

提示：
Python中开根号使用math模块中的sqrt函数
