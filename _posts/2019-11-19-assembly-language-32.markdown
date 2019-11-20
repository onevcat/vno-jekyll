---
layout: post
title: 汇编语言 8.1 8.2 8.3 8.4(1) bx,si,di,bp 机器指令数据在哪 数据位置表达 寻址方式(1)直接寻址
date: 2019-11-19 11:30:24.000000000 +09:00
tags: 汇编语言
---

首先规定寄存器(reg，register): ax,bx,cx,dx,ah,al,bh,bl,ch,cl,dh,dl,sp,bp,si,di;

规定段寄存器(sreg, segment register): ds,ss,cs,es。

### 8.1 bx、si、di和bp

1.在8086CPU中只有**bx,bp,si,di**这四个寄存器可以在`[...]`, 中来进行内存单元的寻址。比如：

```x86asm
mov ax, [bx]
mov ax, [bx+si]
mov ax, [bx+di]
mov ax, [bp]
mov ax, [bp+si]
mvo ax, [bp+di]
```

2.在[...]中，这4个寄存器可以单个出现，或者只能以4种组合出现：**bx和si, bx和di, bp和si, bp和di**，比如：

```x86asm
mov ax, [bx]
mov ax, [si]
mov ax, [di]
mov ax, [bp]
mov ax, [bx+si]
mov ax, [bx+di]
mov ax, [bp+si]
mov ax, [bp+di]
mov ax, [bx+si+idata]
mov ax, [bx+di+idata]
mov ax, [bp+si+idata]
mov ax, [bp+di+idata]
```

3.只要在[...]中使用寄存器bp, 而指令中没有显性的给出段地址, 段地址就默认在ss中。比如：

```x86asm
mov ax, [bp]
mov ax, [bp+idata]
mov ax, [bp+si]
mov ax, [bp+si+idata]    ;含义为(ax)=((ss)*16+(bp)+(si)+idata)
```

### 8.2 机器指令处理的数据在什么地方

绝大部分机器指令都是进行数据处理的指令，处理大致可分为3类：读取、写入、运算。在机器指令这一层来讲，并不关心数据的值是多少，而关心**指令执行前一刻，它将要处理的数据所在位置**。指令执行前，要处理的数据可以在三个地方：

1. CPU内部
2. 内存
3. 端口

指令列举：

| 机器码   | 汇编指令    | 指令执行前数据的位置 |
|----------|-------------|----------------------|
| 8E1E0000 | mov bx, [0] | 内存，ds:0单元       |
| 89C3     | mov bx, ax  | CPU内部，ax寄存器    |
| BB0100   | mov bx, 1   | CPU内部，指令缓冲器  |

### 8.3 汇编语言中数据位置表达

1.立即数(idata)

对于直接包含在机器指令中的数据(CPU的指令缓冲器中), 成为**立即数(idata)**。

```x86asm
mov ax, 1
add bx, 2000H
or bx, 00010000b
mov al, 'a'
```
2.寄存器

指令要处理的数据在寄存器中，在汇编指令中给出相应的寄存器名。

```x86asm
mov ax, bx
mov ds, ax
push bx
mov ds:[0], bx
push ds
mov ss, ax
mov sp, ax
```

3.段地址(SA)和偏移地址(EA)

指令要处理的数据在内存中，在汇编指令中可用[X]的格式给出EA、SA在某个段寄存器中。

存放段地址的寄存器可以是默认的，比如：

```x86asm
mov ax, [0]
mov ax, [di]
mov ax, [bx+9]
mov ax, [bx+si]
mov ax, [bx+si+8]
```
等指令，段地址默认在ds中。

```x86asm
mov ax, [bp]
mov ax, [bp+8]
mov ax, [bp+si]
mov ax, [bp+si+8]
```
等指令，段地址默认在ss中。

存放段地址的寄存器也可以是显性给出的，比如以下命令：

```x86asm
mov ax, ds:[bp]
mov ax, es:[bx]
mov ax, ss:[bx+si]
mov ax, cs:[bx+si+8]    ;含义是 (ax)=((cs)*16+(bx)+(si)+8)
```
### 8.4 寻址方式

当数据存放在内存中，我们可以用多种方式来给定这个内存单元的偏移地址，**这种定位内存单元的方法一般被称为寻址方式**。

首先我们来看一下直接寻址的寻址方式：

首先读取指令过程：

第一步，代码段和代码段偏移地址在地址加法器中进行处理并给出相应地址：`2000E`, 在定位中定位相应的代码地址A10E00, 通过数据总线到达指令缓冲寄存器中。

![figure1](/assets/201911/2019-11-19_11-25-01.png)
![figure2](/assets/201911/2019-11-19_11-26-02.png)

注意偏移地址发生变化，ip从000E变为0011，指针只想了下一条指令。注意这里**并未开始执行指令，这一步是将对应代码的地址从数据总线传输到指令缓冲寄存器**。

下一步，在指令缓冲器寄存器传入了上一步的地址后，**由CPU读取指令缓冲器中的指令后**，执行ip在2000E处的对应指令`mov ax, ds:[000E]`, 再次将地址加法器处理后，地址为2000E的对应在内存中的数据`A10E`(注意实际数据为`0EA1`)沿着数据总线传送到ax寄存器中。

![figure3](/assets/201911/2019-11-19_11-27-44.png)
![figure4](/assets/201911/2019-11-19_11-27-58.png)





