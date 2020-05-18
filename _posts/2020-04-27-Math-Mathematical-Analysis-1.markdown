---
layout: post
title: 数学分析 §1 实数和数列极限
date: 2020-04-27 11:03:24.000000000 +09:00
tags: 数学
---

## § 1.1 实数

任何有理数r都可以表示为两个整数之商：

$$r = \frac{p}{q}$$

### 1.1.1 数轴的建立

其中 $p,q\in Z$ 且$q\neq 0$。根据以上定义首先建立数轴:

![fig1](/assets/202004/f1.png)


建立坐标轴后，就可以建立平面和空间坐标系，从而**建立解析几何学**。

### 1.1.2 建立数轴后引出的2个问题

#### **问题1.** 数轴上每一个点对应一个实数为其坐标，那么每一个实数是否都是数轴上某一点坐标呢？

+ 对固定的正整数 $q$，让 $p$ 取遍所有整数，则 $p/q$ 这些数字把数轴分成了长度为 $1/q$ 的区间。

+ 令每一个实数 $x$ 位于这些中的一个区间，也就是说对任意固定的实数 $x$ 一定可以找出一个整数 $p$ ，使得，

$$\frac{p}{q} \leq x<\frac{p+1}{q} \qquad (1)$$

![fig2](/assets/202004/f2.png)

由 (1) 可得，

$$
\frac{p}{q} \leq x<\frac{p+1}{q}
$$

即，$\forall x$ ，总能找到一个有理数 $p/q$ 和$x$的距离可以小于 $1/q$ 。

如一个新的实数点 $x'$，要证明 $x-\varepsilon$ 与 $x+\varepsilon$ 之间有无穷多个数，则

$$\left|x-\frac{p}{q}\right|<\frac{1}{q}<\varepsilon \Rightarrow q>\frac{1}{\varepsilon}$$

故有，

$$
\left|x-\frac{p}{q}\right|<\varepsilon
$$

即找到了一个有理数 $p/q$ 确实落在 $\varepsilon$ 的区间内部。

根据这个问题，我们得到两个结论：

1. **有理数在数轴上是稠密的**<br>
+ 即随便取一个实数，在充分小的区间就能找到无穷多有理数。
+ 同样的，在充分小的区间内有一个有理数，也就相当于有无穷多个有理数。
2. **任何实数，都可以由无理数来任意逼近**

#### **问题2.** 有理数是连续的吗？即无理数的引出

例题：若 $n$不是平方数，那么 $\sqrt{n}$ 不是有理数。

证明：假定

$$
\sqrt{n}=\frac{p}{q}
$$
就有，
$$
n=\frac{p^{2}}{q^{2}} \quad, \quad p^{2}=n q^{2} \qquad (2) 
$$

其中，$p$ 和 $q$ 的定义同 **问题1**。

由 $p/q$ 一定不是整数得到，

$$
m<\frac{p}{q}<m+1 \quad\left(m \in N^{*}\right) \quad \rightarrow \quad mq<p<m q+q
$$

即，

$$
0<p-m q<q
$$

由 (2) 得，

$$
p^{2}-p m q=n q^{2}-p m q
$$

$$
p(p-m q)=q(n q-p m) \rightarrow \frac{p}{q}=\frac{n q-p m}{p-m q} \quad (3)
$$

令 (3) 等于 $p_1/q_1$，由

$$
p-m q>0 \rightarrow q_{1}>0 \rightarrow 0<q_{1}<q
$$

$$
p_{1}=\frac{q_{1}}{q} \times p<p
$$

推出以下关系式，

$$
\sqrt{n}=\frac{p}{q}=\frac{n q-p m}{p-m q}=\frac{p_{1}}{q_{1}}=\frac{p_{2}}{q_{2}}= \cdots \quad (4)
$$

但由于 $p$ 与 $q$ 均为正整数，所以不可能无限制 (4) 中的关系，所以假设不成立，所以 $\sqrt{n}$ 不是有理数。

## § 1.2 无尽小数

任何一个*有理数*是有穷小数或者*无穷循环小数*，我们可以从以下实例中得到证明。

$$
\begin{array}{l}
a=1.\dot{2}3\dot{4} =1+0.\dot{2}3 \dot{4}=1+b \\
\\
b=0 . \dot{2}3\dot{4} \\
\\
10^{3} b=234. \dot{2}3\dot{4}=234+b \\
\\
(10^3-1) b=234, \quad b=\frac{234}{999}=\frac{26}{111} \\
\\
\rightarrow a=1+\frac{26}{111}=\frac{137}{111}
\end{array}
$$

实际上，实数都可以表示为无尽小数。

$$
n. a_{1} a_{2} a_{3}...
$$

而实数本身可以分为有理数 (循环小数) 及无理数 (不循环小数)。

数轴上的任何一个点一定对应着一个实数，但大多数在数轴上是对不准的。

这里就引入另外一个定理，**区间套定理**，如对于点，

$$
a=n.a_{1} a_{2} a_{3}
$$

![figure3](/assets/202004/f3.png)

$
\left[a_{1}, a_{2}\right] > \left[a_{1}, b_{2}\right]>\left[a_{3}, b_{3}\right]>\ldots
$ 不断循环嵌套下去，存在唯一一个点与之对应。

**即实数与数轴上的点是一一对应的。**

## § 1.3 收敛和收敛数列

当 $n$ 很大时，$a_{n}$ 无限接近，即

$$
a_{n} \rightarrow a \Rightarrow n \rightarrow \infty时 \lim _{i \rightarrow \infty} a_{n}=a
$$

用一个数轴来描述a的 $\varepsilon$ 邻域，

![figure4](/assets/202004/f4.png)

对 $\forall \varepsilon > 0$，$\exists N \in N^{*}$ 当 $n > N$ 时， 

$$
a-\varepsilon<a_{n}<a+\varepsilon
$$

当 $n>N$ 时，

$$
a_{1} a_{2} ... a_{N}(有限项)|a_{N+1}...(无限项)
$$

#### 定义1.2.1

$$
\left|a_{n}-a\right|<\varepsilon \Rightarrow a-\varepsilon<a<a+\varepsilon
$$

#### 几个重要的结论及证明

**结论一**

$$
|q|<| \quad \lim _{n \rightarrow \infty} q^{n}=0
$$

证明：

+ 方法 1

	- $q=0$ 时，显然成立
	- 当 $0< |q| <1$ 时，


$$
\begin{array}{c}
\alpha=\frac{1}{|q|}-1>0, \quad \frac{1}{|q|}=1+\alpha, \quad|q|=\frac{1}{1+\alpha} \\
\\
\forall \varepsilon>0, \quad \exists N \in N^{*}, \quad n>N \quad\left|q^{n}\right|<\varepsilon \\
\\
\left|q^{n}\right|=|q|^{n}=\frac{1}{(1+\alpha)^{n}}=\frac{1}{1+n \alpha+\cdots \cdots \alpha^{n}}<\frac{1}{n a}<\varepsilon \\
\\
n>\frac{1}{\alpha \varepsilon} \quad, \quad N=\left[\frac{1}{\alpha \varepsilon}\right]
\end{array}
$$

+ 方法 2

$$
|q|^{n}<\varepsilon, \quad n \cdot \log |q|<\log \varepsilon, \quad n>\frac{\log \varepsilon}{\log |q|},  \quad N=\left[\frac{\log \varepsilon}{\log |q|}\right]
$$

**结论二**

$$
\lim _{n \rightarrow \infty} \sqrt[n]{n}=1
$$

证明：

$$
\forall \varepsilon>0, \quad \exists N, \quad n>N 时, \quad |^{n}\sqrt{n}-1 |<\varepsilon
$$

$$
^n\sqrt{n} = ^n\sqrt{1*1*...*1((n-2)个1)*\sqrt{n}} <\frac{n-2+2 \sqrt{n}}{n}=\frac{n+2(\sqrt{n}-1)}{n}=1+\frac{2(\sqrt{n}-1)}{n}
$$

$$
0 \leqslant {^n\sqrt{n}}-1<\frac{2(\sqrt{n}-1)}{n}=\frac{2(\sqrt{n}-1)}{\sqrt{n} \cdot \sqrt{n}}<\frac{2}{\sqrt{n}} \Rightarrow n>\frac{4}{\varepsilon^{2}}
$$

$$
N=\left[\frac{4}{\varepsilon^{2}}\right]
$$











































