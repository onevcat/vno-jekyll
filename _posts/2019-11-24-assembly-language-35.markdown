---
layout: post
title: 汇编语言 8.7 8.8 8.9 div 伪指令dd dup
date: 2019-11-24 16:15:24.000000000 +09:00
tags: 汇编语言
---

### 8.7 div 指令

`div`是除法指令，有以下注意事项：

1. 除数：有8位和16位两种，在一个reg或者内存单元中。
2. 被除数：默认放在ax或dx和ax中，如果除数为8位，被除数则为16位，默认在ax中存放；如果除数为16位，则被除数则为32位，在dx和ax中存放，dx存放高16位，ax存放在低16位。
3. 结果：如果除数为8位，则**al存储除法操作的商, ah存储除法操作的余数**；如果除数为16位，则**ax存储除法操作的商，dx存储除法操作的余数**。

除数和被除数的规格总结：

| 除数 | 被除数 |
|------|--------|
| 8位  | 16位   |
| 16位 | 32位   |

ps:

1. 被除数的规格受除数控制
2. 被除数规格往往比除数要大，是为了防止数据溢出问题

伪代码表示如下：

> `div byte ptr ds:[0]`

(al) = (ax) / ((ds) * 16 + 0)---商
(ah) = (ax) / ((ds) * 16 + 0)---余数

> `div word ptr es:[0]`

(ax) = [(dx) * 10000H + (ax)] / ((es) * 16 + 0)   商
(dx) = [(dx) * 10000H + (ax)] / ((es) * 16 + 0)   余数

> `div byte ptr [bx + si + 8]`

(al) = (ax) / ((ds) * 16 + (bx) + (si) + 8)    商
(ah) = (ax) / ((ds) * 16 + (bx) + (si) + 8)    余数

> `div word ptr [bx + si + 8]`

(ax) = [(dx) * 10000H + (ax)] / ((ds) * 16 + (bx) + (si) + 8)    商
(dx) = [(ds) * 10000H + (ax)] / ((ds) * 16 + (bx) + (si) + 8)    余数

例1. 利用div计算100001/100

代码如下：

```x86asm
mov dx, 1
mov ax, 86A1H    ;(dx) * 10000H + (ax) = 100001
                 ;100001 = 186A1H = 10000H + 86A1H
mov bx, 100
div bx
```
### 8.8 伪指令dd

dd用来定义dword (double word, 32bit) 型数据。

```x86asm
data segment
  db 1
  dw 1
  dd 1
data ends
```
第一个数据为01H，在data:0处，1 bit。
第二个数据为0001H，在data:1处，1 word。
第三个数据为00000001H, 在data:3处，占2 words。

例2. 用data段第一个数据段除以第二个数据后的商，放于第三个数据的存储单元中。

```x86asm
data segment
  dd 100001
  dw 100
  dw 0
data ends
```

代码段为：

```x86asm
mov ax, data
mov ds, ax
mov ax, ds:[0]  ;ds:[0]指向dd中的低16位，并存放于ax中
mov dx, ds:[2]  ;ds:[2]指向dd中的高16位，并存放于dx中
div word ptr ds:[4]
mov ds:[6], ax
```

### 8.9 dup

用法：

```x86asm
db num dup  ;相当于定义重复的字节型数据
dw num dup
dd num dup
```
如下代码：

```x86asm
stack segment
  db 200 dup (0)
stack ends
```

