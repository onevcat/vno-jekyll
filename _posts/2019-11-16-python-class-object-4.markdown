---
layout: post
title: python 类和对象 (4) 组合 Mixin 类，类对象与实例对象 绑定
date: 2019-11-16 21:58:24.000000000 +09:00
tags: python
---

### 组合

所谓”组合”，可以理解为相对于继承来讲的一个概念。有些时候，利用多重继承本身除了存在风险的同时，在有些时候，如果类本身并不存在明显的相互继承关系，强行继承会很别扭。比如定义了两个类，小鸟和老鹰后，我们想定义一个新的类，天空，天空中包含小鸟和老鹰，奈何天空和小鸟和老鹰本身并不存在继承关系，这时就适合用组合来解决这个问题。

当执行组合时，**我们将需要的类放进目的类中进行实例化**，就可以实现组合，例如代码：

```python
class Bird():
    def __init__(self, x):
        self.num = x

class Eagle():
    def __init__(self, x):
        self.num = x

class Sky():
    def __init__(self, x, y):
        self.bird  = Bird(x)
        self.eagle = Eagle(y)

def print_num(self):
    # 这里print的对象为self.bird.num以及self.eagle.num，为与当前类无继承关系的类的实例化对象的属性。
    print("天空中共有小鸟 %d只，老鹰 %d只" % (self.bird.num, self.eagle.num))
```

将几个不是很有继承关系的（横向关系）的几个类放在一起，我们称之为**组合**。如果几个类之间的纵向关系，我们就可以使用继承。

除了组合以外，还有另外一种很流行的编程模式，叫做Mixin。

### Mixin

Mixin编程是一种开发模式，是一种将多个类中的功能单元的进行组合的利用的方式。**通常Mixin不作为任何类的基类，也不关心与什么类一起使用，而是在运行时动态的同其他零散的类一起组合使用**。

其具有以下有点：

1. 可以在不修改任何源代码的情况下，对已有类进行扩展；
2. 可以保证组件的划分；
3. 可以根据需要，使用已有的功能进行组合，来实现“新”类；
4. 很好的避免了类继承的局限性，因为新的业务需要，可能就意味着需要创建新的子类

代码示例：

```python
class A:
    def GetA(self):
        print('a')
class B:
    def GetB(self):
        print('b')
  # 这里应用的是python的多继承机制
class C(A, B): pass

a = A()
b = B()
c = C()
c.GetA()
>>>a
c.GetB()
>>>b

  # 下面使用Mixin的方法

class A:
    def GetA(self):
        print('a')
class B:
    def GetB(self):
        print('b')
  # 这里应用的是python的多继承机制
  # 下面使用Mixin的方法

class C(A, B):
    pass

C.__bases__ = (A, B)
a = A()
b = B()
c = C()
c.GetA()
c.GetB()

 # 结果输出
>>>
a
b

 # 利用__base__，我们可以通过C.__bases__来进行控制继承
 # 如下

C.__base__ = (A, object)    # 如果元祖中只有一个元素在后面加object
a = A()
b = B()
c = C()
c.GetA()
c.GetB()

 # 输出结果
AttributeError: 'C' object has no attribute 'GetB'
```

我们也可以通过`__base__ += calss`来对目标类进行拓展。如下代码：

```python
class A:
    def GetA(self):
        print('a')

class B:
    def GetB(self):
        print('b')

class C(A):
    pass

C.__base__ += (B, object)
a = A()
b = B()
c = C()
c.GetA()
c.GetB()

 # 结果输出
>>>
a
b
```

### 类、类对象和实例对象

我们在类中定义的属性是静态的变量，相当于C语言的static关键字，**类的属性是与类对象进行绑定，并不会依赖与任何实例对象**。

那么下面就会衍生出一个问题，如果实例对象中属性的名字和类对象的属性名重复了会怎么样呢？

```python
>>> class C:
        count = 0

>>>a = C()
>>>b = C()
>>>c = C()
>>>print(a.count, b.count, c.count)
0 0 0
>>>c.count += 10
>>>print(a.count, b.count, c.count)
0 0 10
>>> C.count += 100
>>> print(a.count, b.count, c.count)
100 100 10
```

这个例子说明，在实例对象c中的count属性进行了赋值后，就会覆盖掉类对象C的count属性。

由此我们有以下结论：

1. 一般不要再类里面定义出所有属性和方法，应该多利用继承和组合机制来进行扩展。
2. 使用骆驼命名法，`CamelCase`。

### 绑定

**Python严格要求方法需要有实例才能被调用**，这种限制就是绑定。

如下代码：
```python
>>>class A:
       def printA():
           print('A')
>>>A.printA()  # 这里相当于直接调用类对象的方法
A
```
但是一旦将类对象实例化以后，根据类实例化后的实例对象无法调用里面的函数。

```python
>>>B = A()
>>>B.printA()
TypeError: printA() takes 0 positional arguments but 1 was given
```
实际上当我们调用类的实例对象的方法时，`B.printA()`的完整代码为`B.printA(B)`，由于Pyhton的绑定机制，**这里自动把B对象作为第一个参数传入，所以会出现TypeError，print()不需要参数，但是实际上传入了一个参数B。

下面我们利用__dict__来查看对象所有用的属性，来更好地理解。

```python
>>>class C:
       def setXY(self, x, y):
           self.x = x
           self.y = y
       def printXY(self):
           print(self.x, self.y)

>>>d = C()
 #使用__dict__查看对象所拥有的属性
>>>d.__dict__
{}
>>>C.__dict__
mappingproxy({'__module__': '__main__', 'setXY': <function C.setXY at 0x00000166C7E2A378>, 'printXY': <function C.printXY at 0x00000166C7E2A400>, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakreg__': <attribue '__weakref__' of 'C' objects>, '__doc__': None})

```
 __dict__属性由一个字典组成，字典中仅有实例对象的属性，不显示属性和特殊属性(魔法方法)，键表示的是属性名，值代表属性相应的数据值。

当我们给d加入新属性，而且这两个属性仅属于实例对象自身。
```python
>>>d.setXY(4, 5)
>>>d.__dict__
{'x': 4, 'y': 5}
```

因为self参数，当实例对象d调用setXY方法时，传入参数d，使得self.x = 4, self.y = 5等同于d.x = 4, d.y = 5。

再次强调这个属性只属于实例对象本身，即使我们删除掉之前定义的C类，同样可以获得执行：

```python
>>>del C
>>>d.printXY()
4 5
```
注意，一般只要用实例属性，而不要用类属性，因为类属性通常只用来跟踪与类相关的值。

**类中的属性与方法是静态的，只有在程序退出后，才会被释放。**

#### 问题

> 类对象在什么时候产生。

当你这个类定义完时，类定义就编程类对象，可以直接通过“类名.属性”或者“类名.方法名（）”引用或使用相关的属性或方法。

> 类中的`self.x = x`是实例属性

> 定义一个栈类，用于模拟一种后进先出的（LIFO）特性的数据结构。至少需要有以下方法：

| 方法名    | 含义                                    |
|-----------|-----------------------------------------|
| isEmpty() | 判断当前栈是否为空（返回True或者False） |
| push()    | 往栈的顶部压如一个数据项                |
| pop()     | 往栈顶弹出一个数据项(并在栈中删除       |
| top()     | 显示当前栈顶的一个数据                  |
| bottom()  | 显示当前栈底的一个数据                  |

自己的代码：

```python
class Stack():
    def __init__(self):
        self.LIST = []

    def isEmpty(self):
        if self.LIST == []:
            return 'TRUE'
        else:
            return 'FALSE'
    def push(self, data):
        self.LIST.append(data)
    def pop(self):
        self.LIST.pop()
    def top(self):
        return self.LIST[-1]
    def bottom(self):
        return self.LIST[0]

data1 = 1
data2 = 2
data3 = 3
a = Stack()
print(a.isEmpty())
a.push(data1)
a.push(data2)
print(a.isEmpty())
print(a.top())
print(a.bottom())
a.push(data3)
print(a.top())
a.pop()
print(a.top())
```
答案代码：

```python
class Stack:
    def __init__(self, start=[]):    #考虑到了栈的初始情况
            self.stack = []
            for x in start:
                self.push(x)
    def isEmpty(self):
        return not self.stack    #简洁的判断栈是否为空的方法，优于两个if

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print('警告，栈为空!')    #考虑到了栈空的情况
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print('警告，栈为空！')
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]
```

