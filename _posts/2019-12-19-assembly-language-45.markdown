---
layout: post
title: 汇编语言 实验10 (1) 显示字符串
date: 2019-12-19 16:16:24.000000000 +09:00
tags: 汇编语言
---

### 问题

编写一个通用的子程序来实现这个功能。我们应该提供灵活的调用接口，使调用者可以决定显示的位置(行，列)、内容和颜色。

### 子程序描述

1. 名称：show\_str
2. 功能：在指定的位置，用指定的颜色，显示一个用0结束的字符串。
3. 参数：(dh)=行号(取值范围0~24)，(dl)=列号(取值范围0~79)，(cl)=颜色, ds:si指向字符串的首地址。
4. 返回：无
5. 应用举例：在屏幕的8行3列，用绿色显示data段中的字符串。

```x86asm
assume cs:code
data segment
  db 'Welcome to masm!', 0
data ends

code segment
  start:  mov dh, 8
          mov dl, 3
          mov cl, 2
          mov ax, data
          mov ds, ax
          mov si, 0
          call show_str

          mov ax, 4c00h
          int 21h
  show_str:  :
             :
             :
code ends
end start
```
### 提示
(1) 子程序的入口参数是屏幕上的行号与列号，注意在子程序内部要将它们转化为显寸中的地址，首先要分析一下屏幕上的行列位置与显存地址的对应关系；<br>
(2) 注意保护子程序中用到的相关寄存器；<br>
(3) 这个子程序的内部处理和显存的结构密切相关，但是向外提供了与显存结构无关的接口。通过调用这个子程序，进行字符串的显示时可以不必了解显存的结构，为编程提供了方便。在实验中，注意体会这种设计思想。

```x86asm
show_str:  push ax
           push bx
           push es
           push si  ;将寄存器保护起来

           mov ax, 0B800H  ;显示缓存地址为B8000H，所以对应在寄存器中为0B800H
           mov es, ax    ;将显示缓存地址放入es寄存器
           mov ax, A0H
           mul dh    ;此时计算显示缓存器第'dh'行(第8行)第一个字符的起始地址
           mov bx, ax
           mov ax, 02H
           mul dl    ;此时计算第'dl'列(第3列)的字符的起始地址
           add bx, ax   ;将指针指向第'dh'行第'dl'列的字符的起始地址
           mov al, cl   ;指向对应颜色，并保存到对应寄存器al中
           mov cl, 0    ;清空cl

  show0:  mov ch, [si]   ;采用jcxz不断寻0，当找到0跳出的方法来进行字符串从数据段到显示缓存器的转移
          jcxz show1
          mov es:[bx], ch    ;将数据段中的字符按顺序转移到es:[bx]的低位(每个偏移字型数据的低位)
          mov es:[bx].1, al  ;将al中的颜色信息转移到es:[bx].1(每个偏移字型数据的高位)
          inc si
          add bx, 2
          jmp show0

  show1:  pop si
          pop es
          pop bx
          pop ax
          ret
code ends
end start
```


