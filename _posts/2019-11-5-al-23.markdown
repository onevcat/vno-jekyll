---
layout: post
title: 汇编语言 6.2 6.3 在代码中使用段 将数据代码栈放入不同的段
date: 2019-11-05 19:22:24.000000000 +09:00
---

### 6.2 在代码中使用栈

让我们利用栈，将程序中定义的数据逆序存放。

实现代码如下：

```x86asm
assume cs:codesg
codesg segment
    
    dw 0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h

    dw 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ;这里dw定义了16个字型数据，在程序加在后，将取得16个字
    ;的内存空间，存放这16个数据。后面将这段空间当作栈来使用

start:  mov ax, cs
        mov ss, ax
        mov sp, 30h  ;栈顶ss:sp指向cs:30h 
        ; 这里ss:sp指向16 + 32 = 48 = 30h

        mov bx, 0
        mov cx, 8
    s:  push cs:[bx]
        add bx, 2
        loop s      ;0~15单元中的8个字型数据一次入栈
        mov bx, 0
        mov cx, 8
    s0: pop cs:[bx]
        add bx, 2
        loop s0     ;依次出栈8个字型数据到代码段0~15单元中

        mov ax, 4c00h
        int 21h

codesg ends
end start
```

这里将以上代码对比下面这个代码，实现0:0~0:15单元中的内容的正序改写，通用利用栈来完成：

```x86asm
assume cd:codesg
codesg segment
    dw 0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h
    dw 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
start:  mov ax, cs  ;这里可以mov ax, codesg
        mov ss, ax
        mov sp, 24h ;指向栈顶

        mov ax, 0
        mov ds, ax
        mov bx, 0

        mov cx, 8
    s:  push [bx]
        pop cs:[bx] ;也可以pop ss:[bx], 因为代码段这是与栈中数据一致
        add bx, 2
        loop s

        mov ax, 4c00h
        int 21h
codesg ends
end start
```

对比和第一个程序的差别，这个程序是入栈一行代码直接出栈到这一行，保证程序的正方向。

### 6.3 将数据、代码、栈放入不同的段

目前, 如果我们对于数据，代码，栈全部存放在代码段中有两个问题：

1. 非常混乱
2. 数据、栈和代码需要的空间如果超过64KB，就无法放在一个段中(x86cpu)

我们可以用下面的代码来解决这两个问题：

```x86asm
assume cs:code, ds:data, ss:stack
data segment
    dw 0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h
stack segment
    dw 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
stack ends
code segment
start: mov ax, stack
       mov ss, ax
       mov sp, 20h

       mov ax, data
       mov ds, ax  ;ds:bx指向data段

       mov bx, 0

       mov cs, 8
s:     push [bx]
       add bx, 2
       loop s

       mov bx, 0

       mov cx, 8

s0:    pop [bx]
       add bx, 2
       loop s0

       mov ax, 4c00h
       int 21h

code ends
end start
```

注意：

1. 源程序中"data", "code", "stack"均只是我们的命名，CPU不会识别
2. 伪指令中```assume cscode, ds:data, ss:stack```将cs, ds, ss分别与code, data, stack相连。但其是伪指令，是由编译器执行的，cpu同样无法识别
3. CPU的识别其实靠的是控制cs, ds, ss的相关地址来识别相应的数据信息的

