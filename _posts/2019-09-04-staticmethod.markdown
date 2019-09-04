---
layout: post
title: Python - The Staticmethod Binding
date: 2019-09-04 16:45:24.000000000 +09:00
---
## Something about parameter binding
Function is stored as the attribute of class, as you can see in the code followed.
```python
class Pizza(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size
print(Pizza.get_size)
```
You can find the result like this, `<unbound method Pizza.get_size>`. It shows the attribute of the function `get_size` is not bound to any class. And if we try to make this fuction work like this.
```python
Pizza.get_size() 
```
Will traceback `unbound method get_size() must be called with Pizza instance as first argument`. And it is clear that, if we can't call this function because it's not bound to any instance of Pizza. And we need to make it like this.
```python
Pizza.get_size(Pizza(42))
or
Pizza(42).get_size()  #self parameter will pass to Pizza(42), this instance
or
m = Pizza(42).get_size
m()
```
If you want to see where the bound function binds to, try this.
```python
m = Pizza(42).get_size
m.__self__
```
I will give some codes about staticmethod of Python
## Some codes to learn Staticmethod of Python
```python
class Pizza:
    def __init__(self):
        self.cheese = 3
        self.vegetables = 4
    @staticmethod # Here if you delete this code, program will go well too, because it runs as dynamic method
    def mix_ingredients(x, y):
        return x + y
    def cook(self):
        return Pizza.mix_ingredients(self.cheese, self.vegetables)
print(Pizza.mix_ingredients(1, 2))
print(Pizza().cook())
```
Here `@staticmethod` is a marker to begin the staticmethod which lead the defination of mix_ingredients a static fuction. When we make it a staticmethod, we can make the instance x, y not self. In this way, when we have the function, we don't need to input `Pizza().mix_ingredients(1, 2)` again, input `Pizza.mix_ingredients(1, 2)`is OK. To make a comparation, we give another function, `cook`, which is not a statcimethod, and in this situation, we must define a instance to `Pizza()`, and only in this way, the function of self will pass to `Pizza()`.

## The class method
See this code.
```python
import math
class Pizza(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    @staticmethod
    def compute_circumference(radius):
        return math.pi * (radius ** 2)
    @classmethod
    def compute_volume(cls, height, radius):
        return height * cls.compute_circumference(radius)

print(Pizza.compute_volume(2, 3))
```
What is a class method, it's a function bound to class not object. And the first parameter must be the class itself. And when the function is bound to cls, if we del the base_class, the classmethod will still work well. The other side, the staticmethod will not be that lucky, it will call a error as seen followed:
```python
# Using the staticmethod
class Pizza(object):
    key = ['A']
    @staticmethod
    def sta(new_key):
        Pizza.key.append(new_key)
        return Pizza.key
print(Pizza.sta('B'))
del Pizza
#Output will be error:  
> NameError: name 'Pizza' is not defined

# Using the classmethod
class Pizza(object):
    key = ['A']
    @classmethod
    def Cls(cls, new_key):
        cls.new_key = new_key
        cls.key.append(new_key)
        return Pizza.key
print(Pizza.Cls('B'))
del Pizza
# Everything will go well (maybe)
```
## The abstract method
The abstract method is defined in a base_class, but will not get any achievement until this function is inherited to the subclass.
```python
import abc
class BasePizza(object):
    __meta__ = abc.abstractmethod
    @abc.abstractmethod
    def get_radius(self):
        {Method that should do something}
BasePizza()
# it will make typeerr
> TypeError: Can't instantiate abstract class BasePizza with abstract mehtods get_radius
```
Ok let's make an exercise mixed with all of the methods:
```python
import abc
class BasePizza(object):
    __metaclass__ = abc.ABCMeta
    ingredient = ['cheese']
    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
    {Returns the ingredient list}}
        return cls.ingredient

class Pizza(BasePizza):
    def get_ingredients(self):
        return['egg'] + super(Pizza, self).get_ingredients()
a = Pizza()
print(a.get_ingredients())
```




