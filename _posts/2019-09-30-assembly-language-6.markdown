---
layout: post
title: 汇编语言 Debug的用法
date: 2019-09-30 09:39:24.000000000 +09:00
---
#### 什么是Debug

Debug是DOS、Windows都提供的实模式（8086方式）程序的调试工具。使用它，可以查看CPU各种寄存器中的内容、内存的情况和在及其码级跟踪程序的运行。

#### Debug的使用

1. R命令查看、改变CPU寄存器的内容；
2. D命令查看内存中的内容；
3. E命令改写内存中的内容；
3. U命令将内存中的机器指令翻译成汇编指令；
4. T命令执行一条机器指令；
5. A命令以汇编指令的格式在内存中写入一条及其指令。

#### 指令详解

> R命令：

```assembly
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=138C  ES=138C  SS=138C  CS=138C  IP=0100   NV UP EI PL NZ NA PO NC
138C:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD
```
即查看当前寄存器内容。同时R命令还可以修改寄存器的值，
```assembly
-r ax
AX 0000
:
```
可以在```:```后面添加需要改变的值，即可修改通用寄存器的值，如

```assembly
-r ax
AX 0000
:1111

-r
AX=1111  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=138C  ES=138C  SS=138C  CS=138C  IP=0100   NV UP EI PL NZ NA PO NC
138C:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD
```

同理，R命令也可以修改段寄存器CX，

```assembly
-r CS
CS 138C
:1400
-r ip
IP 0100
:1111
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=138C  ES=138C  SS=138C  CS=1400  IP=1111   NV UP EI PL NZ NA PO NC
138C:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD
```
通过这个方法可以用来改变Debug程序的指针。

然后可以通过T命令来执行该指针区间内的指令，可以用D命令来查看当前指针所在内存区间。

但是在本例中，内存为空，使用T命令也不会对命令进行执行，我们可以通过A命令来在此内存空间中添加需要添加的命令。

例如在138C:011F添加代码，

```assembly
-a
138C:0100 mov ax, 4e20
138C:0103 add ax, 1416
138C:0106 mov bx, 2000
138C:0109 add ax, bx
138C:010B add bx, ax
138C:010D add ax, bx
138C:010F mov ax, 001A
138C:0112 mov bx, 0026
138C:0115 add al, bl
138C:0117 add ah, bl
138C:0119 add bh, al
138C:011B mov ah, 0
138C:011D add al, bl
138C:011F add al, 9c
138C:0121
```
> PS: 注意IP偏移地址的增加，在机器码中，例如```mov ax, 4E20H```的机器码为```b8 20 4e```，这时偏移地址增加3，而```mov bx, ax```的及其码为```89 c3```，偏移地址增加2。

这时通过D命令查看相对应的地址区间，就能查看到你输入代码的机器码及ascii码。

```assembly
-d 138c:0100
138c:0100  B8 20 4E 05 16 14 BB 00-20 01 D8 89 C3 01 D8    (ASCII 码)
...
```

使用U命令可以机器指令翻译为汇编指令。

```assembly
-u 138c:0100
138C:0100 mov ax, 4e20
138C:0103 add ax, 1416
138C:0106 mov bx, 2000
138C:0109 add ax, bx
138C:010B add bx, ax
138C:010D add ax, bx
138C:010F mov ax, 001A
138C:0112 mov bx, 0026
138C:0115 add al, bl
138C:0117 add ah, bl
138C:0119 add bh, al
138C:011B mov ah, 0
138C:011D add al, bl
138C:011F add al, 9c
```
之后可以用T命令对上面代码进行逐行实现。每实现一条指令，对应IP都会发生改变。

```assembly
-t
...(-r结果输出)
138C:0100 B8204E           MOV        AX,4E20
-t
...
139C:0103 051614           ADD        Bx,2000
...
```
