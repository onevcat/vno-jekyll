---
layout: post
title: python 正则表达式
date: 2020-07-23 12:59:24.000000000 +09:00
tags: python
---

整理自[鱼 C 论坛](https://fishc.com.cn) 

## python 正则表达式 `re` 模块

python 通过 `re` 模块来实现

```python
>>> import re
>>> re.research(r'FishC', 'I love FishC.com')
<_sre.SRE_Match object; span=(7, 12), match = 'FishC'>
```

> `search()` 方法用于在字符串中搜索正则表达式模式第一次出现的 **位置** 。

这种方法类似于 `find()`方法，

```python
>>> "I love FishC.com!".find('FishC')
7
```

注意事项：

+ 第一个参数是正则表达式模式，也就是要描述的搜索规则，需要使用原始字符串来写

+ 返回的范围下标从 0 开始。找不到则返回 None

## 通配符

和字符串 `find()` 方法相比较，正则表达式较强的地方在于可以使用通配符。

> python 正则表达式中的通配符 `.` 可以匹配除了换行符之外的任何字符

```python
>>> re.search(r'.', 'I love FishC.com!')
<_sre.SRE_Match object; span=(0, 1), match = 'I'>

>>> re.search(r'Fish.', 'I love FishC.com!')
<_sre.SRE_Match object; span=(7, 12), match = 'FishC'>
# 这里 '.' 只替代一个字母
```

## 反斜杠

```python
>>> re.search(r'.', 'I love FishC.com!')
<_sre.SRE_Match object; span=(0, 1), match = 'I'>

>>> re.search(r'\.', 'I love FIshC.com!')
<_sre.SRE_Match object; span=(12, 13), match = '.'>
```

> 正则表达式中，反斜杠用来剥夺元字符的特殊能力。元字符就是拥有特殊能力的符号，如 `.`

## 字符类

为了表示一个字符的范围，可以创建一个字符类。使用中括号将任何内容包起来就是一个字符类，**它的含义是只要匹配这个字符类中的任何字符，结果就算做匹配**。

```python
>>> re.search(r'[aeiou]', 'I love 123 FishC.com')
<_sre.SRE_Match object; span=(3, 4), match = 'o'>
```

同时也可以使用 `-` 做字母或数字范围的搜索：

```python
# 在规定字母顺序范围内搜索
>>> re.search(r'[a-z]', 'I love 123 FishC.com!')
<_sre.SRE_Match object; span=(2, 3), match = 'l'>

# 在规定数字顺序范围内搜索
>>> re.search(r'[0-2][0-5][0-5]', 'I love 123 FishC.com!')
<_sre.SRE_Match object; span=(7, 10), match = '123'>
```

有以下两个注意事项：

+ `re.search` 对于字符的搜索区分大小写
+ `re.search` 只能遍历字符串，并将满足条件的第一个结果返回

## 重复匹配

使用 `{}` 大括号对元字符实现重复匹配功能：

```python
>>> re.search(r'ab{3}c', 'abbbc')
<_sre.SRE_Match object; span=(0, 5), match = 'abbbc'>

# 重复次数可以规定范围
>>> re.search(r'ab{3, 5}c', 'abbbbbc')
<_sre.SRE_Match object; span=(0, 7), match = 'abbbbbc'>
>>> re.search(r'ab{3, 5}c', 'abbbbbc')
<_sre.SRE_Match object; span=(0, 5), match = 'abbbc'>
```

对于重复匹配有以下注意事项：

+ 正则表达式匹配的是 **字符串而非数字** ，所以在匹配大于 10 的数字时需要额外考虑
+ 可以利用 `{0, 1}` 来解决大于 10 数字不好搜索的问题

例如利用正则表达式匹配 ip 地址：

```python
>>> re.search(r'(([0-1]{0, 1}\d{0, 1}\d|2[0-4]\d|25[0-5])\.){3}([0-1]{0, 1}\d{0, 1}\d|2[0-4]\d|25[0-5])', 'other192.168.1.1other'])
<_sre.SRE_Match object; span=(5, 16), match = '192.168.1.1'>
```

## 特殊符号

Python 3 正则表达式的特殊符号及用法见 [re regular expression 文档](https://docs.python.org/3.8/library/re.html)。

## 元字符

### 管道符 `|` 

管道符 `|` 类似于逻辑或操作，

```python
>>> re.search(r"Fish(C|D)", "FishC")
<_sre.SRE_Match object; span=(0, 5), match = 'FishC'>
>>> re.search(r"Fish(C|D)", "FishD")
<_sre.SRE_Match object; span=(0, 5), match = 'FishD'>
```

### 脱字符 `^`

脱字符 `^` 表示匹配字符串需要开始的位置，**只有在目标字符串的开头时才会发生匹配** 。

```python
>>> re.search(r"^FishC", "I love FishC.com!")
>>> re.search(r"^FishC", "FishC.com!")
<_sre.SRE_Match object; span=(0, 5), match = 'FishD'>
```

### 美元符 `$`

则表示匹配字符串的结束位置，也就是说，只有目标字符串出现在末尾才会匹配：

```python
>>> re.search(r"FishC$", "FishC.com"
```

<++>
















