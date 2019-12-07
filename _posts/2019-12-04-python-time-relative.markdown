---
layout: post
title: python 时间处理模块总结
date: 2019-12-04 21:47:24.000000000 +09:00
tags: python
---
整理自小甲鱼[鱼C论坛](https://fishc.com.cn/)

### python中与时间处理总结

Python中，与时间有关的模块包括：time，datetime以及calender。

> datetime模块

#### datetime支持的时间范围

object.MINYEAR = 1
object.MAXYEAR = 9999

#### timedelta类属性

| timedelta.min        | timedelta(\-999999999)                                                           |
|----------------------|----------------------------------------------------------------------------------|
| timedelta.max        | timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999) |
| timedelta.resolution | timedelta(miacroseconds=1)                                                       |

注意：**timedelta.max > -timedelta.min, -timedelta.max无意义**

#### timedelta实例属性(只读)

| 属性                   | 取值范围                |
|------------------------|-------------------------|
| timedelta.days         | \-999999999 ~ 999999999 |
| timedelta.seconds      | 0 ~ 86399               |
| timedelta.microseconds | 0 ~ 999999              |

#### datetime模块中定义的类

| 定义的类           | 说明                  | 常用属性                                                    |
|--------------------|-----------------------|-------------------------------------------------------------|
| datetime.date      | 表示日期的类          | year, month, day                                            |
| datetime.time      | 表示时间的类          | hour, minute, second, microsecond, tzinfo                   |
| datetime.datetime  | 表示日期和时间的类    | year, month, day, hour, minute, second, microsecond, tzinfo |
| datetime.timedelta | 表示时间间隔的类      | 两个时间点date, time, datetime之间的长度                    |
| datetime.tzinfo    | 表示时区的基类        | 为time与datetime类提供调整的基准                            |
| datetime.timezone  | 表示UTC时区的固定偏移 | 是tzinfo基类的实现                                          |

#### timedelta对象详解

timedelta对象表示两个日期或时间之间的间隔

```python
data.timedelta(days = 0, seconds = 0, microseconds = 0, milliseconds = 0, minutes = 0, hours = 0, weeks = 0)
```

默认参数可以是整数，浮点数，整数或复数，默认为0。**内部存储单位只有days，seconds以及microseconds，其他单位需要进行换算**。

#### timedelta对象支持的操作

| 操作                 | 结果                                                                           |
|----------------------|--------------------------------------------------------------------------------|
| t1=t2+t3             |                                                                                |
| t1=t2-t3             |                                                                                |
| t1=t2*i              | 对象乘以一个整数                                                               |
| t1=t2*f              | 对象乘以一个浮点数，结果四舍五入到精度timedelta.resolution                     |
| f=t2/t3              | t2和t3的商，返回一个float对象                                                  |
| t1=t2/f或t1=t2/i     | 对象除以一个整数或浮点数，结果四舍五入到精度                                   |
| t1=t2//i或t1=t2//t3  | 对象地板除一个整数或浮点数，结果社区小鼠，返回一个整数                         |
| t1=t2%t3             | t2和t3的余数，返回一个timedelta对象                                            |
| q,r = divmod(t1, t2) | 计算t1和t2的商和余数，q=t1//t2，r=t1%t2, q是一个整数，r是一个timedelta对象     |
| \+t1                 | 返回一个timedelta对象，且值相同                                                |
| \-t1                 | 等同于timedelta(\-t1.days, \-t1.seconds, \-t1.microseconds)，并且相当于t1\*\-1 |
| abs(t)               | 当t.days >= 0时，等同于\+t；当t.days <= 0时，等同\-t                           |
| str(t)               | 返回一个字符串，格式为：[D day[s], ][H]H:MM:SS[.UUUUUU]                        |
| repr(t)              | 返回一个字符串，格式为：datetime.timedelta(D[, S[, U]])                        |

#### timedelta的实例方法

`timedelta.total_seconds()` 返回timedelta对象所包含的总秒数，相当于td/timedelta(seconds=1)

请注意，对于非常大的时间间隔(大于270年),这种方法将失去微妙(microsecond)精度。

> date 对象

date对象表示一个日期，在一个理想化的日历里，日期由year, month, day。

`datetime.date(year, month, day)`

#### date参数的范围

参数必需为整数并且满足一下范围：

1. MINYEAR <= year <= MAXYEAR (也就是 1 ~ 9999)
2. 1 <= month <= 12
3. 1 <= day <= 根据year 和 month来决定(例如闰年和非闰年的二月问题)

#### date类方法(classmethod):

| classmethod                  | 功能                               |
|------------------------------|------------------------------------|
| date.today()                 | 返回一个表示当前本地日期的date对象 |
| date.fromtimestam(timestamp) | 根据给定的timestamp返回date对象    |
| date.fromordinal(ordinal)    | 将Gregorian日历时间转换为date对象  |

#### date类属性

| 类属性          | 说明                  |
|-----------------|-----------------------|
| date.min        | date(MINYEAR, 1, 1)   |
| date.max        | date(MAXYEAR, 12, 31) |
| date.resolution | timedelta(days=1)     |

#### date实例属性(只读)

| 属性       | 取值范围                  |
|------------|---------------------------|
| date.year  | MINYEAR~MAXYEAR(1~9999)   |
| date.month | 1~12                      |
| date.day   | 1~根据year和month具体确定 |

#### 对象支持的操作

| 操作                      | 结果                            |
|---------------------------|---------------------------------|
| date2 = date1 + timedelta | 日期+时间间隔，返回新的日期对象 |
| date2 = date1 - timedelta |                                 |
| timedelta = date1 - date2 |                                 |
| date1 < date2             | 比较两个日期前后                |

#### date实例方法：

| 实例方法                       | 功能                                                                            |
|--------------------------------|---------------------------------------------------------------------------------|
| date.replace(year, month, day) | 生成一个新的日期对象，用参数指定的年月日代替原有属性                            |
| date.timetuple()               | 返回日期对应的time.struct\_time对象(类似于time.localtime())                     |
| date.toordinal()               | 返回日期对应的Gregorian Calendar日期                                            |
| date.weekday()                 | 返回0~6表示星期几(星期一是0，以此类推)                                          |
| date.isoweekday()              | 返回1~7表示星期几(星期一是1，以此类推)                                          |
| date.isocalendar()             | 返回一个三元组格式(year, month, day)                                            |
| date.isoformat()               | 返回一个ISO 8601格式的日期字符串，如"YYYY\-MM\-DD"的字符串                      |
| date.\_\_str\_\_()             | 对于date对象d来说，str(d)相当于d.isoformat()                                    |
| date.ctime()                   | 返回一个表示日期的字符串，同time.ctime(time.mktime(d/timetuple()))              |
| date.strftime(format)          | 返回自定义格式化字符串表示日期                                                  |
| date.\_\_format\_\_(format)    | 跟date.strftime(format)一样，这使得调用str.format()时可以指定data对象的的字符串 |

代码示例：

```python
from datetime import date
d = date.fromordinal(735678)  # 1.1.0001后735678天
>>> d
datetime.date(2015, 3, 21)
>>> t = d.timetuple()
>>> for i in t:
        print(i)

2015
3
21
0
0
0
5
80
-1

>>> ic = d.isocalendar()    #对比d.timetuple()方法的输出数据
>>> for i in ic:
        print(i)

2015
12
6

>>> d.isoformat()    # ISO 8601格式输出，“YYYY-MM-DD”
'2015-03-21'

>>> d.strftime("%d/%m/%y")    #自定义输出格式
'21/03/15'

>>> d.strftime("%A %d. %B %Y")    #%A大写的周
'Saturday 21. March 2015'

>>> 'The {1} is {0:%d}, the {2} is {0:%b}.'.format(d, "day", "month")
'The day is 21, the month is March.'
```

> time 对象

time对象表示一天中的一个时间，可以通过tzinfo对象进行调整。

`datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)`

#### time 参数范围

所有参数都是可选的，tzinfo可以是None或者tzinfo子类的实例对象；其余参数可以是整数，并在一下范围内：

1. 0 <= hour < 24
2. 0 <= minute < 60
3. 0 <= second < 60
4. 0 <= microsecond < 1000000

注：如果参数超出范围，将引发ValueError

#### time 类属性

| 类属性          | 说明                      |
|-----------------|---------------------------|
| time.min        | time(0, 0, 0, 0)          |
| time.max        | time(23, 59, 59, 999999)  |
| time.resolution | timedelta(microseconds=1) |

#### time 属性(只读)

| 属性             | 取值范围                     |
|------------------|------------------------------|
| time.hour        | 0~23                         |
| time.minute      | 0~59                         |
| time.second      | 0~59                         |
| time.microsecond | 0~999999                     |
| time.tzinfo      | 通过构造函数的tzinfo参数赋值 |

#### time 实例方法

| 实例方法                                                          | 说明                                                                    |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|
| time.replace([hour[, minute[, second[, microsecond[, tzinfo]]]]]) | 生成一个新的日期对象，用参数指定，时间代替原有属性                      |
| time.isoformat()                                                  | 返回一个ISO 8601 格式的日期字符串，如"HH:MM:SS.mmmmmm"的字符串          |
| time.\_\_str\_\_()                                                | 对于time对象t来说，str(t)相当于t.isoformat()                            |
| time.strftime(format)                                             | 返回自定义格式化字符串表示时间                                          |
| time.\_\_format\_\_(format)                                       | 同time.strftime(format)，使得调用str.format()时可以指定time对象的字符串 |
| time.utcoffset()                                                  | 如果tzinfo属性是None，则返回None；否则返回self.tzinfo.utcoffset(self)   |
| time.dst()                                                        | 如果tzinfo属性是None，则返回None；否则返回self.tzinfo.tzname(self)      |

time 代码示例，

```python
>>> fromt datetime import time, timedelta, tzinfo
>>> class GMT1(tzinfo):
        def utcoffset(self, dt):
            return timedelta(hours=1)
        def dst(self, dt):
            return timedelta(0)
        def tzname(self, dt):
            return "欧洲/布拉格"

>>> t = time(14, 10, 30, tzinfo=GMT1())
>>> t
datetime.time(14, 10, 30, tzinfo=<__main__.GMT1 object at 0x02D7FE90)
>>> gmt = GMT1()
>>> t.isoformat()
'14:10:30+01:00'
>>> t.dst()
datetime.timedelta(0)
>>> t.tzname()
'欧洲/布拉格'
>>> t.strftime("%H:%M:%S %Z")
'14:10:30 欧洲/布拉格'
>>> 'The {} is {:%H:%M}.'.format("time", t)
'The time is 14:10.'
```

> datetime对象

datetime对象是date对象和time对象的结合体，并且包含他们所有的信息。

`datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)`

#### datetime 参数范围

必须的参数为year, month, day; tzinfo 可以是None或者tzinfo子类的实例对象；其余的参数可以是整数，范围同上，不做赘述。

#### datetime 实例属性(只读)

datetime实例属性同上，不做赘述。

#### datetime对象支持的操作

同date对象支持的操作，不做赘述。

#### datetime 类方法(classmethod)

| 类方法                                     | 说明                                                                                     |
|--------------------------------------------|------------------------------------------------------------------------------------------|
| datetime.today()                           | 返回一个表示当前本地时间的datetime对象，同datetime.fromtimestamp(time.time())            |
| datetime.now(tz=None)                      | 返回一个表示当前本地时间的datetime对象；如果提供了参数tz，则获取tz参数所指时区的本地时间 |
| datetime.utcnow()                          | 返回一个当前UTC时间的datetime对象                                                        |
| datetime.fromtimestamp(timestamp, tz=None) | 根据时间戳创建一个datetime对象，参数tz指定时区信息                                       |
| datetime.utcfromtimestamp(timestamp)       | 根据时间戳创建一个UTC时间的datetime对象                                                  |
| datetime.fromordinal(ordinal)              | 返回对应Gregorian日历时间对应的datetime对象                                              |
| datetime.combine(date, time)               | 根据参数date和time，创建一个datetime对象                                                 |
| datetime.strptime(date\_string, format)    | 将格式化字符串转化为datetime对象                                                         |

#### datetime 类属性

参考time和date，不做赘述

#### datetime 实例方法

| 实例方法                                                                               | 说明                                                                                         |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| datetime.date()                                                                        | 返回一个date对象datetime.time()， 返回一个time对象(tzinfo属性为None)                         |
| datetime.timetz()                                                                      | 返回一个time()对象(带有tzinfo属性)                                                           |
| datetime.replace([year[,month,[day[,hour[,minute[,second[,microsecond[,tzinfo]]]]]]]]) | 生成一个新的日期对象，用参数指定日期和时间代替原有对象中的属性                               |
| datetime.astimezone(tz=None)                                                           | 传入一个新的tzinfo属性，返回根据新时区调整好的datetime对象                                   |
| datetime.utcoffset()                                                                   | 如果tzinfo为None，返回None；否则返回self.tzinfo.utcoffset(self)                              |
| datetime.dst()                                                                         | tzinfo为None，返回None；否则返回self.tzinfo.dst(self)                                        |
| datetime.tzname()                                                                      | tzinfo为None，返回None；否则返回self.tzinfo.tzname(self)                                     |
| datetime.timetuple()                                                                   | 返回日期对应的time.struct\_time对象(类似于time模块的time.localtime())                        |
| datetime.utctimetuple()                                                                | 返回UTC日期对应的time.struct\_time对象                                                       |
| datetime.timestamp()                                                                   | 返回当前时间的时间戳(类似于time 模块的time.time())                                           |
| date.weekday()                                                                         | 返回0~6表示星期几(星期一是0，以此类推))                                                      |
| datetime.isoweekday()                                                                  | 返回1~7表示星期几                                                                            |
| datetime.isocalendar()                                                                 | 返回一个三元组格式(year, month, day)                                                         |
| datetime.isoformat(sep='T')                                                            | 返回一个ISO 8601格式的日期字符串，如"YYYY\-MM\-DD"的字符串                                   |
| datetime.\_\_str\_\_()                                                                 | 对于date对象来说，str(d)相当于d.isoformat()                                                  |
| datetime.ctime()                                                                       | 返回一个表示日期的字符串，相当于time模块的time.ctime(time.ctime(time.mktime(d.timetuple()))) |
| datetime.strftime(format)                                                              | 返回自定义格式化字符串表示日期                                                               |
| datetime.\_\_format\_\_(format)                                                        | 与datetime.strftime(format)一样，这使得调用str.format()时可以指定data对象的字符串            |

> 格式化字符串： strftime() 和 strptime()

date, datetime 和time均支持strftime(format)方法，将指定日期或时间转化为自定义的格式化字符串。

datetime.strptime()类方法把格式化字符串转换为datetime对象。

| 格式化指令 | 含义                                                                        |
|------------|-----------------------------------------------------------------------------|
| %a         | Mon, Tue, Wed...                                                            |
| %A         | Monday, Tuesday, Wednesday...                                               |
| %w         | 一个星期中的第几天，0星期天，6星期六                                        |
| %d         | 在一个月的第几天(01,02,...,31)                                              |
| %b         | Jan, Feb...                                                                 |
| %B         | January, February...                                                        |
| %m         | 月份(01, 02...)                                                             |
| %y         | 两个数字表示年份，2014 == 14                                                |
| %Y         | 四个数字表示年份                                                            |
| %H         | 24小时(00, 01, ..., 23)                                                     |
| %I         | 12小时(01, 02, ..., 11)                                                     |
| %p         | AM或PM                                                                      |
| %M         | 分钟(00, 01, ..., 59)                                                       |
| %S         | 秒                                                                          |
| %f         | 微秒(000000, 000001, ..., 999999)                                           |
| %z         | 与UTC时间的间隔；如果本地时间，返回空字符串((empty), \+0000,\-0400, \+1030) |
| %Z         | 时区名称；如果是本地时间，返回空字符串((empty), UTC, ET, CST)               |
| %j         | 在一年中的第几天(001, 002, ..., 366)                                        |
| %U         | 在一年中的第几周，星期天作为第一天(00, 01, ..., 53)                         |
| %W         | 在一年中的第几周，星期一作为第一天(00, 01, ..., 53)                         |
| %c         | 用字符串表示日期和时间(Tue Aug 16 21\:30\:00 2014)                          |
| %x         | 用字符串表示日期(08/16/24)                                                  |
| %X         | 用字符串表示时间(21\:30\:00)                                                |
| %%         | 表示百分号                                                                  |



















