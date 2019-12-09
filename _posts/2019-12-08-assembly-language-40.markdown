---
layout: post
title: 汇编语言 实验9 彩色字打印到屏幕
date: 2019-12-08 15:18:24.000000000 +09:00
tags: 汇编语言
---

### 编程： 在屏幕中间分别显示绿色，绿地红色，白底蓝色的字符串 'welcome to masm!'。

内存地址空间中，**B8000H~BFFFFH共32KB的空间(DOS的显存)，为80x25彩色字符模式的显示缓冲区**。向这个地址空间写入数据，写入的内容将立即出现在显示器上。

在80x25彩色字符模式下，显示器可以显示25行，每行80个字符，每个字符可以用256种属性(背景色、前景色、闪烁、高亮等组合信息)。

一个字符在显示缓冲区占两个字节，分别存放字符的ASCII码和属性。80x25模式下，一屏的内容在显示缓冲区共占4000个字节。

显示缓冲区分为8页，每页4KB，显示器可以显示任意一页的内容。一般情况下，显示第0页的内容。也就是说通常情况下，B8000H~B8F9FH中的4000个字节的内容将出现在显示器上。

**在一页的显示缓冲区中**

*偏移000~09F对应显示器上的第1行(80个字符占160个字节，09F=159，0~159共160个字节)；<br>
偏移0A0~13F对应显示器上的第2行；<br>
偏移140~1DF对应显示器上的第3行；<br>
...<br>
偏移F00~F9F对应显示器上的第25行。*

**在一列的显示缓冲区中**

*00~01单元对应显示器上的第1列；<br>
02~03单元对应显示器上的第2列；<br>
04~05单元对应显示器上的第3列；<br>
...<br>
9E~9F单元对应显示器上的第80列。*

在显示缓冲区中，**偶地址存放字符，奇地址存放字符的颜色属性**。

属性字节的格式：

| 二进制位置 | 含义   |
|------------|--------|
| 7          | BL闪烁 |
| 6          | R背景  |
| 5          | G背景  |
| 4          | B背景  |
| 3          | I高亮  |
| 2          | R前景  |
| 1          | G前景  |
| 0          | B前景  |

例如，显示器的0行0列显示红底高亮闪烁绿色的字符串'ABCDEF'，红底高亮闪烁绿色的属性字节为，

11001010B = CAH

代码如下：

```x86asm

assume cs:codesg ds:datasg ss:stacksg

datasg segment
	db 'welcome to masm!'
	db 02h, 24h, 71h   ;换算为16进制的不同前景色和背景色二进制代码
datasg ends

stacksg segment
	dw 8 dup(0)
stacksg ends

codesg segment
start:  mov ax, datasg
        mov ds, ax
        mov ax, stacksg
        mov ss, ax
        mov sp, 10h  ;指向栈顶
        xor bx, bx
        mov ax, 0B872h    ;地址指向B8000h:8720h

        mov cx, 3h        ;外层循环，按行不同要求打印字符串
   s3:  push cx           ;保护外层循环的三个通用寄存器值
        push ax
        push bx

        mov es, ax     ;把当前显示缓存指针调整至屏幕中心
        mov si, 0
        mov di, 0

        mov cx, 10h       ;对数据段中第一部分的16个ASCII码进行依次添加至显示缓存器

   s1:  mov al, ds:[si]		;在低位按顺序放置字符ASCII码
        mov es:[di], al   

        inc si
        add di, 2    ;每次空一格字符串的位置准备放置属性信息

        loop s1

        mov di, 1   ;从第二个字符串的位置处开始放置颜色属性
        pop bx      ;将bx中的值从栈中释放，用于提取出不同的颜色属性
        mov al, ds:10h[bx]
        inc bx       ;提取下一条颜色属性

        mov cx, 10h
   s2:  mov es:[di], al    ;在显示缓冲器中添加颜色属性
        add di, 2
        loop s2

        pop ax       ;取出显示屏的中心的地址
        add ax, 0Ah  ;在屏幕的下一行继续写入信息
        pop cx

        loop s3

        mov ax, 4c00h
        int 21h

codesg ends
end start
```

结果如图：

![figure](/assets/201911/2019-12-08_19-57-53.png)


