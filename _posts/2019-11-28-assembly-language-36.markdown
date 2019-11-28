---
layout: post
title: 汇编语言 9.1 9.2 9.3 offet jmp 依据位移进行转移的jmp指令
date: 2019-11-28 11:58:24.000000000 +09:00
tags: 汇编语言
---

### 9.1 操作符offset

offset在汇编语言中是由编译器处理的符号，它的功能是**取得标号的偏移地址**。

如下代码，

```x86asm
assume cs:codesg

codesg segment
  start: mov ax, offset start  ;equal to: mov ax, 0
      s: mov ax, offset s      ;equal to: mov ax, 3
codesg ends

end start
```

这里`offset start`相当于指明并取得start处的偏移地址0，`offset s`相当于指明并取得标号s处的偏移地址3。

> 问题9.1 

在`__________`处填写指令，使该程序在运行中将s处的一条指令复制到s0处。

```x86asm
assume cs:codesg
codesg segment
  s:  mov ax, bx    ;机器码占两个字节
      mov si, offset s
      mov di, offset s0
      __________
      __________

 s0:  nop   ;这里nop的机器码占一个字节
      nop
codesg ends
end s
```
通过offset分别获得了s和s0处的偏移地址，就可以直接通过通用寄存器ax将代码段中的数据拷贝的目标偏移地址。
```x86asm
mov ax, cs:[si]
mov cs:[di], ax
```

同时给出了汇编语言处理问题的思路：
1. s和s0处的指令所在的内存单元的地址是多少？cs:offset s 和cs:0ffset s0。
2. 将s处的指令复制到s0处，就是将cs:offset s 处的数据复制到cs:offset s0处。
3. 段地址已知在cs中，偏移地址offset s和offset s0已经送入了si和di中。
4. 要复制的数据多长？mov ax, bx指令的长度为2个字节。

### 9.2 jmp指令

jmp为**无条件转移指令**，可以只修改IP也可以同时修改CS和IP。

1. 转移的目的地址
2. 转移的距离（段间转移、段内转移、段内近转移）

### 9.3 依据位移进行转移的jmp指令

jmp short 标号（转移到标号处执行指令）

这种格式的jmp指令实现的是段内短转移，它对IP的修改范围是-128~127 （共256个字节, 一个8进制单位), 标号指明转移目的地，CS:IP应该指向标号处的指令。

例如代码，

```x86asm
assume cs:codesg
codesg segment
start:mov ax, 0
      jmp short s
      add ax, 1    ;跳过该指令的执行
    s:inc ax
codesg ends
end start
```

这里将直接跳过`add ax, 1`指令。

首先，我们来观察一下相关指令对应的机器码：

| 汇编指令           | 机器指令    |                            |
|--------------------|-------------|----------------------------|
| mov ax, 0123h      |    B8 23 01 | 这里需要注意字节类型存储   |
| mov ax, ds:[0123h] |    A1 23 01 | 机器码中高位数据在左侧     |
| push ds:[0123h]    | FF 36 23 01 | 与汇编指令中的数据顺序相反 |

可以看出，一般汇编指令中，idata（立即数）无论代表数据或者内存单元偏移地址都会在对应的及其指令中出现，因为CPU执行的是及其指令，它必须要处理这些数据或者地址。

下面来通过debug探索一下`jmp short`指令的原理，我们对上面代码进行编译，并通过使用U命令来查看对应代码段中的机器码，

![figure1](/assets/201911/2019-11-28_13-08-14.png)

从图中可以看出，在CPU执行JMP命令时，对应的及其指令为`EB03`，而并未给出对应的目标偏移地址。这说明执行该命令时并不知道转移的目的地址。

我们对以上代码进行改写，

```x86asm
assume cs:codesg
codesg segment
start:mov ax, 0
      jmp short s
      add ax, 1    ;跳过该指令的执行
      add ax, ax
    s:inc ax
codesg ends
end start
```

同样在debug中跟踪程序，

![figure2](/assets/201911/2019-11-28_13-17-39.png)

从图中可以看出，通过添加一条长度为两个字节的指令`add ax, ax`，JMP的机器指令从`EB03`变为了`EB05`，这说明这里`EB`后面代表了跳过的指令的字节长度。

同样的，也可以通过下面这个例子代码得到相同的结论，

```x86asm
assume cs:codesg
codesg segment
start:mov ax, 0
      mov bx, 0
      jmp short s
      add ax, 1    ;跳过该指令的执行
      add ax, ax
    s:inc ax
codesg ends
end start
```

debug跟踪程序结果，

![figure3](/assets/201911/2019-11-28_13-24-54.png)

这说明CPU在执行JMP指令时，并不需要转移目的地址。

第一步，CPU运行到了相应的地址即20008，准备执行`jmp s`指令。

![figure4](/assets/201911/2019-11-28_13-29-47.png)

然后获取对应机器指令`EBF6`，放入指令缓冲寄存器，并且这是的IP地址会发生改变增加2，指向2000A。

![figure5](/assets/201911/2019-11-28_13-49-09.png)

之后F6会与现在的IP地址求和并输出对应的结果，更改当前IP为00000，即s:mov ax, 4c00h处。

![figure6](/assets/201911/2019-11-28_13-34-27.png)

而这里的计算：

$$00F6 + 000A = 0000$$

是因为这里的F6是以补码的形式存在的，其值为-10，即:

$$-000A + 000A = 0000$$

补码的方式为：

F6H = 11110110B --> 11110110B - 1B = 11110101B --> 转化为字节型 1010 --> 并取反(not) --> -10

关于补码的方法以后会详细介绍。

与`jmp short`相类似，`jmp near ptr 标号`功能如下：

1. 16位位移=标号处的地址-jmp指令后的第一个字节的地址;
2. near ptr指明此处的位移为16位位移，进行的是段内近转移。
3. 16位位移的范围是-32768~32767，用补码表示。
4. 16位位移由编译程序在编译时算出。


