---
layout: post
title: 汇编语言 寄存器总结 (转载)
date: 2019-12-30 20:55:24.000000000 +09:00
tags: 汇编语言
---
[转自CSDN博客，Dask Jhonson](https://blog.csdn.net/qq_41115702/article/details/82763383)<br>
[转自CSDN博客，iteye\_10501](https://blog.csdn.net/iteye_10501/article/details/82297309)

表格总结：

| 寄存器的分类      |                   | 寄存器     | 主要用途                                         |
|-------------------|-------------------|------------|--------------------------------------------------|
| 通用寄存器        | 数据寄存器        | AX         | 乘、除运算，字的输入输出，中间结果的缓存         |
|                   |                   | AL         | 字节的乘、除运算，字节的输入输出，十进制算数运算 |
|                   |                   | AH         | 字节的乘、除运算，存放中断的功能号               |
|                   |                   | BX         | 存储器指针                                       |
|                   |                   | CX         | 串操作、循环控制的计数器                         |
|                   |                   | CL         | 移位操作的计数器                                 |
|                   |                   | DX         | 字的乘、除运算，间接的输入输出                   |
|                   | 变址寄存器        | SI         | 存储器指针、串指令中的源操作数指针               |
|                   |                   | DI         | 存储器指针、串指令中的目的操作数指针             |
|                   |                   | BP         | 存储器指针、存取堆栈的指针                       |
|                   |                   | SP         | 堆栈的栈顶指针                                   |
| 指令指针          |                   | IP/EIP     |                                                  |
| 标志位寄存器      |                   | FLag/EFlag |                                                  |
| 32位CPU的段寄存器 | 16位CPU的段寄存器 | ES         | 附加段寄存器                                     |
|                   |                   | CS         | 代码段寄存器                                     |
|                   |                   | SS         | 堆栈段寄存器                                     |
|                   |                   | DS         | 数据段寄存器                                     |
|                   | 新增加的段寄存器  | FS         | 附加段寄存器                                     |
|                   |                   | GS         | 附加段寄存器                                     |

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


### 寄存器使用方法

#### 1. 4个数据寄存器是可拆分的

例如AX可分为AH(高位寄存器)和AL(低位寄存器)，即：在负值的时候可分开赋值。


#### 2. CS/IP寄存器

CS:IP 索引的内存即为CPU开始读取代码的起点，之后的一段代码区域，被称为代码片段(code segment)，这两个寄存器不能进行赋值操作(mov操作)，只能通过jmp指令跳转。

```x86asm
jmp 4E6A:0
```

#### 3. SS/SP

用于栈顶操作

#### 4. segment(段)

1. 数据段(被存在DS指定的段地址开始的地方)
2. 代码段(被存在CS指定的段地址开始的地方)
3. 栈段(被存在SS指定的段地址开始的地方)

一般通过assume伪指令把数据段绑定在对应的段上，

```x86asm
assume cs:code, ds:data, ss:stack
```

#### 5. 寄存器寻址

(1) 在8086CPU中只有这四个寄存器可以在[...]中进行内存单元的寻址。

比如，下面的指令都是正确的：<br>
mov ax,[bx]<br>
mov ax,[bx+si]<br>
mov ax,[bx+di]<br>
mov ax,[bp]<br>
mov ax,[bp+si]<br>
mov ax,[bp+di]

而下面都是错误的:
mov ax,[cx]<br>
mov ax,[ax]<br>
mov ax,[dx]<br>
mov ax,[ds]

(2) 在[...]中，这四个寄存器可以单独出现，或者只能以四种组合出现：bx和si、bx和di、bp和si、bp和di。

比如下面都是正确的：<br>
mov ax,[bx]<br>
mov ax,[si]<br>
mov ax,[di]<br>
mov ax,[bp]<br>
mov ax,[bx+si]<br>
mov ax,[bx+di]<br>
mov ax,[bp+si]<br>
mpv ax,[bp+di]<br>
mov ax,[bx+si+idata]<br>
mov ax,[bx+si+idata]<br>
mov ax,[bp+si+idata]<br>
mov ax,[bp+di+idata]

下面就是错误的：<br>
mov ax,[bx+bp]<br>
mov ax,[si+di]

(3) 只要在[...]中使用寄存器bp，而指令汇总没有显示给出段地址，**段地址就默认在ss中**。 比如下面的指令：

mov ax,[bp] 含义：(ax)=((ss)\*16+(bp))<br>
mov ax,[bp+idata] 含义：(ax)=((ss)\*16+(bp)+idata)<br>
mov ax,[bp+si] 含义：(ax)=((ss)\*16+(bp)+(si))<br>
mov ax,[bp+si+idata] 含义：(ax)=((ss)\*16+(bp)+(si)+idata)









