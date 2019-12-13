---
layout: post
title: C语言 如何利用mac xcode实现C语言反汇编
date: 2019-12-13 10:51:24.000000000 +09:00
tags: C语言
---

今天谈一下，如何利用mac系统下的xcode实现类似于windows系统下microsoft visual C++的反汇编功能。

(1) 首先安装xcode
(2) 按顺序在菜单栏目依次选择：file --> new --> Project...
(3) 在新弹出的菜单栏中在最上面选择macos标签页下的Command Line Tool图标，如图所示：
![figure1](/assets/201912/2019-12-13_10-56-11.png)
(4) 在新弹出的菜单栏中的Language选项栏中选择C，
![figure2](/assets/201912/2019-12-13_10-59-12.png)
(5) 主界面上左侧菜单栏中会出现两个文件夹分别存放代码以及编译好的程序，
![figure3](/assets/201912/2019-12-13_11-01-20.png)
(6) 在main.c中输入测试程序，如图，
![figure4](/assets/201912/2019-12-13_11-04-54.png)
(7) 依次在菜单栏选择：Debug --> Debug Workflow --> Always Show Disassembly，勾选此项
(8) 在main.c中加入breakpoint准备对程序进行调试，快捷键：Command + \\\
![figure5](/assets/201912/2019-12-13_11-09-23.png)
(9) 运行程序，快捷键：Command + R
(10) 运行后，反汇编的x86代码就会以分Thread的形式给出，如图所示，
![figure6](/assets/201912/2019-12-13_11-11-38.png)


