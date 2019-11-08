---
layout: post
title: 汇编语言 实验5 第一部分
date: 2019-11-06 22:49:24.000000000 +09:00
tags: 汇编语言
---

代码1
```x86asm
assume cs:code, ds:data, ss:stack

data segment
    dw 0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h
data ends

stack segment
    dw 0, 0, 0, 0, 0, 0, 0, 0
stack ends

code segment

start: mov ax, stack
       mov ss, ax
       mov sp, 16

       mov ax, data
       mov ds, ax

       push ds:[0]
       push ds:[2]   ;这里的代码可以实现正向push
       pop ds:[2]
       pop ds:[0]

       mov ax, 4c00h
       int 21h

code ends
end start
```
设代码段地址为X, 数据段地址为X-2, 栈段地址为X-1.

代码2

```x86asm
assume cs:code, ds:data, ss:stack

data segment
    dw 0123h, 0456h
data ends

stack segment
    dw 0, 0
stack ends

code segment

start: mov ax, stack
       mov ss, ax
       mov sp, 16

       mov ax, data
       mov ds, ax

       push ds:[0]
       push ds:[2]   ;这里的代码可以实现正向push
       pop ds:[2]
       pop ds:[0]

       mov ax, 4c00h
       int 21h

code ends
end start
```

这时的我们发现代码段地址，数据段地址以及栈段地址较第一个代码没有发生改变。

定义段中数据占N个字节，则程序加载后，改段实际占有的空间为：

$$16(N/16 + 1)$$

> 说明如果数据长度没有达到16个字节依然占用一整个段地址空间。

代码3
```x86asm
assume cs:code, ds:data, ss:stack

code segment

start: mov ax, stack
       mov ss, ax
       mov sp, 16

       mov ax, data
       mov ds, ax

       push ds:[0]
       push ds:[2]   ;这里的代码可以实现正向push
       pop ds:[2]
       pop ds:[0]

       mov ax, 4c00h
       int 21h

code ends

data segment
    dw 0123h, 0456h
data ends

stack segment
    dw 0, 0
stack ends

end start
```

设代码段地址为X，数据段地址为X+3，栈段地址为X+4, 因为将data和stack代码放在代码后面。所以数据段地址和栈段地址也同样会发生改变。

> 如果将end start 改为end, 前三个代码中只有第三个能够正常执行，因为代码段正好在前面，直接编译不会出错。


