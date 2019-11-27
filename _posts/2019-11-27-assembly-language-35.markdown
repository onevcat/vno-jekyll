---
layout: post
title: 汇编语言 实验7 寻址方式在结构化数据访问中的应用
date: 2019-11-27 17:02:24.000000000 +09:00
tags: 汇编语言
---

题目如下：

![figure1](/assets/201911/2019-11-27_17-08-54.png)
![figure2](/assets/201911/2019-11-27_17-10-14.png)
![figure3](/assets/201911/2019-11-27_17-12-12.png)

```x86asm

assume cs:codesg, ds:data, es:table data segment
	db '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983'
	db '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992'
	db '1993', '1994', '1995'
; 以上是表示21年的21个字符串

	dd 16, 22, 382, 1356, 2390, 8000, 16000, 24486, 50065, 97479, 140417, 197514
	dd 345980, 590827, 803530, 1183000, 1843000, 2759000, 3753000, 4649000, 5937000
; 以上是表示21年公司总收入的21个dword型数据

	dw 3, 7, 9, 13, 28, 38, 130, 220, 476, 778, 1001, 1442, 2258, 2793, 4037, 5635, 8226
	dw 11542, 14430, 15257, 17800
; 以上是表示21年公司雇员人数的21个word型数据
data ends

table segment
	db 21 dup ('year summ ne ?? ')
table ends

codesg segment

	start: mov ax, data
				 mov ds, ax
				 mov ax, table
				 mov es, ax
	
				 mov bx, 0
				 mov si, 0
				 mov di, 0
				 mov cx, 21
	
	    s: mov al, [bx]      ;对年份进行mov
			   mov es:[di], al
				 mov al, [bx+1]
				 mov es:[di+1], al
				 mov al, [bx+2]
				 mov es:[di+2], al
				 mov al, [bx+3]
				 mov es:[di+3], al
	
				 mov ax, 54H[bx]   ;对收入进行mov，数据类型是dd，所以分开两个通用寄存器
				 mov dx, 56H[bx]
				 mov es:5h[di], ax  ;注意上第三图中的空格
				 mov es:7h[di], dx  ;低位存放在低位，高位数据存放在高位
	
				 mov ax, 0A8H[si]  ;对雇员数进行mov
				 mov es:0AH[di], ax
	
				 mov ax, 54h[bx]  ;工资总数除以雇员
				 mov dx, 56h[bx]
				 div word ptr ds:0A8H[si]
				 mov es:0dh[di], ax  ;默认商保存在ax中，不保留余数
	
				 add bx, 4    ;指针4个字节
				 add si, 2    ;2个字节
				 add di, 16    ;指针行
					
 loop s

mov ax, 4c00h
int 21h

codesg ends
end start

```

