---
layout: post
title: 汇编语言 7.10 不同寻址方式的灵活运用(2)
date: 2019-11-14 21:29:24.000000000 +09:00
tags: 汇编语言
---

### 7.10 不同寻址方式的灵活运用(2)

上次提到的代码会出现死循环，下面来分析具体原因以及如何解决。回顾代码：

```x86asm
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

          loop s    ;<++1++>

          add bx, 16
          loop s0   ;<++2++>
codesg ends
```
这个代码的问题在于当执行到<1>的位置时，cx的值已经跳出内部循环变为了0，而这时当程序运行到<2>，会执行cx = cx-1 = 0-1 = FFFF。

这里注意，不可以多用一个计数器，因为，loop指令默认的cx为循环计数器。

为了解决这个问题我们有三种解决方案：

1. 将外层循环的cx中的数值保存到dx中，然后当执行外层循环的loop指令时在释放cx的值。但是这种方法有局限性，因为通用寄存器数目有限，在本例中，si、cx、ax、bx在循环中要被使用。而cs:ip时刻指向当前指令，ds指向datasg也不能使用，只有dx,di,es,ss,sp,bp可以使用。这在一些复杂情况行不通。
2. 定义一个字形单元来储存外循环cx的值。即在datasg中多加一行`dw 0`, 将这个内存指定为`ds:[40H]`来代替第一种方案中通用寄存器的位置。但是如果需要保存多个数据的时候，必须记住数据放到了哪个单元中，容易混乱。
3. 利用栈，一般来说，在需要暂存数据的时候，我们哦度应该使用栈。任何程序在暂时存储信息时都用栈。代码如下：

```x86asm
codesg segment
  start:  mov ax, datasg
          mov ds, ax
          mov bx, 0

          mov cx, 4
     s0:  push cx    ;外层循环cx压栈
          mov si, 0         ;外层循环

          mov cx, 3
      s:  mov al, [bx+si]   ;内层循环
          and al, 11011111b
          mov [bx+si], al
          inc si

          loop s

          add bx, 16
          pop cx    ;从栈顶弹出cx，恢复外层循环的计数器
          loop s0
codesg ends
```

 
