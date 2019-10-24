---
layout: post
title: 汇编语言 5.1 [bx]
date: 2019-10-24 10:16:24.000000000 +09:00
---
#### [bx]和内存单元

我们在debug中，可以输入以下命令来执行对于段地址偏移地址的操作：

```asm
mov ax, [0]     ；字传输
mov al, [0]     ；字节传输
```
但是当我们将这个命令在编译环境下执行，则会出现问题，例如我们写一个汇编脚本：

```x86asm
assume cs:codesg

codesg segment

start: mov ax, 2000H
       mov ds, ax
       mov al, [0]
       mov bl, [1]
       mov cl, [2]
       mov dl, [3]

       mov ax, 4C00H
       int 21H

codesg ends

end start
```
然后我们在debug中进行调试, 如图所示：

![figure](/assets/201910/2019-10-24_11-34-42.png)

我们发现随着```mov bx, [n]```的执行，通用寄存器BX的值发生改变。

这是因为在编译环境下，无法识别debug中我们用到的内存单元表示" [] "。

### 5.1 [BX]

在编译环境下我们有替代的方法：

```x86asm
mov ax, [bx]
```

功能为在bx中存放的数据作为一个偏移地址EA, 段地址SA默认在DS中，将SA:EA处的数据送入AX中。即：

$(AX)=((DS)*16+(BX))$

另一个用法为：

```x86asm
mov [bx], ax
```

功能为在bx中存放的数据作为一个偏移地址EA, 段地址SA默认在DS中，将AX中的数据送入内存SA:EA处。即：

$((DS)*16+(BX))=(AX)$

注：```inc```命令, 含义为在BX中的内容加1，如：

```x86asm
mov bx, 1
inc bx
```

执行后，BX = 2。
