---
layout: post
title: python 类和对象 (5) 一些相关的BIF
date: 2019-11-18 14:30:24.000000000 +09:00
tags: python
---
整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)
### 对类或者对象从属判断的内置函数
#### issubclass(class, classinfo)

如果第一个参数(class)是第二个参数(classinfo)的一个子类，返回True否则返回False

1. 一个类被认为是其自身的子类
2. classinfo可以是一个类对象组成的元组，只要class是其中任何一个候选类的子类，则返回True
3. 其他情况会抛出TypeError

#### isinstance(object, classinfo)

如果第一个参数(object)是第二个参数(classinfo)的实例对象，则返回True，否则返回False。

1. 如果object是classinfo 的子类的一个实例，也符合条件
2. 如果第一个参数不是对象，则永远返回False
3. classinfo可以是类对象组成的元组，只要object是其中任何一个候选类的子类，则返回True
4. 如果第二个参数不是类或者由类对象组成的元组，会抛出一个TypeError异常

### 用于访问对象的属性
#### hasattr(object, name)

attr即attribute的缩写，属性的意思。hasattr()函数的作用就是测试一个对象里是否有指定的属性。

第一个object是对象，第二个name是属性名。

#### getattr(object, name[, default])

返回对象指定的属性值，如果指定的属性不存在，则返回default的值；若没有设置default参数，抛出AttributeError。  **注意属性要用字符串的形式给出**


#### setattr(object, name, value)

与getattr()对应，setattr()可以设置对象中指定属性的值，如果指定的属性不存在，则会新建属性并赋值。 **注意属性要用字符串的形式给出**

#### delattr(object, name)

与setattr()相反，delattr()用于删除对象中指定的属性如果属性不存在，则抛出AttributeError。 **注意属性要用字符串的形式给出**


#### property(fget=None, fset=None, fdel=None, doc=None)

```python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._X

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property")
```

这样做可以避免大范围对代码中的变量getx, setx, delx进行修改，直接操作x的属性即可。

另外property()也可以用来使用属性修饰符创建描述符：

```python
class C:
    def __init__(self):
        self._x = None
    
    @property 
    del x(self):
        # I'm the 'x' property
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```

注意：三个处理`_x`属性的方法名要相同(参数不同)


