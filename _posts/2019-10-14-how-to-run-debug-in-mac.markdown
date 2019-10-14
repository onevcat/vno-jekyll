---
layout: post
title: 在mac或者linux运行debug的优雅解决方案
date: 2019-10-14 12:16:24.000000000 +09:00
---

I want to run debug in mac or linux sys, however, debug is only designed for windows.

There are two ways:

1. Just install the win virtual box
2. (Recommend) install DOS virtual box [DOSBox here](https://www.dosbox.com/download.php?main=1)

#### For the DOSBox 

When you have installed the DOSBox, firstly mount the disk (mount at c: for example):

```cmd
mount c ~/dos/debug/
c:
debug
```

