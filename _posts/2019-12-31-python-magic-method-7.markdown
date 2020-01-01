---
layout: post
title: python 魔法方法 (7) 定制序列
date: 2019-12-31 15:46:24.000000000 +09:00
tags: python
---

整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### 定制容器与协议(protocol)

成功地实现容器定制，需要先了解一下协议(protocol)。Python中的协议与其他编程语言中的接口很相似，它规定哪些方法必须定义。然后，在Python中的协议就不那么正式。事实上，Python的协议更像是一种指南。

这有点像Python极力推崇的鸭子类型。

### 鸭子类型(duck typing)复习

鸭子类型(duck typing)是动态类型的一种风格。这种风格中，一个对象有效的语义，不是由**继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定**。
即关注的不是对象的类型本身，而是它是如何使用的。在使用鸭子类型的语言中，一个函数可以接受一个任意类型的对象，并调用它的方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的方法的对象，都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。
鸭子类型通常得益于不测试方法和函数中的参数的类型，而是依赖文档、清晰的代码和测试来确保正确的使用。

从静态类型语言转向动态类型语言的用户通常试图添加一些静态的(在运行之前的)类型检查，从而影响了鸭子类型的益处和可伸缩性，并约束了语言的动态特性。

代码示例，

```python
class Duck:
    def quack(self):
        print("呱呱呱!")

    def feathers(self):
        print("这个鸭子拥有灰白灰白的羽毛。")

class Person:
    def quack(self):
        print("你才是鸭子，你们全家人都是鸭子！")

    def feathers(self):
        print("这个人穿着一件羽绒大衣。")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()
```

in\_the\_forest() 函数对参数duck只有一个要求：就是可以实现quack()和feathers()方。然而Duck类和Person类都实现了quack()和feathers()方法，因此它们的实例对象donald和john都可以用作in\_the\_forest()的参数。这就是鸭子类型。

我们可以看出，鸭子类型给予Python这样的动态语言以多态。但是这种多态的实现完全由程序员来约束强制实现(文档、清晰的代码和测试)，并没有语言上的约束(如C++ 继承和虚函数)。因此这种方法即灵活，又提高了对程序员的要求。



