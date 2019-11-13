---
layout: post
title: 汇编语言 7.10 不同寻址方式的灵活运用 (1)
data: 2019-11-13 15:52:24.000000000 +09:00
tags: 汇编语言
---

### 7.10 不同寻址方式的灵活运用(1)

之前有介绍过几种定位内存地址的方法（寻址方式）：
1. [idata]用一个**常量**来表示内存地址，可用于直接定义一个内存单元，注意的是，单独使用[idata]只能在debug中被正确识别，如果在masm中，需要表明[idata]对应的段，即```ds:[idata]```。
2. [bx]用一个**变量**来表示内存地址，可用于间接定位一个内存单元。其使用时不用表明对应的段，默认[bx]就是在ds中。
3. [bx+idata]。
4. [bx+si]。
5. [bx+si+idata]用两个变量和一个常量表示地址。

这有利于我们可以从更加**结构化**的角度来看待所要处理的数据。

> 问题1

编程，将datasg段中的每个单词的首字母改写为大写字母。

```x86asm
assume cs:codesg, ds:datasg
datasg segment
  db '1. file         '
  db '2. edit         '
  db '3. search       '
  db '4. view         '
  db '5. options      '
  db '6. help         '
datasg ends
```
这里可以观察数据结构，如图。

![figure1](/assets/201911/2019-11-13_16-05-36.png)

从图中可见，行需要进行6次循环操作（换行操作），列操作因为每一行需要改写的都是第3行，所以列处理为一个常数3。

处理过程如下：
```x86asm
    R=第一行的地址
    mov cx, 6
s:  改变R行，3列的字母为大写
    R=下一行的地址
    loop s
```
最终的代码段为：
```x86asm
codesg segment
  start:  mov ax, datasg
          mov ds, ax
          mov bx, 0

          mov cx, 6
      s:  mov al, [bx+3]
          and al, 11011111b
          mov [bx+3], al
          add bx, 16    ;通过对bx+16来换到下一行，对下一行[bx+3]进行定位
          loop s
codesg ends
```
这里应用了[bx+idata]的方法，对通过一个变量和一个常量组成的二位数组进行定位。

而如果我们遇到了需要两个变量来定位二维数组的情况又要如何处理呢？

> 问题2 编程，将datasg段中的每个单词改写为大写字母。

```x86asm
assume cs:codesg, ds:datasg
datasg segment
  db 'ibm             '
  db 'dec             '
  db 'dos             '
  db 'vax             '
datasg ends
```
首先我们来分析数据结构，如下图：

![figure2](/assets/201911/2019-11-13_16-16-29.png)

从图中我们可以看出，我们需要进行4*3次的二重循环才能将每一行里的每个单词都改写为大写。

这里需要使用两层循环对数据进行处理（外层循环和内层循环），处理方法如下：

```x86asm
    R=第一行的地址；
    mov cx, 4
s0: C=第一列的地址  ;外层循环
    mov cx, 3
 s: 改写R行，C列的字母为大写 ;内层循环
    C=下一列的地址；
    loop s
    R=下一行的地址
    loop s0
```

我们用bx来定位每一行的起始地址，用si定位要修改的列，用[bx+si]的方式来对目标单元进行寻址，代码段如下：

```
codesg segment
  start:  mov ax, datasg
          mov ds, ax
          mov bx, 0

          mov cx, 4
     s0:  mov si, 0         ;外层循环

          mov cx, 3
      s:  mov al, [bx+si]   ;内层循环
          and al, 11011111b
          mov [bx+si], al
          inc si

          loop s

          add bx, 16
          loop s0
codesg ends
```

但是这个代码是有问题的，因为在进行二重循环时，在第一次执行内层循环时，外层循环的cx就会被覆盖为内层循环的3。

下一个post将介绍如何解决这个问题。
