---
layout: post
title: 汇编语言 10.1 10.2 10.3 ret和retf call指令 依据位移进行转移的call指令
date: 2019-12-10 10:28:24.000000000 +09:00
tags: 汇编语言
---

call和ret指令都是转移指令，它们都修改IP，或同时修改CS和IP。它们经常被共同用来实现子程序的设计。

### 10.1 ret和retf

ret指令用栈中的数据，修改IP的内容，从而实现近转移；<br>
retf指令用栈中的数据，修改CS和IP的内容，从而实现远转移。

> CPU执行ret指令时，进行下面两步操作：

1. (IP)=((ss)\*16+(sp))
2. (sp)=(sp)+2

栈模拟图如下，

| 1 | IP    |
| 2 |       |
|---|-------|
| 3 | stack |
| 4 |       |
| 5 | stack |

这时在栈顶1，2处存放着IP地址，执行ret后，会将IP从栈顶弹出并将指针向下指向3处。注意，这时只是指针被调到3，但是1，2处的IP仍然存在。

> CPU执行retf指令时，进行下面4步操作：

1. (IP)=((ss)\*16+(sp))
2. (sp)=(sp)+2
3. (CS)=((ss)\*16+(sp))
4. (sp)=(sp)+2

栈模拟图如下，

| 1 | IP    |
| 2 |       |
| 3 | CS    |
| 4 |       |
|---|-------|
| 5 | stack |
| 6 |       |
| 7 | stack |

这时在栈顶1，2处存放着IP地址；在3，4中存放着段地址，执行retf后，会将IP和CS分别从栈顶弹出并将指针向下指向5处。

如果我们用汇编语法来解释ret和retf指令，

CPU执行ret指令相当于，

```x86asm
pop IP
```

CPU执行retf指令相当于，

```x86asm
pop IP
pop CS
```

`ret`代码示例，

```x86asm
assume cs:code

stack segment
  db 16 dup (0)
stack ends

code segment
        mov ax, 4c00h
        int 21h

start:  mov ax, stack
        mov ss, ax
        mov sp, 16    ;栈顶指针调整
        mov ax, 0     ;将0推到栈顶
        push ax
        mov bx, 0
        ret           ;执行"pop IP"(IP = 0)，调到最代码段最开始终止程序运行
code ends
end start
```

`retf`代码示例，

```x86asm
assume cs:code

stack segment
  db 16 dup (0)
stack ends

code segment
        mov ax, 4c00h
        int 21h
start:  mov ax, stack
        mov ss, ax
        mov sp, 16
        mov ax, 0
        push cs     ;这里由于不需要改变cs的地址，所以直接"push cs"
        push ax
        mov bx, 0
        retf
code ends
end start
```

### 10.2 call指令

CPU执行call指令时，进行两步操作：
1. 将当前的IP或CS和IP压入栈；
2. 转移

call指令不能实现短转移，除此之外，call指令的实现转移方法与jmp指令的原理相同。

### 10.3

call 标号(将当前的IP压栈后，转到标号处执行指令)

CPU执行此种格式的call指令时，进行如下操作，

1. (sp)=(sp)-2
2. ((ss)\*16+(sp))=(IP)
3. (IP)=(IP)+16位移

用栈模拟图表示，

| 1 | stack |
| 2 |       |
| 3 | stack |
| 4 |       |
|---|-------|
| 5 | IP    |
| 6 |       |
| 7 | 空栈  |
| 8 |       |

开始时指针指向7的位置，即为空栈，在执行call指令时，push IP入栈，指针指向5的位置。

**16位位移=标号处的地址-call指令后的第一个字节的地址**；
16位位移的范围为-32768~32767，用补码表示；
16位位移由编译程序在编译时算出。

用汇编语法来解释此种格式的call指令，

```x86ams
push IP
jmp near ptr 标号
```

用示意图表示整个过程，

第一步cs和IP在地址加法器中生成物理地址并沿地址总线传入，提取数据并沿着数据总线进入指令缓冲寄存器，

![figure1](/assets/201912/2019-12-10_10-10-11.png)
![figure2](/assets/201912/2019-12-10_10-10-02.png)
![figure3](/assets/201912/2019-12-10_10-10-50.png)

这是缓冲寄存器中的机器码E80500，E8为call机器码。随后，0500会传入IP地址和现在的IP地址进行加成：0005h+0005h=000A，值得注意，这时**call 指令后的第一个字节的IP地址0005(注意，这里0005与之前参与地址加和的0005只是巧合相等，不要混淆！)会入栈**，

![figure4](/assets/201912/2019-12-10_10-11-46.png)

之后加成之后的物理地址2000A会再次沿地址总线传入，提取对应的代码并沿数据总线传入指令缓冲寄存器，并且执行对应指令，(ax) = (ax) + 1

![figure5](/assets/201912/2019-12-10_10-12-05.png)
![figure6](/assets/201912/2019-12-10_10-12-15.png)

最后，cs(2000)和IP(000D)在地址加法器合成物理地址2000D并沿地址总线传入，提取对应指令C3即ret指令，沿数据总线传入指令缓冲寄存器，并执行pop，将栈中的IP替换当前的cs与IP，

![figure7](/assets/201912/2019-12-10_10-16-10.png)
![figure8](/assets/201912/2019-12-10_10-16-27.png)

最后执行20005处的终止程序指令。

![figure9](/assets/201912/2019-12-10_10-16-53.png)

问题：

下面的程序执行后，ax中的值为多少？

|   | 内存地址 | 机器码 | 汇编指令  |
|---|----------|--------|-----------|
| 1 | 1000\:0  | b80000 | mov ax, 0 |
| 2 | 1000\:3  | e80100 | call s    |
| 3 | 1000\:6  | 40     | inc ax    |
| 4 | 1000\:7  | 58     | s\:pop ax |

在1处，ax = 0, IP --> 1000:3<br>
在2处，IP --> 1000:7, 入栈call指令后第一个字节的IP地址，即ax = 6<br>
在3处，被跳过<br>
在4处，pop ax，ax = 6












