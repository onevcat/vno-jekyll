---
layout: post
title: 汇编语言 第七章总结 实验6 Debug跟踪问题7.9
date: 2019-11-18 15:56.24.000000000 +09:00
tags: 汇编语言
---

### 问题7.9

编程，将datasg段中每个单词的前4个字母改为大写字母。

```x86asm
assume cs:codesg, ss:stacksg, ds:datasg

stacksg segment
  dw 0,0,0,0,0,0,0,0
stacksg ends

datasg segment
  db '1. display      '
  db '2. brows        '
  db '3. replace      '
  db '4. modify       '
datasg ends

codesg segment
  start:
codesg ends

end start
```

数据结构分析如下图：

![figure](/assets/201911/2019-11-18_16-06-11.png)

```x86asm
assume cs:codesg, ss:stacksg, ds:datasg 
stacksg segment
	dw 0,0,0,0,0,0,0,0
stacksg ends

datasg segment
  db '1. display      '
  db '2. brows        '
  db '3. replace      '
  db '4. modify       '
datasg ends

codesg segment
	start: mov ax, stacksg
				 mov ss, ax
				 mov sp, 16  ;这里要把指针指到空栈的位置
				 mov ax, datasg
				 mov ds, ax
				 mov bx, 0

				 mov cx, 4
		 s0: push cx
				 mov si, 0

				 mov cx, 4
		  s: mov al, [bx+3+si]
				 and al, 11011111b
				 mov [bx+3+si], al

				 inc si
				 loop s

			  add bx, 16
				pop cx
				loop s0
				
				mov ax, 4c00H
				int 21H
codesg ends
end start
```

对程序进行汇编与连接。并使用debug进行调试：

![figure2](/assets/201911/2019-11-18_17-07-16.png)

我们运行第一步后查看对应的栈内信息：

![figure3](/assets/201911/2019-11-18_17-10-01.png)

可以看出栈内情况，如stacksg一致。

![figure4](/assets/201911/2019-11-18_17-18-29.png)

经过第一轮大写修改后，可以看到数据段第一个字母被大写成功。

![figure5](/assets/201911/2019-11-18_17-21-10.png)

用p指令跳过循环后，观察数据段，第一行的前四个字母已经被大写成功。

同理，我们将所有循环执行完毕，观察改写情况，发现已经全部改写成功。

![figure6](/assets/201911/2019-11-18_17-24-12.png)

