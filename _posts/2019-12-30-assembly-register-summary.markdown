---
layout: post
title: 汇编语言 寄存器总结 (转载)
date: 2019-12-30 20:55:24.000000000 +09:00
tags: 汇编语言
---
![转自CSDN论坛，Dask Jhonson](https://blog.csdn.net/qq_41115702/article/details/82763383)

8086CPU总共有14个寄存器：<br>
即AX，BX，CX，DX，SP，BP，SI，DI，IP，FLAG，CS，DS，SS，ES共14个。

### 1. 通用寄存器

> AX，BX，CX，DX称作为**数据寄存器**：

AX (Accumulator)：累加寄存器，也称之为累加器；<br>
BX (Base)：基地址寄存器；<Br>
CX (Count)：计数器寄存器；<br>
DX (Data)：数据寄存器；

> SP和BP又称作为**指针寄存器**：

SP (Stack Pointer)：堆栈指针寄存器；<br>
BP (Base Pointer)：基指针寄存器；<br>

> SI和DI又称作为**变址寄存器**：

SI (Source Index)：源变址寄存器；<br>
DI (Destination Index)：目的贬值寄存器；

### 2. 控制寄存器

> IP (Instruction Pointer)：指令指针寄存器；
> FLAG：标志寄存器；

### 3. 段寄存器

> CS (Code Segment)：代码段寄存器；<br>
> DS (Data Segment)：数据段寄存器；<br>
> SS (Stack Segment)：堆栈段寄存器；<br>
> ES (Extra Segment)：附加段寄存器；

以上是常见的寄存器分类；其终值得注意的每个寄存器都是16位的(dword，双字节)，而只有4个数据寄存器，**即AX，BX，CX，DX可以拆分为两个8位寄存器来使用**。

### 4. 4个数据寄存器是可拆分的

例如AX可分为AH(高位寄存器)和AL(低位寄存器)，即：在负值的时候可分开赋值。


### 5. CS/IP寄存器

CS:IP 索引的内存即为CPU开始读取代码的起点，之后的一段代码区域，被称为代码片段(code segment)，这两个寄存器不能进行赋值操作(mov操作)，只能通过jmp指令跳转。

```x86asm
jmp 4E6A:0
```

### 6. SS/SP

用于栈

### 7. segment(段)

1. 数据段(被存在DS指定的段地址开始的地方)
2. 代码段(被存在CS指定的段地址开始的地方)
3. 栈段(被存在SS指定的段地址开始的地方)

一般通过assume伪指令把数据段绑定在对应的段上，

```x86asm
assume cs:code, ds:data, ss:stack
```









