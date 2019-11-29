---
layout: post
title: python 魔法方法 (3) 反运算 一元操作符
date: 2019-11-28 22:21:24.000000000 +09:00
tags: python
---
整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)
### 反运算

执行反运算时首先观察加法规则：

$$ a + b $$

这个加法中，首先来确定谁是加法的主动一方，谁是被加一方。a 是主动实施加法的一方，而b则是被加一方。而反运算描述的就是被加一方的相关的算数性质。

如下：

```python
calss Nint(int):
    def __rsub__(self, other)
        return int.__sub__(other, self)

>>> a = Nint(5)
>>> b = Nint(3)
>>> a + b    #当存在主动加法施加的a时，将会调用a的__add__()
8
>>> 1 + b    #当第一个数是常数，不具备__add__()时，就只会调用b的被加一方的__radd__()方法
-2
```
这里要注意`other`和`self`的顺序，如下，

```python
class Nint(int):
    def __rsub__(self, other):
        return int.__sub__(self, other)

>>> a = Nint(5)
>>> 3 - a
2
```

除了例子中的`__rsub__()`方法外，还有以下的反运算相关的魔法方法，

| 魔法方法                       | 含义                          |
|--------------------------------|-------------------------------|
| \_\_radd\_\_(self, other)      | 定义加法行为：\+              |
| \_\_rsub\_\_(self, other)      | 定义减法行为：\-              |
| \_\_rmul\_\_(self, other)      | 定义乘法行为：\*              |
| \_\_rtruediv\_\_(self, other)  | 定义真除法行为：/             |
| \_\_rfllordiv\_\_(self, other) | 定义整数除法：//              |
| \_\_rmod\_\_(self, other)      | 定义取模算法：%               |
| \_\_rpow\_\_(self, other)      | 定义当被power()调用算法：\*\* |
| 以下为汇编行为                 |
| \_\_rlshift\_\_(self, other)   | 定义按位左移位行为：<<        |
| \_\_rrshift\_\_(self, other)   | 定义按位右移位行为：>>        |
| \_\_rand\_\_(self, other)      | 定义按位与操作行为：&         |
| \_\_rxor\_\_(self, other)      | 定义按位异或操作行为：^       |
| \_\_ror\_\_(self, other)       | 定义按位或操作行为：\|        |

> 需要注意的是，**以上操作都在相应操作数不支持相应操作时被调用**

### 一元操作符

Python 支持的一元操作符：

| 一元操作符       | 含义                       |
|------------------|----------------------------|
| \_\_neg\_\_()    | 表示负号行为               |
| \_\_pos\_\_()    | 表示正号行为               |
| \_\_abs\_\_()    | 表示取绝对值时被调用的行为 |
| \_\_invert\_\_() | 表示定义按位取反的行为     |

> 问题：

(1) 如何在继承的类中调用基类的方法?

```python
class Derived(Base):
    def meth(self):
        super(Derived, self).meth()
```

(2) 如果继承的基类是动态的，如何部署代码？

可以先为基类定义一个别名，在类定义时，使用别名代替你要继承的基类。如此，当想要改变基类的时候，只需要修改给别名赋值的那个语句即可。**当资源是视情况而定的时候，这个方法很好用**。代码示例如下,

```python
BaseAlias = BaseClass

class Derived(BaseAlias):
    def meth(self):
        BaseAlias.meth(self)
        ...
```

(3) 举例说明静态，并指出使用类的静态方法的优点

```python
class C:
    @staticmethod # 该修饰符表示static()是静态方法
    def static(arg1, arg2, arg3):
        print(arg1, arg2, arg3):
    
    def nostatic(self):
        print('nostatic
```

静态方法最大的优点，就是不会绑定到**实例对象上，节省开销**。

```python
>>> c1 = C()
>>> c2 = C()
# 静态方法只在内存中生成一个，节省开销
>>> c1.static is C.static
True
>>> c1.nostatic is C.nostatic
False
>>> c1.static
<function C.static at 0x03001420>
>>> c2.static
<function C.static at 0x03001420>    #注意这里c1和c2实例对象的静态方法地址相同
# 以下是动态方法，注意与静态方法的比较，开销很大
>>> c1.nostatic
<bound method C.nostatic of <__main__.C object at 0x03010590>>
>>> c2.nostatic
<bound method C.nostatic of <__main__.C object at 0x032809D0>>
>>> C.nostatic
<function C.nostatic at 0x038D2B8>
```
> 需要注意，静态方法不需要self参数，因此即使是使用对象去访问，self参数也无法传输进去

(4) 定义一个类，当实例化该类时，自动判断传入了多少参数，并显示出来。效果如下，

```python
>>> c = C()
并没有传入参数
>>> c = C(1, 2, 3)
传入3个参数，分别是: 1, 2, 3
```
代码如下：

```python
class ShowNum:
    def __init__(self, *args):
        if not args:
            print('并没有输入参数')
        else:
            print('传入%d个参数'% len(args), end='')
            for each in args:
                print(each, end=' ')
```







