---
layout: post
title: C语言 简介以及C转化asm的初尝试
date: 2019-11-22 10:55:24.000000000 +09:00
tags: C语言
---
整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

#### 编译的概念

将助记符转化为机器码的过程叫做编译。

#### C语言的优势

(1) 效率高

C语言相对于其他第三代编程语言，C语言是编译型语言，源代码最终编译为机器语言，也就是可执行文件，从此CPU就可以直接执行。编译型语言与解释型语言的对比：

| C语言    | Python  |
|----------|---------|
| 汇编语言 | 字节码  |
| 机器语言 | 解释器  |
| CPU执行  | CPU执行 |

(2) 灵活度高

C语言不仅提供**多种运算符**，还可以完成类似计算机底层操作的位运算，**语法简单、约束少**，拥有丰富多变的结构和数据类型，还**拥有可以直接操作计算机硬件的能力**。**指针是C语言的灵魂**。

(3) 可移植性高

不同机器上的C语言编译程序80%的代码是公共的。

#### 第一个程序

```cpp
//HelloWorld.c
#include <stdio.h>
int main(void)
{
      printf("Hello world!\n");
      return 0;
}

$ gcc test1.c && ./a.out
Hello world!
```

#### 关于C转化asm的尝试

目前我所摸索的方法主要有两种：

(1) 我的第一个中尝试是利用gcc编译命令

```bash
gcc -S test1.c
```

通过这种方法编译获得asm文件test1.s，查看代码如下：

```asm
	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movl	$0, -4(%rbp)
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -8(%rbp)          ## 4-byte Spill
	movl	%ecx, %eax
	addq	$16, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Hello world!\n"


.subsections_via_symbols
```

但是遗憾的是，这种并不是我所经常接触的x86asm代码。

(2) 第二种尝试，利用debug程序跟踪编译出的程序。

查看其代码段以及对应偏移地址的机器码

![figure1](/assets/201911/2019-11-22_11-19-37.png)

将这段代码利用U命令查看其汇编指令：

![figure2](/assets/201911/2019-11-22_11-23-21.png)

结果看得一头雾水。。。

我们将用D命令查看更多的机器码以及ASCII码

![figure3](/assets/201911/2019-11-22_11-26-50.png)

还是摸不清头绪，先保留吧，以后解决。

