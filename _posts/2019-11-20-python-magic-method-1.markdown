---
layout: post
title: python 魔方方法 (1) 构造与析构
date: 2019-11-20 22:13:24.000000000 +09:00
tags: python
---

### 构造与析构

#### `__init__(self[,...])`

 __init__()相当于其他面向对象编程语言的构造方法，也就是**类在实例化成对象时，首先会调用的方法**。

```python
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y
>>> rect = Rectangle(3, 4)    #这里输入__init__()中需要的参数。
>>> rect.getArea()
12
```

> 需要注意，__init__()方法不能return值，只能return None.

#### `__new__(cls[,...])`

 `__new__()`方法是对象实例化时，调用的第一个方法。**他的第一个参数不self，而是类cls**，**同时，其他参数会传入`__init__()`中**。

 `__new__()`**需要返回一个实例对象**，通常是cls这个类实例化的对象，当然也可以返回其他对象。

 通常在**继承一个不可变的类型的时候**，需要使用`__new__()`方法。如下代码：

```python
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)
>>> a = Capstr('abc')
>>> a
'ABC'
```
#### `__del__(self)`

  `__del__()`方法只有在垃圾回收机制激活时才能调用，即对应数据完全删除以后。

```python
class DelPrint():
    def __del__(self):
        print('__delf__()方法被调用')

>>> A = DelPrint()
>>> B = A
>>> C = B
>>> del B
>>> del C
>>> del A
__delf__()方法被调用
```

练习：

(1) 写一个FileObject类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭。

```python
class FileObject:
    def __init__(self, FILE='example.txt'):
        self.FILE = open(FILE, 'r')
    del __del__(self):
        self.FILE.close()
        del self.FILE
```


(2) 定义一个摄氏度到华氏度转换(华氏度 = 摄氏度\*1.8 + 32)。

```python
class C2F(float):
    def __new__(cls, C = 0.0):
        return float.__new__(cls, C * 1.8 + 32)
```

(3) 定一个一个类继承int类型，当传入参数是字符串时候，返回该字符串所有字符的ASCII码的和（ord()）

```python
class TOASCII(int):
    def __new__(cls, INPUT = ''):
        if isinstance(INPUT, str):
            total = 0
            for each in INPUT:
                total += ord(each)
                INPUT = total  #最后要赋值回INPUT
        return int.__new__(cls, INPUT)

>>> print(TOASCII('A'))
```

