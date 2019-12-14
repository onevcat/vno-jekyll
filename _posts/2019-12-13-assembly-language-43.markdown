---
layout: post
title: 汇编语言 10.7-10.10 call和ret的配合使用 mul 模块化 参数和结果传递的问题
date: 2019-12-14 16:52:24.000000000 +09:00
tags: 汇编语言
---

### 10.7 call和ret的配合使用

问题(1) 下面程序返回前，bx中的值是多少？

```x86asm
assume cs:code
code segment
start: mov ax, 1
       mov cx, 3
       call s
       mov bx, ax
       mov ax, 4c00h
       int 21h
    s: add ax, ax
       loop s
       ret
code ends
end start
```
分析程序运行的过程：
1. CPU将call s 指令的机器码读入，IP指向了call s后的指令`mov bx, ax`，然后CPU执行call s指令，将当前的IP值(指令`mov bx, ax`的偏移地址)压栈，并将IP的改变为标号处s处的偏移地址。
2. CPU从标号s处开始执行指令，loop循环完毕后，(ax)=8；
3. CPU将ret指令的机器码读入，IP指向了ret指令后的内存单元，然后CPU执行ret指令，从栈中弹出一个值(即call s先前压入的`mov bx, ax`指令的偏移地址)送入IP中。则CS:IP指向指令`mov bx, ax`。
4. CPU从`mov bx, ax`开始执行指令，直至完成。

程序返回前，(bx)=8。可以看出，从标号s到ret的程序段的作用是计算2的N次方，计算前，N的值由cx提供。

再从机器码的角度观察一下栈的变化。

代码示例，
stack segment
  db 8 dup (0) 1000:0000 00 00 00 00 00 00 00 00
  db 8 dup (0) 1000:0008 00 00 00 00 00 00 00 00
stack ends

code segment:

| 编号 | 代码                | 地址      | 机器码   |
|------|---------------------|-----------|----------|
| 1    | start:mov ax, stack | 1001:0000 | B8 00 10 |
| 2    | mov ss, ax          | 1001:0003 | 8E D0    |
| 3    | mov sp, 16          | 1001:0005 | BC 10 00 |
| 4    | mov ax, 1000        | 1001:0008 | B8 E8 03 |
| 5    | call s              | 1001:000B | E8 05 00 |
| 6    | mov ax, 4c00h       | 1001:000E | B8 00 4C |
| 7    | int 21h             | 1001:0011 | CD 21    |
| 8    | s:add ax, ax        | 1001:0013 | 03 C0    |
| 9    | ret                 | 1001:0015 | C3       |

code ends
end start

分析：

1. 首先当执行1~3行代码，会对栈进行清空，这是指针指向栈顶：<br>
1000:0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00(指针)<br>
2. 第5行执行call指令`E8 05 00`后，IP = 000EH，并将此IP压入栈中：<br>
1000:0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0E(指针) 00<br>
并行跳转(IP)=(IP)+0005=0013H
3. CPU从cs:0013H处(即标号s处)开始执行
4. 到9后执行`ret`指令后，机器码`C3`，进行`pop IP`，执行后，栈中情况如下：<br>
1000:0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0E 00(指针)<br>
5. CPU回到cs:000EH处，继续执行。

从上面的例子与讨论中，我们可以发现，可以写一个具有一定功能的程序段，我们称其为子程序，在需要的时候，用call指令转去执行。call指令转去子程序之前，call指令后面的指令的地址将存储在栈中，所以可在子程序的后面使用ret指令，用栈中的数据设置IP的值，从而转到call指令后面的代码处继续执行。

这样，我们可以利用call和ret来实现子程序的机制。先通过写一段C语言代码，然后进行反汇编：

```c
#include <stdio.h>

void love(void);

int main()
{
    printf("aaaaaaaa\n");
    love();
}

void love()
{
    printf("Then, bbbbbbb\n");
}
```
反汇编结果如下，

```x86asm
test main:
    0x100000f20 <+0>:  pushq  %rbp
    0x100000f21 <+1>:  movq   %rsp, %rbp
    0x100000f24 <+4>:  subq   $0x10, %rsp
    0x100000f28 <+8>:  leaq   0x63(%rip), %rdi          ; "aaaaaaaa\n"
    0x100000f2f <+15>: movb   $0x0, %al
    0x100000f31 <+17>: callq  0x100000f70               ; symbol stub for: printf
    0x100000f36 <+22>: movl   %eax, -0x4(%rbp)
    0x100000f39 <+25>: callq  0x100000f50               ; love at main.c:14
    0x100000f3e <+30>: xorl   %eax, %eax
    0x100000f40 <+32>: addq   $0x10, %rsp
    0x100000f44 <+36>: popq   %rbp
    0x100000f45 <+37>: retq
```

```x86asm
test love:
    0x100000f50 <+0>:  pushq  %rbp
    0x100000f51 <+1>:  movq   %rsp, %rbp
    0x100000f54 <+4>:  subq   $0x10, %rsp
    0x100000f58 <+8>:  leaq   0x3d(%rip), %rdi          ; "Then, bbbbbbb\n"
    0x100000f5f <+15>: movb   $0x0, %al
    0x100000f61 <+17>: callq  0x100000f70               ; symbol stub for: printf
    0x100000f66 <+22>: movl   %eax, -0x4(%rbp)
    0x100000f69 <+25>: addq   $0x10, %rsp
    0x100000f6d <+29>: popq   %rbp
    0x100000f6e <+30>: retq
```

从以上反汇编结果总结具有子程序的源程序的框架如下：

```x86asm
assume cs:code
code segment
  main: :
        :
        call sub1       ;调用子程序sub1
        :
        :
        mov ax, 4c00h
        int 21h

  sub1: :               ;子程序sub1
        :
        call sub2       ;调用子程序sub2
        :
        :
        ret             ;子程序返回至main

  sub2: :
        :
        :
        ret             ;子程序返回至sub1
code ends
end main
```

### 10.8 mul 指令

mul指令总结起来共有三种形式，

1. 8位数与8位数相乘：<br>
这两个8位数一个放在AL中，另一个放在8位reg或内存字节单元中。<br>
结果默认放在ax中。因为8位和8位的乘法不会超过16位。
2. 16位数与16位数相乘：<br>
这两个16位数一个放在AX中，另一个放在16位reg或内存字单元中。<br>
结果高位默认在DX中存放，低位在AX中放。
3. 8位数与16位相乘：<br>
其中一个8位数按16位处理，并按16位数乘法规则进行。

代码示例，

```x86asm
mul byte ptr ds:[0]
```
含义：

$(ax)=(al)*((ds)*16+0)$

```x86asm
mul word ptr [bx+si+8]
```
含义：

结果的低16位存放在 $(ax)=(ax)*((ds)*16+(bx)+(si)+8)$

结果的高16位存放在 $(dx)=(ax)*((ds)*16+(bx)+(si)+8)$

举例说明，

(1) 计算100\*10

100和10小于255，可以做8位乘法，程序如下，

```x86asm
mov al, 100
mov bl, 10
mul bl
```
结果：(ax) = 1000 (03E8H)

(2) 计算100\*10000

100小于255，可10000大于255，所以必须做16位乘法，程序如下，

```x86asm
mov ax, 100
mov bx, 10000
mul bx
```
结果：(ax)=4240H，(dx)=000FH  (F4240H = 1000000)

### 10.9 模块化程序设计

call与ret指令共同支持了汇编语言编程中的模块化设计。在实际编程中，程序模块化是必不可少的。因为现实的问题比较复杂，对现实问题进行分析时，把它转化成为相互联系、不同层次的子问题，是必须的解决方法。而call与ret指令对这种分析方法提供了程序实现上的支持。利用call和ret指令，我们可以用简捷的方法，实现多个相互联系、功能独立的子程序来解决一个复杂的问题。

**以下，我们来看一下子程序设计中的相关问题和解决方法。**

### 10.10 参数和结果传递问题

子程序一般都要**根据提供的参数处理一定的事务**，处理后，**将结果（返回值）提供给调用者**。

**其实，我们讨论参数和返回值传递的问题，实际上就是在探讨，应该如何存储子程序需要的参数和产生的返回值**。



