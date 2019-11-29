---
layout: post
title: python 类和对象 (1)
date: 2019-11-7 16:16:24.000000000 +09:00
tags: python
---
整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)
### 对象 = 属性 + 方法

代码示例：

```python
class Turtle:
    
    # Python 中的类名(class)约定以大写字母开头
    # 特征的描述成为属性(attribute)，在代码层面来看就是变量

    color = 'green'
    weight = 10
    legs = 4
    shell = True

    # 方法(method)就是函数，通过调用这些函数来完成工作

    def run(self):
        print("我正在很努力的往前爬。。。")

    def bite(self):
        print("咬死你咬死你！")
```

### 实例(instance)与实例对象(instance object)

上面代码定义了对象的属性(特征)以及方法(行动)，但还不是一个完整的对象，将**定义的这些称为类(class)**。

需要使用类来创建一个真正的对象，这个**对象就称为这个类的一个实例(instance)**, 也称为**实例对象(instance object)**。

如以下代码：

```python
tt = Turtle()  # 这里注意类要以大写字母开头
```

> 类名约定以答谢字母开头，函数用小写字母开头。<br>
赋值本身不是必需的，但如果没有把创建好的实例对象赋值给一个变量，那这个实例对象就没办法使用，因为**没有任何引用指向这个实例**，最终会被垃圾收集机制回收。

代码如下：
```python
tt.climb()
我正在很努力的向前爬。。。
```

### python面向对象编程的三个要素

#### 第一个要素，封装

对象封装了属性，也就是封装了变量。也封装了方法，也就是函数。并成为了一个独立性的模块。

#### 第二个要素，多态

不同对象对于不同的方法响应不同的行动。

如下代码：

```python
class A:
    def fun(self):
        print("I'm A")

class B:
    def fun(self):
        print('I'm B)

a = A()
b = B()
```
虽然行动名称相同(```fun(self)```)，但由于对象的不同，会触发不同的行动。

#### 第三个要素， 继承

子类自动共享父类之间数据和方法的机制。

如下代码：

```python
class Mylist(list):   # 这里Mylist 继承了list的方法
    pass

list2 = Mylist()
list2.append(1)
```
### 课后练习

> 1.函数和方法有什么区别？<br>
函数和方法几乎完全一样，但方法默认有一个self参数。

> 2.按要求定义矩形类并生成实例对象<br>
属性：长，宽<br>
方法：设置长和宽 setRect(self)，获得长和宽 getRect(self)，获得面积 getArea(self)

```python
class Rect:
    length = 5
    width = 4

    def setRect(self):
        print('Please input the Width & Length!')
        self.length = float(input('Width of the Rect is: '))
        self.width = float(input('Length of the Rect is: '))
    
    def getRect(self):
        print('Length is %.2f' % self.length, \n
              'Width is %.2f' % self.width)
    
    def getArea(self):
        Area = self.length * self.width
        print('The area of the Rect is %.2f' % Area)

rectA = Rect()
rectA.setRect()
rectA.getRect()
rectA.getArea()
```

