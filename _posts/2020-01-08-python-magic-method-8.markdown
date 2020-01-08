---
layout: post
title: python 魔法方法 (8) 迭代器
date: 2020-01-08 16:21:24.000000000 +09:00
tags: python
---

整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### 迭代器的详细解释

迭代器的意思类似于循环，每一次重复的过程被称为**一次迭代的过程**，而每一次迭代得到的结果会被用来作为下一次迭代的初始值。提供迭代方法的容器被称为**迭代器**，通常接触的迭代器有序列(如列表、元组、字符)、字典等，它们都支持迭代的操作。

举个例子，通常使用for语句来进行迭代，

```python
>>> for i in "FishC"
        print(i)

F
i
s
h
C
```

字符串就是一个容器，同时也是一个迭代器，for语句的作用就是**触发这个迭代器的迭代功能**，每次从容器里一次拿出一个数据，这就是**迭代操作**。

> 但需要注意的是，迭代器不是一个容器，因为我们经常了解的容器像列表、字典、元组都是可以存放数据的，而迭代器就是实现了`__next__()`方法的对象(用于遍历容器中的数据)。

例2，字典和文件也是支持迭代操作的，

```python
>>> links = {'鱼C工作室':'http://www.fishc.com', \
             '鱼C论坛':'http://bbs.fishc.com', \
             '鱼C博客':'http://blog.fishc.com', \}
>>> for each in links:
        print('%s -> %s' % (each, links[each]))

鱼C博客 -> http://www.fishc.com
鱼C论坛 -> http://bbs.fishc.com
鱼C工作室 -> http://blog.fishc.com
```

### 迭代器的两个BIF

关于迭代，Python提供了两个BIF: `iter()`和`next()`。

对于一个容器对象调用`iter()`就**得到它的迭代器**，调用`next()`迭代器就会**返回下一个值**。

> 迭代器的结束：如果迭代器没有值就可以返回了，并抛出StopInteration Error。

```python
>>> string = "FishC"
>>> it = iter(string)  # iter() --> 获得了字符串容器的迭代器
>>> next(it)
'F'
>>> next(it)
'i'
...

>>> next(it)
'C'
>>> next(it)
StopIteration
```

我们利用while以及迭代器的两个BIF来分析for语句的工作方式：

```python
>>> string = "FishC"
>>> it = iter(string)
>>> while True:
        try:
            each = next(it)
        except StopIteration:
            break
        print(each)

F
i
s
h
C
```

### 实现迭代器的两个魔法方法

实现迭代器的两个魔法方法有两个：`__iter__()`和`__next__()`。

| 方法         | 功能                                           |
|--------------|------------------------------------------------|
| `__init__()` | 一个容器如果是迭代器，给方法实现返回迭代器本身 |
| `__next__()` | 决定迭代的规则                                 |

```python
>>> class Fibs:
        def __init__(self):
            self.a = 0
            self.b = 1

        def __iter__(self):
            return self

        def __next__(self):
            self.a, self.b = self.b, self.a +self.b
            return self.a

>>> fibs = Fibs()
>>> for each in fibs:
        if each < 20:
            print(each)
        else:
            break

1
1
2
3
5
8
13
```
这个迭代器的唯一亮点就是没有终点，所以如果没有跳出循环，会不断迭代。可以通过修改`__next__()`来控制迭代的范围。

```python
>>> class Fibs:
        def __init__(self, n=20):
            self.a = 0
            self.b = 1
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b
            if self.a > self.n:
                raise StopIteration
                return self.a

>>> fibs = Fibs(10)
>>> for each in fibs:
        print(each)

1
1
2
3
5
8
```

### 问题

问题(1) 用while语句实现与以下for语句相同的功能：

```python
for each in range(5):
    print(each)
```

代码如下，

```python
n = 0
list = []
list.append(n)
it = iter(list)
while n < 6:
    n += 1
    list.append(n)
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)
```

答案代码，

```python
alist = range(5)   # 直接用range()生成一个列表

while True:
    try:
        print(next(it))
    except StopIteration:
        break
```

问题(2) 写一个迭代器，要求输出至今为止所有的闰年。如：

```python
>>> leapYears = LeapYear()
>>> for i in leapYears:
        if i >= 2000:
            print(i)
        else:
            break

2012
2008
2004
2000
```

提示：<br>
闰年判定法<br>
((year%4 == 0 and year%100! = 0)) or (year%400 == 0)

代码如下，

```python
import datetime

class LeapYear():
    def __init__(self, n = datetime.date.today().year):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):  
    # 注意的是__next__()方法总是描述下一次运行时即迭代中的单次行为。
        while (self.n % 400 != 0) and (self.n%4 != 0 and self.n%100 != 0):
            self.n = self.n - 1
        self.n -= 1
        return self.n+1  # return指令要在迭代描述的后面

leapYears = LeapYear()

for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break
```

答案代码如下，

```python
import datetime as dt

class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year)
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1

        temp = self.now
        self.now -= 1

        return temp
for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break
```

问题(3) 要求自己写一个MyRev类，功能与reversed()相同(内置函数reversed(seq)是返回一个迭代器，是序列seq的逆序显示)。例如：

```python
>>> myRev = MyRev("FishC")
>>> for i in myRev:
    print(i, end='')

ChsiF
```

代码如下，

```python
class MyRev():
    def __init__(self, seq):
        self.seq = seq
        self.len = len(seq)

    def seq2list(seq):
        list = []
        for i in seq:
            list.append(i)
        return list

    def __iter__(self):
        return self

    def __next__(self):
        temp = MyRev.seq2list(self.seq)
        if self.len == 0:
            raise StopIteration
        self.len -= 1
        # 这里可以直接return self.seq[self.len]，即字符串可以当做列表使用
        return temp[self.len]

myRev = MyRev("FishC")
for i in myRev:
    print(i, end='')
```















