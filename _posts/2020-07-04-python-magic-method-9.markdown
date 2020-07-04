---
layout: post
title: python 魔法方法 (9) 生成器
date: 2020-07-04 15:00:24.000000000 +09:00
tags: python
---

整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### 什么是生成器

生成器（ iterator ）和迭代器（ generator ）是 Python 今年来引入的最强大的两个特性，但其不涉及魔法方法，可以巧妙避开类和对象，仅通过普通的函数即可实现。

生成器其实是迭代器的一种实现，其目的是为了使得 Python 更为简洁，因为迭代器需要我们去定义一个类和实现相关的方法，而生成器则只需要在普通的函数中加上一个`yield`语句即可。

生成器的发明使得 Python 模仿**协同程序**的概念得以实现。

### 协同程序

**协同程序**就是可以运行的独立函数调用，函数可以**暂定**或者**挂起**，并从程序离开的地方继续或者重新开始。

对于一个普通的 Pyhton 函数，一般是从函数的第一行代码开始执行，结束于 return 语句、异常或者函数所有语句执行完毕（`return None`）。一旦函数将控制权交还给调用者，就意味着全部结束。函数中做的所有工作以及保存在局部变量中的数据都将丢失。再次调用这个函数时，一切都将从头创建。

Pyhton 是通过生成器来实现类似于协同程序的概念：生成器可以暂时挂起函数，并保留函数的局部变量等数据，然后再次调用它的时候，从上次暂停的位置基序执行下去。

```python
>>> def myGen():
	print('生成器被执行。')
	yield 1
	yield 2

>>> myG = myGen()
>>> next(myG)
生成器被执行。
1
>>> next(myG)
2
>>> next(myG)
StopIteration # 异常报错
```

利用`next()`函数当超出函数范围时，就是抛出 StopIteration 异常。

由于`for`循环包含`next()`，所以也可以用来对生成器产生作用。

```python
>>> for i in my Gen():
	print(i)

生成器被执行。
1
2
```

### 生成器表达式

#### 列表推导式 ( list comprehensions )

```python
>>> [i*i for i in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

相当于,

```python
list = []
for i in range(10):
	list1.append(i * i)
```

再举个例子，

```python
>>> [i for i in range(100) if not (i % 2) and i % 3]
```

相当于

```python
list1 = []
for i in range(100):
	if not (i % 2) and i % 3:
		list1.append(i)
```

#### 字典推导式 （ dictionary comprehension ）

```python
>>> {i:i % 2 == 0 for i in range(10)}
{0: True, 1:False, 2: True, ...}
```

#### 结合推导式 （ set comprehension ）

```python
>>> {i for i in [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8]}
{1, 2, 3, 4, 5, 6, 7, 8}
```

但需要注意的是：

1. **不存在字符串推导式**，

	 ```python
	 >>> "i for i in 'I love FishC.com!'"
	 "i for i in 'I love FishC.com!'"
	 ```
2. 元组推导式即位生成器表达式（ generator expressions ）本身。

	 ```python
	 >>> (i for i in range(10))
	 <generator object <genexpr> at 0x03135300>
	 ```
	 
	 ```
	 >>> e = (i for i in range(10))
	 0
	 >>> next (e)
	 1
	 >>> next(e)
	 2
	 >>> for each in e:
			 print(each)
	 3
	 4
	 5
	 6
	 7
	 8
	 9
	 ```

3. 生成器表达器可以作为函数的参数使用，可以直接写推导式，而不必加小括号：

	 ```python
	 >>> sum(i for i in range(100) if i % 2)
	 2500
	 ```

	 等同于，

	 ```python
	 >>> sum((i for i in range(100) if i % 2))
	 2500
	 ```

### 作业

> 作业 1：

```python
"""
要求实现一个功能与 reversed()相同 （内置函数 reversed(seq)）是返回一个迭代器，是序列seq的逆序显示）的生成器。例如：

>>> for i in myRev("FishC")
        print(i, end='')
>>> ChsiF
"""
def myRev(data):

	for index in range(len(data) - 1, -1, -1):
	yield data[index]

if __name__ == '__main__':
	for i in myRev("FishC"):
		print(i, end='')
```

> 作业 2：

```python
"""
10 以内的素数之和是：2 + 3 + 5 + 7 = 17，那么请编写程序，计算 2000000 以内的素数之和？
"""

import math


def primeIF(number):
    """  # 这个算法效率太低
    for i in range(number):
        if i == 0 or i == 1 or i == number:
            continue
        else:
            if number % i == 0:
                return False
            else:
                continue
    return True
    """
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True


def primeCOUNT(InputNumber, number=2):
    for i in range(InputNumber - 1):
        if primeIF(number):
            yield number
        number += 1


def primeSUM(InputNumber):
    SUM = 0
    for i in primeCOUNT(InputNumber):
        SUM += i
    print(SUM)


if __name__ == '__main__':
    primeSUM(2000000)
```

### 关于 yield 与 Generator 提高篇

#### 协同（协同程序）与子例程

`return`隐含的意思是函数正在将执行代码的控制权返回给函数被调用的地方。而`yield`的隐含意思是控制权的转移是临时和自愿的，我们的函数将来还会收回控制权。

为了更好的理解生成器所解决的问题，始终记住我们需要解决的问题：**生成值的序列**。

**一个生成器会生成值**，生成器函数返回生成器的迭代器。作为一个迭代器，生成器必须要定义一些方法，其中一个就是`__next__()`。同迭代器，我们可以使用`next()`函数来获取下一个值。

下面引入一个例子，

```python
>>> def simple_generator_function():
	yield 1
	yield 2
	yield 3
```

这里有两个简单的方法来使用它：

```python
>>> for value in simple_generator_function():
	print(value)
1
2
3

>>> our_generator = simple_generator_function()
>>> next(our_generator)
1
>>> next(our_generator)
2
>>> next(our_generator)
3
```

当一个生成器函数调用`yield`，生成器函数的“状态”会被冻结。如果永远不调用`next()`，`yield`保存的状态就被无视了。

在 PEP 342 中加入了将值传给生成器的支持，能让生成器在单一语句中实现，生成一个值，接受一个值，或同事生成一个值并接受一个值。

```python
if is_prime(number):
	number = yield number
number += 1
```

通过这种方式，我们可以在每次执行 `yield` 的时候为 number 设置不同的值。

### `next()`和`send()`用法

+ 如果`send`不携带参数，那么`send(None)` 和`next()`的作用的相同的

	```
	>>> def a():
		print('aaa')
		p = yield '123'
		print(p)
		print('bbb')

	>>> r = a()
	>>> print(next(r))
	# 等同于print(r.send(None))
	# 二者，使用next(r) 和 r.send(None)输出的结果都是 123
	# 另外注意，这里的p变量的值都是None
	
	aaa
	123
	```


+ 如果`send`的参数不是`None`，则是把`yield xx`当成一个表达式，且把`send`的参数的值赋给了p；而后的操作同next一样，如：

	```python
	>>> def a():
		print('aaa')
		p1 = yield '123'
		print('bbb')
		if (p1 == 'hello'):
			print('p1是send传过来的')
			p2 = yield '234'
			print(p2)

	>>> r = a()
	>>> next(r)
	>>> r.send('hello')

	aaa # 执行第一次 `next()` 在第一次打印 `aaa`，在 p1 = yield '123' 处暂停
	bbb # 执行第二次 `next()` ，打印'bbb' 和 'p1是send传过来的'
	p1是send传过来的
	```

> 实例：找出比某个数的等比级数大的最小素数（ 例如 10，我们要生成比 10，100，1000，10000 ... 大的最小素数）。我们从 `get_primes` 开始：

```python
def print_successive_primes(iterations, base=10):
	prime_generator = get_primes(base)
	prime_generator.send(None)
	for power in range(itarations):
		print(prime_generator.send(base ** power))

def get_primes(number):
	while True:
		if is_prime(number):
			number = yield number
		number += 1
```

本例中的注意事项：

1. 我们打印的是 generator.send 的结果，这是没问题的，因为`send`在发送数据给生成器的同时还返回生成器通过`yield`生成的值（就如同生成器中 `yield` 语句做的那样）

2. 当你用 `send` 来“启动”一个生成器时，必须发动`None`。这不难理解，根据刚才的描述，生成器还没有走到第一个`yield`语句，如果我们发生一个真实的值，这时是没有人去“接收”它的。一旦生成器启动了，我们就可以像上面那样发送数据了

### 总结

+ generator 是用来产生一系列值的

+ `yield` 则像是 generator 函数的返回结果

+ `yield` 唯一所做的另一件事就是保存一个 generator 函数的状态

+ generator 就是一个特殊类型的迭代器

+ 和迭代器相似，我们可以通过使用 `next()` 来从 generator 中获取下一个值

+ 通过隐式地调用 `next()` 来忽略一些值







