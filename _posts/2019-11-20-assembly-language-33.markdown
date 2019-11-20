---
layout: post
title: 汇编语言 8.4 8.5 寻址方式(2) 指令要处理的数据多长
date: 2019-11-20 16:59:24.000000000 +09:00
tags: 汇编语言
---

### 8.4 寻址方式(2)

寻址方式的小结表格:

| 寻址方式      | 含义                       | 名称             | 常用格式举例                  |
|---------------|----------------------------|------------------|-------------------------------|
| [idata]       | EA=idata;SA=(ds)           | 直接寻址         | [idata]                       |
| [bx]          | EA=(bx);SA=(ds)            | 寄存器间接寻址   | [bx]                          |
| [si]          | EA=(bx);SA=(ds)            |                  |                               |
| [di]          | EA=(di);SA=(ds)            |                  |                               |
| [bp]          | EA=(bp);SA=(ss)            |                  |                               |
| [bx+idata]    | EA=(bx)+idata;SA=(ds)      | 寄存器相对寻址   | 用于结构体: [bx].idata        |
| [si+idata]    | EA=(si)+idata;SA=(ds)      |                  | 用于数组: idata[si],idata[di] |
| [di+idata]    | EA=(di)+idata;SA=(ds)      |                  | 用于二位数组: [bx][idata]     |
| [bp+idata]    | EA=(bp)+idata;SA=(ss)      |                  |                               |
| [bx+si]       | EA=(bx)+(si);SA=(ds)       | 基址变址寻址     | 用于二维数组: [bx][si]        |
| [bx+di]       | EA=(bx)+(di);SA=(ds)       |                  |                               |
| [bp+si]       | EA=(bp)+(si);SA=(ss)       |                  |                               |
| [bp+di]       | EA=(bp)+(di);SA=(ss)       |                  |                               |
| [bx+si+idata] | EA=(bx)+(si)+idata;SA=(ds) | 相对基址变址寻址 | 用于表格(结构)中的数组项:     |
| [bx+di+idata] | EA=(bx)+(di)+idata;SA=(ds) |                  | [bx].idata[si]                |
| [bp+si+idata] | EA=(bp)+(si)+idata;SA=(ss) |                  | 用于二维数组:                 |
| [bp+di+idata] | EA=(bp)+(di)+idata;SA=(ss) |                  | idata[bx][si]                 |

我们以相对基址变址寻址为例，用图例讲一下寻址和运行的步骤：

首先代码段地址和偏移地址在地址加法器合成20位地址数据:
![figure1](/assets/201911/2019-11-20_15-55-41.png)
20位地址20018随着地址总线传输到内存，寻找对应地址的代码地址8B4001，并沿数据总线传输到指令缓冲寄存器。
![figure2](/assets/201911/2019-11-20_15-55-47.png)
![figure3](/assets/201911/2019-11-20_15-55-57.png)
之后CPU会从对应的指令缓冲寄存器中的指令，将对应在ds, si, bx中的地址在地址加法器中进行处理变为20012，再沿地址总线寻找对应地址的数据8B07(低位在前，高位在后)。之后8B07将会沿着数据总线进入ax中。
![figure4](/assets/201911/2019-11-20_15-56-11.png)
![figure5](/assets/201911/2019-11-20_15-56-20.png)
![figure6](/assets/201911/2019-11-20_15-56-33.png)

### 8.5 指令要处理的数据有多长

8086CPU的指令，可以处理两种尺寸的数据，byte和word。所以在机器指令中要指明，指令进行的是字操作。对于这个问题，汇编语言中用一下方法处理。

(1) 通过寄存器名指明要处理的数据的尺寸。

寄存器指明了指令进行的是字(字型)操作。

```x86asm
mov ax, 1
mov bx, ds:[0] ;这里的ds:[0]传入了bx中，为字型数据
      ;所以这里的ds:[0]应该包含ds:[1](前8位高位地址)
      ;ds:[0]包含低位的后8位数据
mov ds, ax
mov ds:[0], ax
inc ax
add ax, 1000
```
而对于字节型的操作。

```x86asm
mov al, 1    ;字节型
mov al, bl
mov al, ds:[0]
mov ds:[0], al
inc al
add al, 100
```

(2) 在没有寄存器名存在的情况下，用操作符X ptr指明内存单元的长度，X 为word 或者byte。例如：

```x86asm
;字型
mov word ptr ds:[0], 1
inc word ptr [bx]
inc word ptr ds:[0]
add word ptr [bx], 2
;字节
mov byte ptr ds:[0], 1
inc byte ptr [bx]
inc byte ptr ds:[0]
add byte ptr [bx], 2
```
如果没有指明数据类型，很容易造成溢出错误，例如'FFH' + '1' = '00H'，而16位的数据'00FFH' + 1 = '0100H'。

再如，

2000: 1000 FF FF FF FF FF FF

指令，

```x86asm
mov ax, 2000H
mov ds, ax
mov byte ptr [1000H], 1
```

将使内存中的内容变为,

2000: 1000 01 FF FF FF FF FF

而如果指令为，

```x86asm
mov ax, 2000H
mov ds, ax
mov word ptr [1000H], 1
```

将使内存中的内容变为，

2000: 1000 01 00 FF FF FF FF

因为对于字节型和字型数据，所针对的数据长度是不同的。同样也强调了明确数据类型的必要性!

(3) 其他方法

有些指令默认了访问的是字单元还是字节单元，如栈指令，`push`，只针对字单元进行操作(对于`push`，sp=sp-2)。







