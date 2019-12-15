---
layout: post
title: 汇编语言 10.11 10.12 批量数据的传递 寄存器冲突问题
date: 2019-12-15 10:39:24.000000000 +09:00
tags: 汇编语言
---

### 10.11 批量数据的传递

子程序中如果只要一个参数，可以放在寄存器bx中。但是如果应对多个数据需要传递，由于寄存器的数量终究有限，我们不能简单地用寄存器存放多个需要传递的数据。对于返回值，也同样有相同的问题。

这种情况，我们将批量数据放到内存中，然后将它们所在的内存空间地址放在寄存器中，传递给需要的子程序。对于具有批量数据的返回结果，也可以用同样的方法。

问题： 设计一个子程序，功能：将一个全是字母的字符串转化为大写。

分析：

这个子程序需要知道两件事，**字符串的内容和字符串的长度**。因为字符串中的字母可能有很多，所以不便将整个字符串中的所有字母都直接传递给子程序。但是可以将字符串在内存中的首地址放在寄存器中传递给子程序。因为子程序中要用到循环，我们可以用loop指令，而循环的次数恰恰就是字符串的长度。处于方便，我们把字符串的长度放在cx中。

子程序代码如下：

```x86asm
capital: and byte ptr [si], 11011111b    ;将目标字符改写为大写
        inc si                          ;指向目标字符的下一个字符
        loop captal                     ;直至改写全部字符
        ret
```

完整代码如下，

```x86asm
assume cs:code
data segment
  db 'conversation'
data ends

code segment
  start: mov ax, data
         mov ds, ax
         mov si, 0
         mov cx, 12
         call capital
         mov ax, 4c00h
         int 21h

capital: and byte ptr [si], 11011111b
         inc si
         loop capital
         ret
code ends
end start
```
除了寄存器传递参数外，还有一种通用的方法是用栈来传递参数。

### 10.12 寄存器冲突的问题

设计一个子程序，功能：讲一个全是字母，以0结尾的字符串，转化为大写。

程序要处理的字符串以0作为结尾符，这个字符串可以如下定义：

`db 'conversation', 0`

应用这个子程序，字符串的额内容后面以一定要有一个0，标记字符串的结束。子程序可以依次读取每个字符进行检测，如果不是0，就进行大写的转化；如果是0，就结束处理。由于可通过检测0而直到是否已经处理完整个字符串，所以子程序可以不需要字符串的长度作为参数。这时可以用jcxz来检测0。

```x86asm
;说明：讲一个全是字母，以0结尾的字符串，转化为大写
;参数：ds:si指向字符串的首地址
;结果：没有返回值

captial: mov cl, [si]
         mov ch, 0    ;寻找cx = 0000时，执行jcxz命令
         jcxz ok
         and byte ptr [si], 11011111b
         inc si
         jmp short capital
     ok: ret
```
子程序的应用，将数据段中的字符串全部转化为大写。
```x86asm
assume cs:code
data segment
  db 'word', 0
  db 'unix', 0
  db 'wind', 0
  db 'good', 0
data ends
```
应用子程序后的代码段为，

```x86asm
code segment
  start: mov ax, data
         mov ds, ax
         mov bx, 0

         mov cx, 4
      s: mov bx, 0
         call capital
         add bx, 5
         loop s

         mov ax, 4c00h
         int 21h
capital: push cx
         push si

 change: mov cl, [si]
         mov ch, 0
         jcxz ok
         and byte ptr [si], 11011111b
         inc si
         jmp short change

     ok: pop si    ;这里注意寄存器入栈和出栈的顺序
         pop cx
         ret
```
要小心实际上的一般化问题：子程序中使用的寄存器很可能会造成与主程序中的寄存器之间的冲突。

解决方案：

在子程序开始将子程序中所有用到的寄存器中的内容都保存起来，在子程序返回前再回复。这样用栈来保存寄存器中的内容。

以后，编写的框架如下：

```x86asm
子程序开始时：子程序中使用的寄存器入栈
              子程序内容
              子程序中使用的寄存器出栈
              返回（ret、retf）
```
**要注意寄存器入栈和出栈的顺序**



