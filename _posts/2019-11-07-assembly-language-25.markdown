---
layout: post
title: 汇编语言 实验5 第二部分
date: 2019-11-07 23:22:24.000000000 +09:00
tags: 汇编语言
---

代码1、编写代码段代码，将a段和b段中的数据依次相加，将结果存到c段中。

```x86asm
assume cs:code

a segment
    db 1, 2, 3, 4, 5, 6, 7, 8
a ends

b segment
    db 1, 2, 3, 4, 5, 6, 7, 8
b ends

c segment
    db 0, 0, 0, 0, 0, 0, 0, 0
c ends

code segment

start:  mov ax, a
        mov ds, ax
        mov ax, b
        mov es, ax

        mov bx, 0

        mov cx, 8
        
s:      mov al, ds:[bx]    ;将ax中的数据移到段寄存器al中
        add es:[bx], al    ;将al中的a数据与es中的b相加
        inc bx
        loop s

        mov ax, c
        mov ds, ax

        mov bx, 0

        mov cx, 8

s0:     mov al, es:[bx]
        mov ds:[bx], al
        inc bx
        loop s0

        mov ax, 4c00h
        int 21h

code ends
end start
```

代码二、编写代码段中的代码，用push指令将a段中的前8个字型数据，逆序存储到b段中。

```x86asm
assume cs:code

a segment
    dw 1, 2, 3, 4, 5, 6, 7, 8, 9, 0ah, 0bh, 0ch, 0dh, 0eh, 0fh, 0ffh
a ends

b segment
    dw 0, 0, 0, 0, 0, 0, 0, 0
b ends

code segment

start:  mov ax, a
        mov ds, ax
        mov ax, b

        mov bx, 0
        mov ss, ax
        mov sp, 16  ;设置栈顶指向b:16

        mov cx, 8
s:      push ds:[bx]
        add bx, 2   ;注意push每次两个字节
        loop s

        mov bx, 0
        mov ss, ax
        mov sp, 0

        mov cx, 8
s0:     pop ds:[bx]
        add bx, 2
        loop s0

code ends
end start
```
