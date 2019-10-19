---
layout: post
title: 如何利用dosbox搭建mac, linux masm环境
date: 2019-10-19 12:03:24.000000000 +09:00
---

之前介绍过如何dosbox运性debug，这里介绍一下如何用doxbox运行汇编语言的调试包。

首先[下载MASM5.0软件包](http://cdn.suiyuanjian.com/masm5.zip)。

安装好后，运用之前的方法进行虚拟盘挂载。

挂载好后，将masm5 软件包所有内容进行拷贝，为了方便可以将测试用的汇编程序test.asm 放在相同文件夹

之后就可以执行相关编译连接指令

```asm
>>>masm test.asm
>>>link test.asm
>>>ml test.asm
...
```

