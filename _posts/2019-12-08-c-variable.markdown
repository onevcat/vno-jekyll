---
layout: post
title: C语言 变量
date: 2019-12-08 21:23:24.000000000 +09:00
tags: C语言
---
整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### 变量

变量和常量是程序处理的两种基本数据对象。通常会在内存中找一个位置来存放CPU要处理的数据，每个存放数据的位置都有一个“地址”，通过这个地址，CPU就可以找到并使用它们。**这个存放的位置就是变量**。

**变量名就是给一个数据的“地址“贴标签**。

### 变量命名的规则：

1. C语言变量名只能由**英文字母和数字或者下划线**来组成，**其他特殊字母不行**。
2. 变量名必须以**英文字母或者下划线开头**，**不能以数字开头**。
3. 便令名区分大小写。
4. 不能使用关键字来命名。

一下对C语言的关键字进行整理：

| 传统C语言(ANSI C) |
| auto              | break     | case     | char             | const       | continue        | default   | do     |
| double            | else      | enum     | extern           | float       | for             | goto      | if     |
| int               | long      | register | return           | short       | signed          | sizeof    | static |
| struct            | switch    | typedef  | union            | unsigned    | void            | volatile  | while  |
| C99标准           |
| inline            | restrict  | \_Bool   | \_Complex        | \_Imaginary |
| C11标准           |
| \_Alignas         | \_Alignof | \_Atomic | \_Static\_assert | \_Noreturn  | \_Thread\_local | \_Generic |


为变量指定名字后，还需要为变量指定”坑位”大小，即指定该变量即将存放的数据类型。以防浪费。

### C语言常用的基本数据类型

| 数据类型 | 说明                                     |
| char     | 字符型，占用一个字节                     |
| int      | 整型，通常反映了所用机器中整数的自然长度 |
| float    | 单精度浮点型                             |
| double   | 双精度浮点型                             |

代码说明，

```c
数据类型 变量名;
int a;      /* 在内存中找到一个整型大小的位置，并给它命名为a */
char b;     /* 在内存中找到一个字节大小的位置，并给它命名为b */
float c;    /*在内存中找到一个单精度浮点型数据大小的位置，并给它命名为c */
double d;   /*在内存中找到一个双精度浮点型数据大小的位置，并给它命名为d */
```
> PS：单精度浮点型用于存放小数点后位数比较小的浮点数，对于比较大的，要用更大的空间来存储，这就是双精度浮点型。

代码说明，

```c
//test.c
#include <stdio.h>
int main(void)
{
    float c;
    double d;

    c = 3.14;
    d = 3.141592653;

    printf("圆周率是：%.2f\n", c);
    printf("圆周率是：%11.9f\n", d);

    return 0;
}
```

