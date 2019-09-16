---
layout: post
title: PCB1.1 - Squence unpacking, Star syntax, Use of deque, Use of yield, Keeping the Last N Items, Finding the Largest or Smallest N Items.
date: 2019-09-16 08:21:24.000000000 +09:00
---
#### About the title
Python - Cookbook study CHAPTER 1 - Data Strucutres and Algorithms - PCB1 for short
#### Something to say before everything begins
I plan to have a python cookbook study (David Beazley & Brian K. Jones). Aim to have a deeper understanding Python coding tech. And for better studying, I will make a notebook for studying process, I will upload this part to github, **if I inadvertently encroaching on the interests of anyone, please contact me in time, I will delete the related information immediately**.
## 1.1. Unpacking a Sequence into Separate Variables
> Unpack N-element tuple or sequence into a collection of N variables

```python
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
```
and if there is a mismatch in the number of elements, you'll get an error.
```python
ValueError: need more than 2 values to unpack
```

> throwaway variable name

If you want to discard certain values.

```python
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_ , shares, price, _ = data
```

## 1.2. Unpacking Elements from Iterables of Arbitrary Length
> Problems of "too many values to unpack"

Python use "star expressions" to address the problems when there are too many values to unpack.

```python
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
```

The unpacked variables will be returned as a list (including none)
```python
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
>>> name, email, *phone_numbers = user_record
>>> phone_numbers
['773-555-1212', '847-555-1212']
```
example 2 is to put the star expressions at the first one in the list.

```python
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)
```
and
```python
>>> *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
>>> trailing
[10, 8, 7, 1, 9, 5, 10, 3]
>>> current
3
```
> star syntax can be especially useful when iterating over a sequence of tupls of varying length. For example, a sequence of **tagged tuples**:

```python
records = [('ffo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

```
> star unpacking combined with certain kinds of string processing operations, such as splitting.

```python
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
>>> uname, *fields, homedir, sh = line.split(':')
>>> homedir
'/var/empty'
>>> sh
'/usr/bin/false'
```
> combined with a common throwaway variable name, such as _ or ign (ignored).

```python
>>> record = ('ACME', 50, 123.45, (12, 18, 2012))
>>> name, *_, (*_, year) = record
>>> name
'ACME'
>>> year
2012
```

> **Split a list into head and tail components** with star syntax

```python
>>> items = [1, 10, 7, 4, 5, 9]
>>> head, *tail = items
1
>>> tail
[10, 7, 4, 5, 9]
```

> apply the star unpacking to recursive algorithm <br>
(not recommand, because of Python is not strong about inherent recursion limit)
```python
>>> def sum(items):
        head, *tail = items
        return head + sum(tail) if tail else head
        
>>> sum(items)
36
```
## 1.3. Keeping the Last N Items

To keep a ***limited history*** of the last few items seen during iteration or during some other kind of processing. It's a perfect use for a ```cllections.deque```.
*** 
#### What is deque
Related codes and text translated from [HERE](https://blog.csdn.net/hellojoy/article/details/81281367).
1. Similirity with list
```python
# deque provides the same function with part of list
from collections import deque
d = deque()  #Create a 'deque' sequence
d.append(3)
d.append(8)
d.append(1)
>>> d
d = deque([3, 8, 1])
>>> len(d)
3
>>> d[0]
3
>>> d[-1]
1
```
2. The use of pop of deque
```python
>>> d = deque('12345')
d = deque(['1', '2', '3', '4', '5'])
>>> d.pop()
5
>>> d.leftpop()
1
```
3. The 'length limit fuction' of deque
```python
d = deque(maxlen = 3)
for i in range(30):
    d.append(str(i)):
        d.append(str(i))
>>> d
d = deque(['10', '11', '12'], maxlen = 3)
```
4. Extend the list to deque
```pyhon
d = deque([1, 2, 3, 4, 5])
d.extend([0])
>>> d
d = deque([1, 2, 3, 4, 5, 0])
d.extendleft([6, 7, 8])
>>> d
d = deque([8, 7, 6, 1, 2, 3, 4, 5, 0])
```
***
#### Yield?
Codes and text is tranlated [HERE](https://blog.csdn.net/mieleizhi0522/article/details/82142856)
Another thing to concern is the yield, here I find some explain about this function. <br>
1. At first, you can just think ```yield``` as ```return``` for easy understanding. And next, think it as a *generator*
```python
def foo():
    print('starting...')
    while True:
        res = yield 4 # <-**->
        print('res:', res)
g = foo()  # will not call foo(), because of the use of 'yield', but get a generator named with 'g'
print(next(g)) # only when call the next(), foo() will begin working**
print('x'*20)
print(next(g)) # Here start from the where previous  next(g) stop {the res valuing process}

>>>
starting...
4   # *** WHAT NEED TO GET ATTENTION: Here, 4 is not valued to res (<-**->), only print the yielded 4 (the returned 4) and then the program will stop
********************
res: None  # Here, next() begins from the {prviously stopped point of previous next(g) at <-**->} to value to res, however, at the first next(), 4 has been returned out, so here "res: None"
4     # Here because of the recyle of 'while', yield 4 again.
```
Here you may understand the relationship between yield and return, ```yield``` is a generator but not a function. There is a function of ```yield```, ```next()```, means which function to generate next step, and this time the fuction will continue from where previous ```next()``` stops, and when call the ```next()```, generator will not begin from ```foo()```, but from the previous stopped point. Then when meet the `yield` again, return the generated number, and this stip will stop.
<br>
2. Then another example about ```send()```
```python
def foo():
    print('starting...')
    while True:
        res = yield 4
        print('res:', res)
g = foo()
print(next(g))
print('*' * 20)
print(g.send(7))  # Here 7 has been valued to res <-**->

>>>
starting...
4
********************
res: 7   # Because before the second next() {Here, send() include the use of next()}, 7 has been valued to res.
4
```

Here, <-**-> The fucntion of ```g.send()``` includes ```g.next()```, and different from ```g.next()```, it can pass the value 7 to res.

3. Why need the yield?
<br>
If there is a very big data, like (0 ~ 1000).
```python
for n in range(1000):
    a = n
```
```range(1000)``` will generate a list with 1000 datas, not good for storage. Then you can use ```yield```:
```python
def foo(num):    # This will help make a very small list which will help for better storage.
    print('starting...')
    while num < 10:
        num = num + 1
        yield num
for n in foo(0):
    print(n)

>>>
starting...
1
2
3
4
5
6
7
8
9
10
```
It is the same with ```xrange(1000)```:
```python
for n in xrange(1000):
    a = n
```

However, in python3, ```range()``` is ```xrange()``` already. So you don't need to care about this.

***

After the preparing knowledge about ```yield``` as well as the ```deque```. The following code performs a simple text match on a sequence of lines and yields the matching line along with the previous N lines of context when found:

```python
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines # yield to make a generator
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for pline, prevlines in search(f, 'python', 5):
            print(pline, end = '')
            print('-' * 20)
```
When writing code to search for items, it is common to use a generator function involving ```yield```, this decouples the process of searching from the code that uses the reults. And using ```deque(maxlen=N)``` creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed.
<br>
More generally, a deque can be used whenever you need a simple queue structure. If you don't give it a maximum size, you get an unbounded queue that lets you append and pop items on either end. Adding or popping items from either end of a queue has O(1) complexity. This is unlike a list where inserting or removing items from the front of the list is O(N).

## 1.4. Finding the Largest or Smallest N Items
The ```heapq``` module has two functions, ```nlargest()``` and ```nsmallest()``` --- that do exactly what you want.
```python
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Print [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Print -4, 1, 2
```
A key parameter that allows them to be used with more complicated data structures is accepted.
```python
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': ...}
]

cheap = heapq.nsmallest(3, portfolio, key = lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s: s['price'])
```
1. If N is small compared to the overall size of the collection and you are looking for the N smallest or largest items.
They work by first converting the data into a list where items are ordered as a heap. For example,
```python
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> import heapq
>>> heap = list(nums)
>>> heapq.heapify(heap)
>>> heap
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
```
The most important feature of a heap, ```heap[0]``` is **always the smallest item. Moreover, subsequent items can be easily found using the ```heapq.heappop()``` method. For example, to find the three smallest items, you can do this:

```python
>>> heapq.heappop(heap)
-4
>>> heapq.heappop(heap)
1
>>> heapq.heappop(heap)
2
```
If you just want to find the single largest or smallest, ```max()``` and ```min()``` is faster.<br>
If N is about the same size as the collection itself, sort first and take a slice (```sorted(items)[:N]``` or ```sorted(items)[-N:]``` is faster).

## 1.5. Implemeting a Priority Queue
How to implement a queue that sorts items by a given priority and always returns the item with the highest priority on each pop operations.
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0    # index: to properly order items with the same priority level. <-**->

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))    # -priority: to get get the queue to sort items from highest priority to lowest priority.
        self._index += 1

    def pop(self):
        return heapq.heapop(self._queue)[-1]

>>> class Item:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return 'Item({!r})' format(self.name)   #???

>>> q = PriorityQueue()
>>> q.push(Item('foo'), 1)
>>> q.push(Item('bar'), 5)
>>> q.push(Item('spam'), 4)
>>> q.push(Item('grok'), 1)
>>> q.pop()
Item('bar')
>>> q.pop()
Item('spam')
>>> q.pop()
Item('foo')
>>> q.pop()
Item('grok')
```
Make data a ```priority, item``` tuple will help make a comparision between two items.
```python
a = Item('foo')
b = Item('bar')
a < b

>>>

TypeError: unorderable types: Item() < Item()
```
<br>
<-**-> Here index will function as a proper way to handle the problems when two items possess the same priority.
```python

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))

>>> a < b
True
>>> a < c
True
```






