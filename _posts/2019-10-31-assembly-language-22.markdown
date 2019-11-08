---
layout: post
title: 汇编语言 6.1 在CS中使用数据
date: 2019-10-31 16:43:24.000000000 +09:00
tags: 汇编语言
---

### 6.1 在代码段中使用数据

这里有个问题，我们希望使用loop的方法将如下数据累加和。

数据如下：

0123H、0456H、0789H、0ABCH、0DEFH、0FEDH、0CBAH、0987H

为此我们进行了编程，代码如下：

```x86asm
assume cs:code
code segment
  dw 0123H, 0456H, 0789H, 0ABCH, 0DEFH, 0FEDH, 0CBAH, 0987H  ;dw意为define word

  mov bx, 0
  mov ax, 0

  mov cx, 8

s:add ax, cs:[bx]
  add bx, 2
  loop s

  mov ax, 4c00h
  int 21h

code ends
end
```

对此我们进行编译与连接，并使用debug对其进行调试。

![figure1](/assets/201910/2019-10-31_17-10-03.png)

图中我们可以看到数据已经被拷贝到了对应的代码段内（```076A:0000~076A:000F```），然后我们通过```-u```命令查看机器指令。

![figure2](/assets/201910/2019-10-31_17-13-43.png)

奇怪的是，即使到了```076A:000F```，偏移地址已经超过了CS中所存储数据的总长度，仍然见不到我们所需要的指令。

原来，CPU错把存储在CS中的数据也当成了指令并进行了编译，运行程序一定会出错。

解决办法很简单，只需要人为指定一个入口，代码如下：

```x86asm
assume cs:code
code segment
  dw 0123H, 0456H, 0789H, 0ABCH, 0DEFH, 0FEDH, 0CBAH, 0987H  ;dw意为define word

start:  mov bx, 0   ;给定入口，供CPU识别出从哪里开始是指令代码
        mov ax, 0
      
        mov cx, 8
      
      s:add ax, cs:[bx]
        add bx, 2
        loop s
      
        mov ax, 4c00h
        int 21h
      
code ends
end start
```

总结一下end的用法：

1. 通知编译器程序结束
2. 通知编译器程序的入口在什么地方，所以入口的名称'start'可以自定义






