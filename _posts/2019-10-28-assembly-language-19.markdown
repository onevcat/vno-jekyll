---
layout: post
title: 汇编语言 5.5 5.6 loop与[bx]的联合应用 段前缀
date: 2019-10-28 21:56:24.000000000 +09:00
---

#### loop 和[bx]的联合应用

问题： 计算ffff:0~ffff:b单元中的数据和，结果存储在dx中。

分析上述问题，

1. 运算结构是否会超出dx存储范围。不会，因为ffff:0~ffff:b内存单元中每一位都是字节型数据，累加12个不会超出ds的最大存储范围(65535)。
2. 因为ffff:0~ffff:b数据是8位的，不能直接加到16位寄存器dx中。
3. 如果直接将ffff:0~ffff:b中的数据累加到dl中，而设置$(dh)=0$，12个8位数据全部累加到8位数据的dl中，很可能会造成进位丢失。

总结问题：

1. (dx)=(dx)+内存中的8位数据 ---> 会不匹配
2. (dl)=(dl)+内存中的8位数据 ---> 会发生越界问题

解决办法：

用一个16位寄存器作为中介，把内存单元中的每一位都复制到16位寄存ax中。

数学表达：

$$\begin{array}{c}\\ {\mathrm{sum}=\sum_{\mathrm{X}=0}^{0bH}\left(\mathrm{ffffh}^{*} 10 \mathrm{h}+\mathrm{X}\right)}\end{array}$$

代码如下：
```x86asm
assume cs:code
code segment

    mov ax, 0ffffh
    mov ds, ax
    mov bx, 0
    mov dx, 0
    mov cx, 12
s:  mov al, [bx]
    mov ah, 0
    add dx, ax
    inc bx
    loop s

    mov ax, 4c00h
    int 21h

code ends
end
```
#### 5.6 段前缀

1. mov ax, ds:[bx]
2. mov ax, cs:[bx]
3. mov ax, ss:[bx]
4. mov ax, es:[bx]
5. mov ax, ss:[0]
6. mov ax, cs:[0]

这些出现在访问内存单元的指令中，用于指明内存单元的段地址的"ds:"...被称为**段前缀**。


