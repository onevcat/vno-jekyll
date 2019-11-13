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

> 问题0 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人和1个小孩的平日票价。

1. 平日票价100元
2. 周末票价为平日的120%
3. 儿童半票

代码如下：

```python
class Ticket():
    def __init__(self, child = False, weekend = False):
        self.price = 100
        if weekend:
            self.inc1 = 1.2
        else:
            self.inc1 = 1
        if child:
            self.inc2 = 0.5
        else:
            self.inc2 = 1
    def calculatePrice(self, num):    #注意类中函数必须要绑定self参数, 不然后面实力对象无法正确调用
        return self.price*self.inc1*self.inc2*num
adult = Ticket()
child = Ticket(child = True)
print('2个成人与1一个小孩的票价为%.2f元' % (adult.calculatePrice(2)+child.calculatePrice(1)))
```

> 要按要求定义一个乌龟类和一个鱼类并尝试编写游戏。

1. 假设游戏场景为范围(x, y)为0 <= x <= 10, 0 <= y <= 10
2. 游戏生成1只乌龟和10条鱼
3. 他们的移动方法均随机
4. 乌龟的最大移动能力是2(可以随机选择移动1还是移动2)，鱼的最大移动能力是1
5. 当移动到场景边缘，自动向反方向移动
6. 乌龟初始化体力为100
7. 乌龟每移动一次，体力消耗1
8. 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
9. 鱼暂不计算体力
10. 当乌龟体力为0或者鱼数量为0时，游戏结束

代码如下：
```python
import random as r
legalX = [0, 10]
legalY = [0, 10]

class Turtle():
    def __init__(self):
        self.HP = 100
        self.x = r.randint(legalX[0], legalX[1])
        self.y = r.randint(legalY[0], legalY[1])
    def move(self):
        self.newX = self.x + r.choice([2, 1, 0, -1, -2])
        self.newY = self.y + r.choice([2, 1, 0, -1, -2])
        if self.newX > 10:
            self.newX = legalX[1] - (self.newX - legalX[1])
        elif self.newX < 0:
            self.newX = legalX[0] + (legalX[0] - self.newX)
        else:
            self.x = self.newX
        if self.newY > 10:
            self.newY = legalY[1] - (self.newY - legalY[1])
        elif self.newY < 0:
            self.newY = legalY[0] + (legalY[0] - self.newY)
        else:
            self.y = self.newY

        self.HP -= 1
        return (self.x, self.y)

    def eat(self):
        self.HP += 20
        if self.HP > 100:
            self.HP = 100

class Fish():
    def __init__(self):
        self.x = r.randint(legalX[0], legalX[1])
        self.y = r.randint(legalY[0], legalY[1])
    def move(self):
        self.newX = self.x + r.choice([1, 0, -1])
        self.newY = self.y + r.choice([1, 0, -1])
        if self.newX > 10:
            self.newX = legalX[1] - (self.newX - legalX[1])
        elif self.newX < 0:
            self.newX = legalX[0] + (legalX[0] - self.newX)
        else:
            self.x = self.newX
        if self.newY > 10:
            self.newY = legalY[1] - (self.newY - legalY[1])
        elif self.newY < 0:
            self.newY = legalY[0] + (legalY[0] - self.newY)
        else:
            self.y = self.newY
        return (self.x, self.y)    #注意使用return来返回数值的方法

turtle = Turtle()
fish = []

for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼被吃完了，游戏结束！')
        break
    
    if not turtle.HP:
        print('乌龟累死了，游戏结束!')
        break
    
    pos = turtle.move()    #这里的while可以反复调用实例对象turtle的move方法

    #在迭代器中删除列表元素是非常危险的，经常会出现意想不到的效果，因为迭代器是直接饮用列表的数据进行引用的
    #针对这一问题，我们通常把列表拷贝给迭代器，然后对原列表进行删除就不会有问题了。
    #关于在迭代器中直接删除列表的具体风险。比如我在列表[0, 1, 2, 3]中，迭代器中直接删除了[0], 下次循环时i += 1, 但这个列表为[1, 2, 3]，而i = 1, 指向的第二项, 会跳过[1]

    for each in fish:
        if new_fish.move() == pos:
            turtle.eat()
            fish.remove(each)
            print('有条鱼被吃了！')
```
