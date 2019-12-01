---
layout: post
title: 汇编语言 9.4 9.5 9.6 转移的目的地址以及转移地址在寄存器和内存中的jmp指令
date: 2019-11-30 16:19:24.000000000 +09:00
tags: 汇编语言
---

### 9.4 转移的目的地址在指令中的jmp指令

之前的jmp指令语法都是相当于当前IP的转移位移。

`jmp far ptr 标号` 该命令实现的是段间转移，这种转移也被成为远转移。功能如下：

(CS)=标号所在段的段地址；(IP)=标号在段中的偏移地址。

如下指令，

```x86asm
assume cs:codesg
  codesg segment
    start:mov ax, 0
          mov bx, 0
          jmp far ptr s
          db 256 dup (0)
        s:add ax, 1
          inc ax
  codesg ends
end start
```
对其进行编译并使用debug跟踪，查看其机器代码如下，

![figure1](/assets/201911/2019-12-01_15-22-54.png)

观察076A:0006，jmp 相关指令为`EA0B016A07`，指令`EA`为jmp的机器指令，后面的`0B016A07`为相应的跳转地址，由于机器码与汇编程序地址相反，高位在前，低位在后，所以对应着`jmp cs(076A):ip(010B)`。

### 9.5 转移地址在寄存器中的jmp指令

所谓转移地址在寄存器中，即通过`jmp`到寄存器中来实现段内近转移，这时寄存器中存放IP的值。

`jmp 16位reg`，实现功能为：(IP)=(16位reg)

如下，

```x86asm
jmp ax
```
ax中为IP的值，**实现的是段内近转移**。

### 9.6 转移地址在内存中的jmp指令

转移地址在内存中的jmp指令有两种格式：

(1) jmp word ptr 内存单元地址(**段内转移**):

功能：从内存单元地址处开始**存放一个字单元，是转移的目的的偏移地址**。

内存单元地址可用[寻址方式的任一格式](http://life.zququ.fun/2019/11/assembly-language-28/)给出。

代码如下，

```x86asm
mov ax, 0123H
mov ds:[0], ax
jmp word ptr ds:[0]
```
执行后，(IP)=0123H。或者如下，

```x86asm
mov ax, 0123H
mov [bx], ax
jmp word ptr [bx]
```
执行后，(IP)=0123H。

(2) jmp dword ptr 内存单元地址(**段间转移**):

功能：从内存单元地址处开始存放**两个字单元，高地址处的字是转移的目的段地址，低地址处是转移的目的偏移地址**。

(CS)=(内存单元地址+2)
(IP)=(内存单元地址)

内存单元地址可用寻址方式的任一格式给出。

例如代码，

```x86asm
mov ax, 0123H
mov ds:[0], ax
mov word ptr ds:[2], 0
jmp dword ptr ds:[0]
```
执行后，(CS)=0, (IP)=0123H, CS:IP指向0000:0123H。高位为0000--\>CS，低位为0123H--\>IP。

又如下面代码，

```x86asm
mov ax, 0123H
mov [bx], ax
mov word ptr [bx+2], 0
jmp dword ptr [bx]
```
执行后，(CS)=0，(IP)=123H，CS:IP指向0000:0123H。

练习：

> (1) 程序如下：

```x86asm
assume cs:code
data segment
?
data ends

code segment
  start:mov ax, data
        mov ds, ax
        mov bx, 0
        jmp word ptr [bx+1]
code ends
end start
```
问题：若要使程序中的jmp指令执行后，CS:IP指向程序的第一条指令，在data段中应该定义哪些数据？

分析可知在执行`jmp word ptr [bx+1]`，由于`[bx+1]`被指定为`word`格式，说明是在内存单元地址的**段内转移**。

另一方面由于[bx]中为0，所以等同于`jmp word ptr [1]`跳转到0000地址。所以data中为`dd 0`或`db 4 dup 0`或`dw 2 dup 0`。

> (2) 程序如下：

```x86asm
assume cs:code
data segment
  dd 12345678H
data ends

code segment
  start:mov ax, data
        mov ds, ax
        mov bx, 0
        mov [bx], ______
        mov [bx+2], ______
        jmp dword ptr ds:[0]
code ends
end start
```
补全程序，使jmp指令执行后，CS:IP指向程序的第一条指令。

从`jmp dword ptr ds:[0]`，可以看出是`dword`格式，判断为转移地址在内存中的**段间转移**。由于CS:IP指向程序的第一条指令，所以CS:IP应该为CS:0000，故第一个位置应该为`mov [bx], bx`或`mov [bx], word ptr 0`或`mov [bx], offset start`等等，总之表示IP地址为0000。而第二个位置应该为`mov [bx+2], CS`或者`mov [bx+2], seg code`等等，总之表示其**CS的段地址**。

> (3) 用Debug查看内存，结果如下：

2000:1000 BE 00 06 00 00 00 ...

则此时，CPU执行指令：

```x86asm
mov ax, 2000H
mov es, ax
jmp dword ptr es:[1000H]
```

这时的(CS)和(IP)为多少？

对于双字类型的jmp指令，判断为段间跳转，即跳转到es:[1000H]，也就是2000H:1000H地址。这时的CS为高位0006，IP为低位00BE。这里需要注意的是，无论地址为多少，**jmp都把相应地址所指的高位作为CS地址，而低位作为IP地址**。

另外记住，在数据段中，**后面的数据为高位, 前面的数据为低位**!




