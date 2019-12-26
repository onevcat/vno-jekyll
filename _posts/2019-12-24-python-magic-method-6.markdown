---
layout: post
title: python 魔法方法(6) 描述符，property()函数的原理
date: 2019-12-24 13:48:24.000000000 +09:00
tags: python
---

整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### 描述符的概念

描述符就是将某种**特殊类型的类的实例**指派给**另一个类**的属性。而这个特殊类型的类，就是至少要再这个类里面定义\_\_get\_\_()、\_\_set\_\_()或\_\_delete\_\_()三个特殊方法中的任意一个。

| 魔法方法                           | 含义                                   |
|------------------------------------|----------------------------------------|
| \_\_get\_\_(self, instance, owner) | 用于访问属性，它返回属性的值           |
| \_\_set\_\_(self, instance, value) | 将在属性分配操作中调用，不返回任何内容 |
| \_\_delete\_\_(self, instance)     | 控制删除操作，不返回任何内容           |


### 描述符的解释

```python
class MyDespritor:
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)

    def __set__(self, instance, value):
        print("setting...", self, instance, value)

    def __delete__(self, instance):
        print("deleting...", self, instance)

class Test:
    x = MyDespritor()
```

MyDespritor实现了\_\_get\_\_()、\_\_set\_\_()和\_\_delete\_\_()方法，并且将它的类实例指派给Test类的属性，所以MyDescriptor就是描述符类。

当实例化Test类没然后尝试对x属性进行各种操作，看看描述符类的响应：

```python
>>> test = Test()
>>> test.x
getting... <__main__.MyDescriptor object at 0x02D7FE90>  
            # self，是描述符类自身的实例

           <__main__.Test object at 0x02FE0930> 
            # instance，是这个描述符的拥有者所在的类的实例

           <class '__main__.Test'>
            # owner, 是这个描述符的拥有者所在的类本身
```

```python
>>> test.x = 'X-man'
setting... <__main__.MyDescriptor object at 0x02D7FE90>
           <__main__.Test object at 0x02FE0930>
           X-man    # 最有一个参数value的值
```

```python
>>> del test.x
deleting... <__main__.MyDescriptor object at 0x02D7FE90>
            <__main__.Test object at 0x02FE0930>
```

### property()函数的原理

#### 复习property()函数

##### 什么是property()函数

property()返回一个可以设置属性的属性，当然如何设置属性还是需要人为来写代码。第一个参数是获得属性的方法名，第二个参数是设置属性的方法名，第三个参数是删除属性的方法名。例如，

```python
class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self, value):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSzie, delSize)
```

##### property()函数的作用

当我们想要对程序进行大概，就可能需要把setSize和getSize修改为setXSize和getXSize，那就不得不修改用户调用的接口，这样的体验非常不好。

有了property()，为用户访问size属性，只提供了x属性。无论内部如何改动，只需要相应地修改property()的参数，**用户仍然只需要去操作x属性即可**，没有任何影响。如下，

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

### property()函数的原理

通过描述符写一个类似于property()的Myproperty(),

```python
class Myproperty:
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = Myproperty(getX, setX, delX)


>>> c = C()
>>> c.x = 'X-man'  # 用x去干预_x
>>> c.x
'X-man'
>>> c._x
'X-man'
>>> del c.x
>>> c._x
AttributeError: 'C' object has no attributer '_x'
```

从而实现了property()函数的功能。

最后从一个实例来总结一下描述符：

先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性。两个属性会自动进行转换，也就是说，可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果。

```python
class Celsius:        # 摄氏度的描述符类
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __init__(self, value = 78.8):
        self.value = float(value) *1.8

    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
# 因为要用华氏度去设置，所以要用逆运算先计算出摄氏度，在执行__set__()方法
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


>>> temp = Temperature()
>>> temp.cel
26.0
>>> temp.fah
78.80000000000001
```

### 问题

(1) 按要求编写描述符 MyDes：当类的属性被访问、修改或设置的时候，分别作出提醒。

要求:
```python
>>> class Test:
        x = MyDes(10, 'x')

>>> test = Test()
>>> y = test.x
正在获取变量：x
>>> y
10
>>> test.x = 8
正在修改变量：x
>>> del test.x
正在删除变量：x
噢~这个变量没法删除~
>>> test.x
正在获取变量：x
8
```

代码：
```python
class MyDespritor:
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
    x = MyDespritor(10, 'x')

test = Test()
y = test.x
print(y)
test.x = 8
del test.x
test.x
print(test.x)
```

(2) 按要求编写描述符 MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件(record.txt)

要求：
```python
>>> class Test:
        x = Record(10, 'x')
        y = Record(8.8, 'y')

>>> test = Test()
>>> test.x
10
>>> test.y
8.8
>>> test.x = 123
>>> test.x = 1.23
>>> test.y = 'I love FishC.com!'
```

并产生record.txt。
```
x变量于北京时间Thu Dec 26 20:20:29 2019被读取，x = 10
y变量于北京时间Thu Dec 26 20:20:29 2019被读取，y = 8.8
x变量与北京时间Thu Dec 26 20:20:29 2019被修改，x = 123
x变量与北京时间Thu Dec 26 20:20:29 2019被修改，x = 1.23
y变量与北京时间Thu Dec 26 20:20:29 2019被修改，y = I love FIshC.com
```

代码如下，

```python
import time

class Record:
    def __init__(self, value = None, name = None):
        self.value = value
        self.name = name
        self.filename = 'record.txt'

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding = 'utf-8') as f:
            f.write('%s变量于北京时间%s被读取，%s = %s\n' % \
                    (self.name, time.ctime(), self.name, self.value))
        return self.value

    def __set__(self, instance, value):
        self.value = value
        with open(self.filename, 'a', encoding = 'utf-8') as f:
            f.write('%s变量与北京时间%s被修改，%s = %s\n' % \
                    (self.name, time.ctime(), self.name, self.value))

class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')

test = Test()
print(test.x)
print(test.y)
test.x = 123
test.x = 1.23
test.y = 'I love FIshC.com'
```

(3) 编写描述符 MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle文件。如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。

要求：
```python
>>> class Test:
        x = MyDes('x')
        y = MyDes('y')

>>> test = Test()
>>> test.x = 123
>>> test.y = "I love FishC.com!"
>>> test.x
123
>>> test.y
'I love FishC.com!'
```
产生对应的文件存储变量的值，如果我们删除x属性，对应的文件也不见了。

代码：

```python
import os
import pickle

class MyDes:
    saved = []
    def __init__(self, name, value = None):
        self.name = name
        self.value = value
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError('%s 属性还没有赋值' % self.name)
        with open(self.filename, 'rb') as f:
            value = pickle.load(f)
        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)


class Test:
    x = MyDes('x')
    y = MyDes('y')
```


