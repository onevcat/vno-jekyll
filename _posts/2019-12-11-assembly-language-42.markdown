---
layout: post
title: 汇编语言 10.4 10.5 10.6 转移的目的地址在指令，寄存器以及内存最后那个的call指令
date: 2019-12-11 11:48:24.000000000 +09:00
tags: 汇编语言
---

### 10.4 转移的目的地址在指令中的call指令

前面讲的call指令，其对应的及其指令中并没有转移的目的地址，而是相对于当前IP的转移位移。

"call far ptr 标号"实现的是段间转移。

CPU执行此种格式的call指令时，进行如下的操作。

1. (sp)=(sp)-2 <br>
   ((ss)\*16+(sp))=(CS)<br>
   (sp)=(sp)-2<br>
   ((ss)\*16+(sp))=(IP)

2. (CS)=标号所在段的段地址<br>
   (IP)=标号在段中的偏移地址

从上面的描述中可以看出，如果我们用汇编语法来解释此种格式的call指令，则:

CPU执行"call far ptr 标号"时，相当于进行：

push CS<br>
push IP<br>
jmp far ptr 标号

问题：

下面的程序执行后，ax中的数值为多少？

|   | 内存地址 | 机器码     | 汇编指令       |
|---|----------|------------|----------------|
| 1 | 1000\:0  | b80000     | mov ax, 0      |
| 2 | 1000\:3  | 9A09000010 | call far ptr s |
| 3 | 1000\:8  | 40         | inc ax         |
| 4 | 1000\:9  | 58         | s:pop ax       |
| 5 |          |            | add ax, ax     |
| 6 |          |            | pop bx         |
| 7 |          |            | add ax, bx     |

在1处，ax --> 0，在2处，执行call指令，IP = 8，并跳转到5处，`pop ax`，弹出IP地址并赋值给ax，此时ax --> 8。执行`add ax, ax`，ax --> 8 + 8 = 16 (**注意这里是错误的，因为IP地址间的运算应该为16进制运算：8h + 8h = 10h**)。由于call指令为`call far ptr 标号`实现的是段间转移，所以首先push的地址为CS，而后push进栈的地址为IP，所以第一次pop出的为IP，而后pop出的为CS。所以`pop bx`会弹出CS地址并赋值给bx，所以这是，bx的值为1000，所以`add ax, bx` --> ax = ax + bx = 10h + 1000h = 1010h。

### 10.5 转移地址在寄存器中的call指令

指令格式：call 16位reg<br>
功能：

(sp)=(sp)-2<br>
((ss)\*16)+(sp)=(IP)<br>
(IP)=(16位reg)

用汇编语法来解释此种格式的call指令，CPU执行"call 16位reg"时，相当于进行：

push IP<br>
jmp 16位reg

问题：

下面的程序执行后，ax中的数值为多少？

|   | 内存地址 | 机器码 | 汇编指令     |
|---|----------|--------|--------------|
| 1 | 1000\:0  | b80600 | mov ax, 6    |
| 2 | 1000\:3  | ffd0   | call ax      |
| 3 | 1000\:5  | 40     | inc ax       |
| 4 | 1000\:6  |        | mov bp, sp   |
| 5 |          |        | add ax, [bp] |

在1处，ax --> 6，在2处执行`call ax`指令，将IP = 5推入栈中，并跳转到ax对应的值为IP的地址，即1000:6，执行`mov bp, sp`，此时的(sp) = (sp) - 2 = 0000h(栈顶) - 2 = fffeh并赋值给bp。并且此时[bp] = ss:[bp] = 5。所以执行`add ax, [bp]`后，ax = ax + [bp] = 6h + 5h = 0bh。

### 10.6 转移地址在内存中的call指令

转移地址在内存中的call指令有两种格式。

1. call word ptr 内存单元地址<br>
   用汇编语法来解释此种格式的call指令，则：<br>
   CPU执行"call word ptr 内存单元地址"时，相当于进行：<br>
   push IP<br>
   jmp word ptr 内存单元地址<br>
   <br>
   代码示例，<br>
   <br>
   mov sp, 10h<br>
   mov ax, 0123h<br>
   mov ds:[0], ax<br>
   call sord ptr ds:[0]<br>
   <br>
   执行后，(IP) = 0123H，(sp)=0EH。

2. call dword ptr 内存单元地址<br>
   用汇编语法来解释此种格式的call指令，则：<br>
   CPU执行"call dword ptr 内存单元地址"时，相当于进行：<br>
   <br>
   push CS<br>
   push IP<br>
   jmp dword ptr 内存那单元地址<br>

   代码示例，<br>

   mov sp, 10h<br>
   mov ax, 0123h<br>
   mov ds:[0], ax<br>
   mov word ptr ds:[2], 0<br>
   call dword ptr ds:[0]<br>

   执行后，(CS)=0，(IP)=123H，(sp)=0CH。

问题(1)：

下面的程序执行后，ax中的数值为多少？

```x86asm
assume cs:code
stack segment
  dw 8 dup (0)
stack ends
code segment
  start:mov ax, stack
        mov sp, ax
        mov sp, 16
        mov ds, ax
        mov ax, 0
        call word ptr ds:[0EH]
        inc ax
        inc ax
        inc ax
        mov ax, 4c00h
        int 21h
code ends
end start
```
首先我们绘制一个对应地址的表格，

|    | 内存地址   | 代码                    |
|----|------------|-------------------------|
| 1  | 0C50\:0000 | mov ax, stack           |
| 2  | 0C50\:0003 | mov ss, ax              |
| 3  | 0C50\:0005 | mov sp, 16              |
| 4  | 0C50\:0008 | mov ds, ax              |
| 5  | 0C50\:000A | mov ax, 0               |
| 6  | 0C50\:000D | call word ptr ds\:[0EH] |
| 7  | 0C50\:0011 | inc ax                  |
| 8  |            | inc ax                  |
| 9  |            | inc ax                  |
| 10 |            | mov ax, 4c00h           |
| 11 |            | int 21h                 |

在5处，ax --> 0。在6处，执行`call word ptr ds:[0EH]`，前面在3处，指明了栈顶为sp = 16，所以在栈顶的位置推入IP地址：IP = 0011，并执行跳转到目标地址ds:[0EH]，正好指向刚刚推入栈的IP = 0011，所以ds:[0EH] = 0011，所以跳转到7处，执行三次inc ax，所以ax = 0 + 1 + 1 + 1 = 3。

问题(2)

下面的程序执行后，ax和bx中的数值为多少？

```x86asm
assume cs:code
data segment
  dw 8 dup(0)
data ends
code segment
  start:mov ax, data
        mov ss, ax
        mov sp, 16
        mov word ptr ss:[0], 0ffset s
        mov ss:[2], cs
        call dword ptr ss:[0]
        nop
      s:mov ax, 0ffset s
        sub ax, ss:[0ch]
        mov bx, cs
        sub bx, ss:[0eh]
        mov ax, 4c00h
        int 21h
code ends
end start
```
根据代码绘制栈，

| s的CS    |
| s的IP\-1 |
| ...      |
| ...      |
| ...      |
| s的CS    |
| s的IP    |

ss:[0]为s的IP，ss:[2]为s的CS。执行`call dword ptr ss:[0]`后，在ss:[0ch]，ss:[0dh]处推入IP = s的IP - 1，并在ss:[0eh]，ss:[0fh]推入CS = s的CS。在s中，`mov ax, offset s`ax = s 的IP。执行`sub ax, ss:[0ch]`，所以ax = ax - ss:[0ch] = s的IP - (s的IP - 1) = 1。`mov bx, cs`，所以bx = s的CS。则`sub bx, ss:[0eh]`结果，bx = s的CS - s的CS = 0。











