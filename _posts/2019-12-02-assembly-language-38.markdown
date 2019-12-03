---
layout: post
title: 汇编语言 9.7 9.8 jcxz loop 指令
date: 2019-12-02 22:19:24.000000000 +09:00
tags: 汇编语言
---

### 9.7 jcxz 指令

jcxz 指令为有条件转移指令，**所有的有条件转移指令都是短转移**，在对应的机器码中包含转移的位移，而不是目的地址。对IP的修改范围都为：-128~127。

指令格式：

jcxz 标号(如果(cx)=0, 转移到标号处执行。)

操作：

当(cx)=0时，(IP)=(IP)+8位位移；

8位位移 = 标号处的地址 - jcxz指令后的第一个字节的地址；

8位位移的范围为-128~127，用补码表示；

8位位移由编译程序在编译时算出。

当(cx)!=0时，程序继续向下执行。

我们从jcxz的功能中可以看出，`jcxz 标号` 的功能相当于：

```cpp
if((cx)==0) jmp short 标号；
```

问题(1)

补全编程，利用jcxz指令，实现在内存2000H段中查找第一个值为0的字节，找到后，将它的偏移地址存储在dx中。

```x86asm
assume cs:code
code segment
  start:mov ax, 2000H
        mov ds, ax
        mov bx, 0
      s:______
        ______
        ______
        ______
        jmp short s
     ok:mov dx, bx
        mov ax, 4c00h
        int 21h
code ends
end start
```
分析一下题意，即为按顺序将2000H段地址中的数据来给`cx`赋值，然后当`cx = 0`时，直接跳转到ok:处，将此时的偏移地址保存到`dx`中结束程序。但是要注意题中所讲为一个字节一个字节查找，所以应当将`cx`拆开两个高位和低位寄存器来考虑。

所以横线处代码应该依次为，

```x86asm
mov cl, [bx]
mov ch, 0
jcxz ok
inc bx
```

### 9.8 loop指令

loop指令与jcxz正好相反，为循环指令，**所有的循环执行都是短转移**，在对应的机器码中包含转移的位移，而不是目的地址。对IP的修改范围为：-128~127。

指令格式：

loop 标号((cx)=(cx)-1，如果(cx)!=0，转移到标号处执行。)

操作：

(1) (cx)=(cx)-1;

(2) 如果(cx)!=0, (IP)=(IP)+8位位移。

8位位移=标号处的地址-loop指令后的第一个字节的地址；

8位位移的范围为-128~127，用补码表示；

8位位移由编译程序在编译时算出。

如果(cx)=0，什么也不做(程序向下执行)。

我们从loop的功能中可以看出，`loop 标号`的功能相当于：

```cpp
(cx)--
if((cx)!=0) jmp short 标号；
```

问题(2)

补全编程，利用loop指令，实现在内存2000H段中查找第一个值为0的字节，找到后，将它的偏移地址存储在dx中。

```x86asm
asuume cs:code
code segment
  start:mov ax, 2000H
        mov ds, ax
        mov bx, 0
      s:mov cl, [bx]
        mov ch, 0
        ______
        inc bx
        loop s
     ok:dec bx
        mov dx, bx
        mov ax, 4cooh
        int 21h
code ends
end start
```
分析题意，注意loop标号执行时候的规则，每次`loop s`都会令cx寄存器的值，`(cx)=(cx)-1`，但如果`(cx)-1=0`就会跳出循环，所以横线处的代码应该为，

```x86asm
inc cx
```

