---
layout: post
title: 汇编语言 7.1 7.2 7.3 7.4 and or, ASCII, 按字符给出数据, 大小写转化
date: 2019-11-08 23:11:24.000000000 +09:00
tags: 汇编语言
---

### 7.1 and和or指令

#### and 指令

```x86asm
mov al, 01100011B
mov al, 00111011B

;结果为 al = 00100011B
```
通过该指令可将操作对象的相应位设为0，其他不变。如将al的第六位设置为零的指令为：

```x86asm
and al, 10111111B
```

#### or 指令

```x86asm
mov al, 01100011B
or al, 00111011B

;结果为 al = 01111011B
```
通过该指令可将操作对象的相应位设置为1，其他位不变。如将al的第六位设置为1的指令为：

```x86asm
or al, 09000000B
```

### 7.2 关于ASCII码

世界上有很多种编码方案，有一种方案叫做ASCII编码，是在计算机系统中通常被采用的。比如ASCII中，61H表示'a', 62H表示'b'。

#### 文本便捷过程

我们按下键盘的a键，这个按键的信息被送入计算机，计算机用ASCII码的规则对其进行编码，将其转化为61H存储在内存的指定空间中；文本编辑软件从内存中取出61H，将其送到显卡上的显存中。

### 7.3 以字符形式给出的数据

我们可以在汇编程序中，用**单引号**指明数据时以字符的形式给出，编译器将把他们转化为对应的ASCII码。如下代码：

```x86asm
assume cs:code, ds:data
data segment
  db 'unIX'
  db 'foRK'
data ends
code segment
  start: mov al, 'a'
         mov bl, 'b'
         mov ax, 4c00h
         int 21h
code ends
end start
```
这里```mov al, 'a'```相当于```mov al, 61H```，可以使用debug查看。电脑会直接将字符转化为ASCII码。

### 7.4 大小写转换的问题

| 大写 | 十六进制 | 二进制   | 小写 | 十六进制 | 二进制   |
|------|----------|----------|------|----------|----------|
| A    | 41       | 01000001 | a    | 61       | 01100001 |
| B    | 42       | 01000010 | b    | 62       | 01100010 |
| ...  | ...      | ...      | ...  | ...      | ...      |

同理我们发现如果将'a'的ASCII码值减去20H，就会得到'A'。相应的二进制第5位上多了一个 1。

可以通过ASCII码的二进制形式来不需要判断相应字符大小写来直接对其进行改写大小写，代码如下：

```x86asm
assume cs:codesg, ds:datasg

datasg segment
  db 'BaSiC'
  db 'iNfOrMaTiOn'
datasg ends

codesg segment
start:  mov ax, datasg
        mov ds, ax    ;设置ds指向datasg

        mov bx, 0    ;设置ds:[bx]指向‘BaSiC’第一个字母

        mov cx, 5
      s:mov al, [bx]  ;将ASCII码从ds:bx所指向的单元中取出
        and al, 11011111B  ;将ASCII第五位改为0，变为大写字母
        mov [bx], al      ;将转变后的ASCII码写回原单元
        inc bx
        loop s

        mov bx, 5
        
        mov cx, 11
     s0:mov al, [bx]
        or al, 00100000B
        mov [bx], al
        inc bx
        loop s0

        mov ax, 4c00h
        int 21h

codesg ends
end start
```
