---
layout: post
title: 汇编语言 8.6 寻址方式的综合应用
date: 2019-11-21 15:47:24.000000000 +09:00
tags: 汇编语言
---

### 8.6 寻址方式的综合应用

按照王爽教材里给的例子：

| 公司名称 | DEC       |
| 总裁姓名 | Ken Olsen |
| 排名     | 137       |
| 收入     | 40        |
| 著名产品 | PDP       |

以上是DEC公司1982年的情况，到了1988年DEC公司的信息放生了变化，如下：

| 公司名称 | DEC       |
| 总裁姓名 | Ken Olsen |
| 排名     | 38        |
| 收入     | +70       |
| 著名产品 | VAX       |

利用汇编语言来对对应数据进行修改。

![figure1](/assets/201911/2019-11-21_15-53-09.png)

代码如下：

```x86asm
mov ax, seg  ;seg:60
mov ds, ax
mov bx, 60h  ;设置seg的偏移地址

mov word ptr [bx+0Ch], 38
add word ptr [bx+0Eh], 70

mov si, 0
mov byte ptr [bx+10h+si], 'V'  ;字符串占用3个字节
inc si
mov byte ptr [bx+10h+si], 'A'
inc si
mov byte prt [bx+10h_si], 'X'
```

观察相同功能的C语言代码：

```cpp
struct company {    /*定义公司记录的结构体*/
    char cn[3];     /*公司名称*/
    char hn[9];     /*总裁姓名*/
    int  pm;        /*排    名*/
    int  sr;        /*收    入*/
    char cp[3];     /*注明产品*/
    };
struct company dec={"DEC", "Ken Olsen", 137, 40, "PDP"};
/*定义一个公司记录的变量，内存中将存有一条公司的记录*/
```
```cpp
main()
{
 int i;
 dec.pm=38;
 dec.sr=dec.sr+70;
 i=0;
 dec.cp[i]='V';
 i++;
 dec.cp[i]='A';
 i++;
 dec.cp[i]='x';
 return 0;
}
```
对应C语言风格，将汇编语言代码进行改写：

```x86asm
mov ax, seg
mov ds, ax
mov bx, 60h
mov word ptr [bx].0ch, 38
add word ptr [bx].0eh, 70

mov si, 0
mov byte ptr [bx].10h[si], 'V'
inc si
mov byte ptr [bx].10h[si], 'A'
inc si
mov byte ptr [bx].10h[si], 'X'
```

从这个例子看，有几个收获与结论：

1. 我们再编程的时候，从结构化的角度去看待所要处理的数据。
2. 一个结构化的数据包含了多个数据项。
3. 8086CPU提供的[bx+si+idata]的寻址方式为结构化数据的处理提供了方便。
4. **我们可以用[bx+idata+si]的方式来访问结构体中的数据。用bx定位整体结构体，用idata定位结构体中的某一个数据项，用si定位数组项中的每一个元素。为此，汇编语言提供了更贴切的书写方式，`[bx].idata`、`[bx].idata[si]`。

> 对比C语言和汇编语言代码，我们可以看到，如`dec.cp[i]`与汇编语言的`bx.10h[si]`是很相似的。



