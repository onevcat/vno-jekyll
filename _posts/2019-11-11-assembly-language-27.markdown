---
layout: post
title: 汇编语言 7.5 7.6 通过[bx+idata]进行数组处理
date: 2019-11-11 10:39:24.000000000 +09:00
tags: 汇编语言
---

### 7.5 [bx+idata]

例如我们要访问地址[10H], 可以进行如下变换：

$$[bx=10H]=[bx=8H+2H]$$

[bx+idata]表示一个内存单元，它的偏移地址为(bx)+idata (bx中的数值加上idata)。

将这种操作代入指令中，如```mov ax, [bx+200]```，含义为：

$$(ax)=((ds)*16+(bx)+200)$$

[bx+idata]的形式有多种方法，如下等同：

1. mov ax, [200+bx]
2. mov ax, 200[bx]
3. mov ax, [bx].200

### 7.6 用[bx+idata]的方式进行数组的处理

首先复习一下上一篇博客中大小写字母转化的代码（非常重要）：

```x86asm
assume cs:codesg, ds:datasg
datasg segment
  db 'BaSiC'
  db 'MinIX'
datasg ends

codesg segment
  start:  mov ax, datasg
          mov ds, ax

          mov bx, 0
          mov cx, 5
      s:  mov al, ds:[bx]
          and al, 11011111b
          mov ds:[bx], al
          inc bx
          loop s
          
          mov bx, 5
          mov cx, 5
     s0:  mov al, ds:[bx]
          or al, 00100000b
          mov ds:[bx], al
          inc bx
          loop s0

          mov ax, 4c00h
          int 21h

codesg ends
end start
```

利用[bx+idata]的方法对代码进行优化：

```x86asm
assume cs:codesg, ds:datasg
datasg segment
  db 'BaSiC'
  db 'MinIX'
datasg ends

codesg segment
  start:  mov ax, datasg
          mov ds, ax

          mov bx, 0
          mov cx, 5
      s:  mov al, ds:[bx]  ;定义第一个字符串中的字符
          and al, 11011111b
          mov ds:[bx], al  ;定义第二个字符串中的字符

          mov al, ds:[bx+5]
          or al, 00100000b
          mov ds:[bx+5], al

          inc bx
          loop s

codesg ends
end start
```
这里注意以下关系，并可以基于此对代码进行改写，代码完全等效：

$$0[bx]=[bx]=[bx].0=[bx+0]=[0+bx]$$

在C语言中也存在着相同的处理方式，如下代码：

```c
char a[5]="BaSiC";
char b[5]="MinIX";

main()
{
  int i;
  i=0;
  do
  {
  a[i]=a[i]&0xDF;
  b[i]=b[i]|0x20;
  i++;
  }
  while(i<5);
}
```
其中，&含义与and相同，|含义与or相同。

C语言：a[i], b[i]
汇编语言：0[bx], 5[bx]

通过比较，我们可以发现，**[bx+idata]的方式为高级语言实现数组提供了便利机制**。




