---
layout: post
title: 使用Python 读写Excel (1)
date: 2019-10-26 22:32:24.000000000 +09:00
tags: python
---

openpyxl 模块简单易用、功能广泛，单元格格式、图片、表格、公式、筛选、批注、文件保护等功能都具有，图表功能是其一大特点。

### openpyxl模块的安装

```
pip install openpyxl
```

### 创建并保存Excel文件

通过调用openpyxl.Workbook()生成一个Workbook的实例化对象，这个就代表一个工作簿：

```python
import openpyxl

wb = openpyxl.Workbook()

# 获取活跃的工作表
ws = wb.active

# 数据可以直接赋值给单元格
ws['A1'] = 520

# 可以整行添加
ws.append([1, 2, 3])

# Python 类型将自动转换
import datetime
ws['A3'] = datetime.datetime.now()

# 保存文件
wb.save("demo.xlsx")<Paste>
```
对应excel输出结果如图：

![figure1](/assets/201910/2019-10-26_22-46-46.png)


