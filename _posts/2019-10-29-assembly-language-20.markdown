---
layout: post
title: 汇编语言 5.7 5.8 安全空间，段前缀的使用，附加段
date: 2019-10-29 23:36:24.000000000 +09:00
tags: 汇编语言
---

### 5.7 一段安全的空间

1. 我们需要直接向一段内存中写入内容。
2. 这段内存空间不应存放系统或其他程序的数据或代码，否则写入操作很可能引发错误。
3. DOS方式下，一般情况，**0:200~0:2ff**(256字节)空间中没有系统或其他程序的数据或代码。
4. 以后，我们需要直接向一段内存中写入内容时，就是用0:200~0:2ff这段空间。

### 5.8 段前缀的使用

我们可以利用段前缀来简化代码，如下面这个例子：

将内存ffff:0~ffff:b单元中的数据复制到0:200~0:20b单元中。

```x86asm
assume cs:code
code segment
    mov bx, 0
    mov cx, 12

s:  mov ax, 0ffffh
    mov ds, ax
    mov dl, [bx]

    mov ax, 0020h
    mov ds, ax
    mov [bx], dl

    inc bx
    loop s

    mov ax, 4c00h
    int 21h

code ends
end
```

可以通过添加另外一个段寄存器es(附加段)来实现减少ds在循环中的设置次数：

```x86asm
assume cs:code
code segment
    mov ax, 0ffffh
    mov ds, ax

    mov ax, 0020h
    mov es, ax

    mov bx, 0

    mov cx, 12

s:  mov dl, [bx]
    mov es:[bx], dl
    inc bx
    loop s

    mov ax, 4c00h
    int 21h

code ends
end
```
