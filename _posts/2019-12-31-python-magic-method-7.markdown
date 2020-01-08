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

### 与定制容器类型相关的魔法方法及含义

在Python中，像序列类型(如列表、元组、字符串)或映射类型(如字典)都属于容器类型。

下面讲一下与定制容器有关的一些协议：

* 如果希望定制的容器**不可变**，则只需要定义\_\_len\_\_()和\_\_getitem\_\_()方法。
* 如果希望地址的容器是**可变的**，除了\_\_len\_\_()和\_\_getitem\_\_()方法，还需要定义\_\_setitem\_\_()和\_\_delitem\_\_()两个方法。

下表列举了与定制容器有关的魔法方法及含义。

| 魔法方法                          | 含义                                                  |
|-----------------------------------|-------------------------------------------------------|
| \_\_len\_\_(self)                 | 定义当被len()函数调用时的行为，即返回容器中元素的个数 |
| \_\_getitem\_\_(self, key)        | 定义获取容器中指定元素时的行为，相当于self[key]       |
| \_\_setitem\_\_(self, key, value) | 定义设置容器中指定元素的行为，相当于self[key]=value   |
| \_\_delitem\_\_(self, key)        | 定义删除容器中指定元素的行为，相当于del self[key]     |
| \_\_iter\_\_(self)                | 定义当迭代容器中的元素的行为                          |
| \_\_reversed\_\_(self)            | 定义当被reversed()函数调用时的行为                    |
| \_\_contains\_\_(self, item)      | 定义当使用成员测试运算符(in或not in)时的行为          |

实例，编写一个不可变的自定义列表，要求记录列表中的每个元素被访问的次数。

```python
class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        # 使用列表的下标作为字典的键，注意不能用元素作为字典的键
        # 因为列表的不同下标可能有数值相等的元素，但字典不可能有两个相同的键
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):    # 这里可以注释掉，不用定义__len__()方法
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

>>> c1 = CountList(1, 3, 5, 7, 9)
>>> c2 = CountList(2, 4, 6, 8, 10)
>>> c1[1]
3
>>> c2[1]
4
>>> c1[1] + c2[1]
7
>>> c1.count
{0: 0, 1: 2, 2: 0, 3: 0, 4: 0}
>>> c2.count
{0: 0, 1: 2, 2: 0, 3: 0, 4: 0}
```

### 练习

根据上面的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数。并且支持append()、pop()、extand()原生列表所拥有的方法。

要求：

1. 实现获取、设置和删除一个元素的行为(删除一个元素的时候对应的计数器也会被删除)
2. 增加counter(index)方法，返回index参数所指定的元素记录的访问次数
3. 实现append()、pop()、remove()、insert()、clear()和reverse()方法(重写这些方法时要注意考虑计数器的对应改变)

自己的代码如下，

```python
class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.counterkey = []
        for i in range(len(self.values)):
            self.counterkey.append(0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.counterkey[key] += 1
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]
        del self.counterkey[key]

    def append(self, added_value):
        self.values.append(added_value)
        self.counterkey.append(0)

    def reverse(self):
        return self.values.reverse(), self.counterkey.reverse()

    def insert(self, insert_pos, inserted_value):
        self.values.insert(insert_pos, inserted_value)
        self.counterkey.insert(insert_pos, 0)

    def pop(self):
        return self.values.pop(), self.counterkey.pop()

    def clear(self):
        self.values.clear()
        self.counterkey.clear()

    def remove(self, remove_value):
        remove_pos = self.values.index(remove_value)
        self.values.remove(remove_value)
        del self.counterkey[remove_pos]


c1 = CountList(1, 2, 3, 4, 5)
print(c1[1])
print(c1.counterkey)
del c1[1]
print(c1.counterkey)
c1.append(4)
print(c1.counterkey)
print(c1[-1])
print(c1.counterkey)
print(c1[1])
c1.reverse()
print(c1.counterkey)
print(c1[1])
print(c1.counterkey)
c1.insert(1, 8)
print(c1.counterkey)
print(c1[1])
print(c1.counterkey)
c1.pop()
print(c1[-1])
print(c1.counterkey)
print(c1.values)
c1.remove(3)
print(c1.counterkey)
print(c1.values)
c1.clear()
print(c1.counterkey)

# 输出结果
2
[0, 1, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0, 0]
4
[0, 0, 0, 0, 1]
3
[1, 0, 0, 1, 0]
5
[1, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0]
8
[1, 1, 1, 0, 1, 0]
3
[1, 1, 1, 0, 2]
[4, 8, 5, 4, 3]
[1, 1, 1, 0]
[4, 8, 5, 4]
[]
```

答案该出的代码类继承并严重依赖其父类(list)的行为，并按要求重写了一些方法，代码如下，

```python
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key

    def counter(self, key):
        return self.count[key

    def append(self, value):
        self.count.append(0)
        super().append(value

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key

    def remove(self, value):
        key = super().index(value)
        del slef.count[key]
        super().remove(value

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value

    def clear(self):
        self.count.clear()
        super().clear(

    def reverse(self):
        self.count.reverse()
        super().reverse()
```
