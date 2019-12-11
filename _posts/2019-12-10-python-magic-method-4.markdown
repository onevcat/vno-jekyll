---
layout: post
title: python 魔法方法 (4) 简单定制
date: 2019-12-10 22:24:24.000000000 +09:00
tags: python
---

整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### 简单定制

下面来做一个案例，要求如下：

1. 定制一个计时器的类
2. start和stop方法代表启动定时和停止计时
3. 假设计时器对象t1，print(t1)和直接调用t1均显示结果
4. 当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
5. 像个计时器对象可以相加：t1+t2
6. 只能使用提供的有限资源完成

需要用到下面的资源：

1. 使用time模块的localtime方法获取时间
2. time.localtime返回struct\_time的时间格式
3. \_\_str\_\_()和\_\_repr\_\_()魔法方法
4. 其中，\_\_str\_\_()和\_\_repr\_\_()魔法方法的用法如下：

```python
# __str__()的代码示例

>>> class A:
        def __str__(self):
            return "A"
>>> a = A()
>>> print(a)
A
>>> a
>>> <__main__.A object at 0x03260F30>

# __repr__()的代码示例

>>> class B:
        def __repr__(self):
            return "B"

>>> b = B()
>>> b
B
```

首先谈一下—\_\_str\_\_()的方法，在打印一个实例化对象时，打印的其实和是一个对象的地址。而通过\_\_str\_\_()函数就可以帮助我们打印对象中具体的属性值，因为在python中调用print函数打印实例化对象时就会调用\_\_str\_\_()的方法，如果\_\_str\_\_()中有返回值，就会打印其中的返回值。

而\_\_repr\_\_()本身功能为显示自身的属性，在实例化以后，调用自身就会打印出属性。

```python
import time as t

class Mytimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "还未开始计时"
        self.last_list = []
        self.begin = 0    # 这里如果使用self.start = 0，
                          # 会因为在__init__()方法中使用
                          # 与类中方法相同的名的属性，而覆盖方法
        self.end = 0

    def start(self):
        self.begin = t.localtime()
        self.prompt = "请调用stop()开始计时"
        print("计时开始")

    def stop(self):
        self.end = t.localtime()
        self.calc()
        print("计时结束")

    def calc(self):
        self.last_list = []
        self.prompt = "总共运行了"
        for i in range(6):
            self.list.append(self.stop[i] - self.start[i])
            self.prompt += str(self.last_list[i])

    def __str__(self):
        return self.prompt

    __repr__ = __str__    # 实现print(实例对象)和
                          # 直接调用实例对象都会
                          # 显示结果

    __add__(self, other):
        prompt = '总共运行了'
        result = []
        for i in range(6):
            result.append(self.result[i] + other.result[i])
            if result[i]:
                prompt += (str(result[i]) + self.unit[i])
                
        return prompt
```




