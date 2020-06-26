---
layout: post
title: ml-P2 Regression Case Study
date: 2020-06-26 21:08:24.000000000 +09:00
tags: Machine Learning
---

## Regression

+ Stock Market Forecast

$$
f("股票数据") = Dow\ Jones\ Industrial\ Average\ at\ tomorrow
$$

+ Self-driving Car

$$
f("无人车的Sensor") = 方向盘角度
$$

+ Recommendation

$$
f("使用者A\ \ 商品B") = 购买可能性
$$

## Example Application

+ Estimating the Combat Power (CP) of a pokemon after evolution

	用$x$代表宝可梦，其中$x_{s}$代表宝可梦的名称，$x_{cp}$，$x_{w}$代表重量，$x_{h}$代表身高。

$$
f("宝可梦的参数\rarr x") = "CP\ after \ evolution \rightarrow y"
$$

#### Step 1: Model
	
+ A set of function 去描述一个Model:

	$$ y = b + w\cdot x_{cp} $$

	$w$ and $b$ are parameters (can be any value), eg:

 
	$$f_1:y=10.0+9.0\cdot x_{cp} \\f_2:y=9.8 + 9.2\cdot x_{cp} \\f_3:y=-0.8-1.2\cdot x_{cp} \\......$$

	用以上去描述宝可梦的函数式:

	$$f(x)="CP\ after\ evolution" \rarr y$$

	这叫做 **Linear model**，

	$$ y = b + \sum{w_ix_i} $$

	其中，$x_i$：An attribute of input x, 用来描述 `feature`，$w_i$：weight，$b$: bias 。

+ Step 2: Goodness of Function

	引入一些数据来作为 $y=b+w\cdot x_{cp}$ 的 input，比如，第一个数据为杰尼龟的数据，用$x^1$来表示第一个数据的数据集，对应的 output ，即卡咪龟的数据集，用 $\hat{y}^1$ 代表。其他数据以此类推。

	接下来的 Training Data 假设就是 10 只宝可梦。即，

	$$(x^1, \hat{y}^1)\\ (x^2, \hat{y}^2)\\... \\(x^{10}，\hat{y}^{10})$$

	对应图像如下，

	![figure1](/assets/202006/2020-06-26-22-17-41.png)

	图中任意一点的值为 $(x^n_{cp}, \hat{y}^n)$。

	在有了 training data 以后，需要定义另一个Loss function $L$: 其中input 为对应的 function，output 即为 how bad it is，即：

	$$L(f) = L(w, b)\\ =\sum^{10}_{n=1}(\hat{y}^n - (b+w\cdot x^n_{cp}))^2$$

	衡量参数的好坏, 即$w$ 和$b$ 的好坏，

	其中里面的括号中为 Estimated y based on input function，而 $\hat{y}^n$即为真实至，而$L(f)$则给出 Estimation error。

	$\sum$来 Sum over examples。

	图像为，

	![figure2](/assets/202006/2020-06-26-22-36-19.png)

+ Step: Best Function

	在建立了 A set of function 之后，要 pick the BEST Function，

	$$\begin{aligned}f^{*}=& \arg \min _{f} L(f) \\w^{*}, b^{*} &=\arg \min _{w, b} L(w, b) \\&=\arg \min _{w, b} \sum_{n=1}^{10}\left(\hat{y}^{n}-\left(b+w \cdot x_{c p}^{n}\right)\right)^{2}\end{aligned}$$

	可以利用 **Gradient Descent** 来解这个 function。

+ Step 3: Gradient Descent，来解$w^{*}=\arg \min_{w}L(w)$

	- Consider loss function $L(w)$ with one parameter w:
		+ 首先随机选一个起始值 $w^0$

		+ Compute $\frac{dL}{dw}|_{w=w^0}$

			用图像来表示即为，

			![figure3](/assets/202006/2020-06-26-22-49-54.png)

			寻找下一个$w^1$的值，即为

			$$w^1 \larr w^0 - \eta \frac{dL}{dw}|_{w=w^0}$$

			其中 $\eta$ 被称为 "**learning rate**"，越大学习速度越快。

		+ 下一步重复 Compute $\frac{dL}{dw}|_{w=w^1}$

		+ ... Many iterations ( T times )

			这时候的情况如下图：

			![figure4](/assets/202006/2020-06-26-23-00-53.png)

			这时获得了 **Local optimal** $\rarr w^*$，但注意是并非 **Global optimal** 。

			



	











	











