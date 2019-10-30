---
layout: post
title: 汇编语言 实验4 [bx]和loop的使用
date: 2019-10-30 11:04:24.000000000 +09:00
---

### 实验4 [bx]和loop的使用

问题1：编程， 向内存0:200~0:23F依次复制数据0~63(3FH)。

```x86asm
assume cs:code
code segment

    mov ax, 0020h     ;0:200~0:23F相当于0020h:0~0020h:23f
    mov ds, ax
    mov bx, 0
    mov cx, 64

s:  mov ds:[bx], bl   ;这里因为直接从0开始复制

    inc bx
    loop s

    mov ax, 4c00h
    int 21h

code ends
end
```

问题2：将上述代码```mov ax, 4c00h```之前的代码复制到内存0:200处。

```x86asm
assume cs:code
code segment

    mov ax, code    ; 数据和代码对于CPU来讲一样，只识别其CS:IP的指向
    mov ds, ax
    mov ax, 0020h
    mov es, ax

    mov bx, 0
    mov cx, 17h     ; 这里多加了10H，是因为程序代码
                    ; 前存在长度为10H的段前缀区域(PSP), 见4.9

s:  mov al, ds:[bx]
    mov es:[bx], al
    inc bx
    loop s

    mov ax, 4c00h
    int 21h

code ends
end
```
