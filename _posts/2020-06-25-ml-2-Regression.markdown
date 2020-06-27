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
f("宝可梦的参数\rightarrow x") = "CP\ after \ evolution \rightarrow y"
$$

#### Step 1: Model
	
+ A set of function 去描述一个Model:

	$$ y = b + w\cdot x_{cp} $$

	$w$ and $b$ are parameters (can be any value), eg:

 
	$$f_1:y=10.0+9.0\cdot x_{cp} \\f_2:y=9.8 + 9.2\cdot x_{cp} \\f_3:y=-0.8-1.2\cdot x_{cp} \\......$$

	用以上去描述宝可梦的函数式:

	$$f(x)="CP\ after\ evolution" \rightarrow y$$

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

		+ Compute 

			$$\left.\frac{dL}{dw}\right|_{w=w^0}$$

			用图像来表示即为，

			![figure3](/assets/202006/2020-06-26-22-49-54.png)

			寻找下一个$w^1$的值，即为

			$$w^1 \leftarrow w^0 - \left.\eta \frac{dL}{dw}\right|_{w=w^0}$$

			其中 $\eta$ 被称为 "**learning rate**"，越大学习速度越快。

		+ 下一步重复 Compute 
			$$\left.\frac{dL}{dw}\right| _{w=w^1}$$

		+ ... Many iterations ( T times )

			这时候的情况如下图：

			![figure4](/assets/202006/2020-06-26-23-00-53.png)

			这时获得了 **Local optimal** $\rightarrow w^T$，但注意是并非 **Global optimal** 。
			
	+ 如果有两个参数呢?
	
		对应公式如下，

		$$w^*, b^* = \arg \min_{w, b}L(w, b)$$

		- 随机 Pick an initial value $w^0, b^0$
		 
		- Compute

			$$\left.\frac{\partial L}{\partial w}\right|_{w=w^{0}, b=b^{0}},\left.\frac{\partial L}{\partial b}\right|_{w=w^0, b=b^0}$$

		- 分别更新 $w$ 与 $b$ 的值

		$$ w^1 \leftarrow w^0 - \left.\eta\frac{\partial L}{\partial w}\right|_{w=w^0, b=b^0}\\ b^1 \leftarrow b^0 - \left.\eta\frac{\partial L}{\partial b}\right|_{w=w^0, b=b^0}$$

		- Compute

		$$ \left.\frac{\partial L}{\partial w}\right|_{w=w^1, b=b^1}, \left.\frac{\partial L}{\partial b}\right|_{w=w^1, b=b^1}

		- 再次更新 $w$，$b$ 的值

		$$ w^2 \leftarrow w^1 - \left.\eta\frac{\partial L}{\partial w}\right|_{w=w^1, b=b^1}\\ b^2 \leftarrow b^1 - \left.\eta\frac{\partial L}{\partial b}\right|_{w=w^1, b=b^1}$$
	
		- 反复重复这个步骤最终获得 loss 相对比较小的 $w$ 和 $b$ 的值

		- 而 $\nabla L$ 即为 **gradient** ：

		$$\nabla L=\left[\begin{array}{l}\frac{\partial L}{\partial w} \\ \frac{\partial L}{\partial b}\end{array}\right] _\text { gradient }$$	

			其中，将两个偏微分排成一个 vector

		- 示意图如下，

		![figure5](/assets/202006/2020-06-27-13-42-50.png)

		其中每一次的 **gradient** 即为等高线的法线法向。

		- 但用这种方法，会出现问题，即如下图左侧所示，如果起点不同可能会找到不同的输出值，但实际上，利用这种方法是不会产生 **local optimal** 的

		![figure6](/assets/202006/2020-06-27_13-47-03.png)

		- Formulation of $\partial L / \partial w$ and $\partial L / \partial b$，即为

		$$\begin{array}{l}L(w, b)=\sum_{n=1}^{10} ({\left.\hat{y}^{n}-\left(b+w \cdot x_{c p}^{n}\right)\right)^{2}} \\\\\frac{\partial L}{\partial w}=? \sum_{n=1}^{10} 2\left(\hat{y}^{n}-\left(b+w \cdot x_{c p}^{n}\right)\right)\left(-x_{c p}^{n}\right) \\\\\frac{\partial L}{\partial b}=? \sum_{n=1}^{10} 2\left(\hat{y}^{n}-\left(b+w \cdot x_{c p}^{n}\right)\right)(-1)\end{array}$$

	+ How's the results?

		![figure6](/assets/202006/2020-06-27-14-55-10.png)

		可以获得 Average Error on Training Data为，

		$$ \sum_{n=1}^{10}e^n = 31.9 $$

	+ 但是真正关心的应该是 **Generalization**，What we reaaly care about is the error on new data (testing data)

		于是又取了十只 Pokemon，情况如下

		![figure7](/assets/202006/2020-06-27-15-00-34.png)

		而新的数据中的 Average Error on Training Data 为 35.0

	+ How can we do better

		- 从上图中可见在CP较低和较高的区域，拟合不好，于是我们选择令 Selecting another Model

			$$ y = b+ w_1\cdot x_{cp}+w_2\cdot (x_{cp})^2$$

			找出 Best function，这时

			$$ b= -10.3, \\w_1=1.0, w_2=2.7*10^{-3}\\ \text{Average Error} = 18.4$$

			![figure8](/assets/202006/2020-06-27_15-10-09.png)

			重新取 10 只 Pokemon 得出，Average Error = 18.4

		- Better! Could it be even better?

			引入更复杂的model，

			$$ y = b + w_1 \cdot x_{cp}+w_2\cdot (x_{cp})^2 + w_3\cdot (x_{cp})^3$$

			找出 Best Function，

			$$ b=6.4, w_1=0.66\\ w_2=4.3*10^{-3},\\ w_3=-1.8*1-^{-6}, \\Average Error = 15.3$$

			同样重新取 10 只 Pokemon ，得出 Average Error = 18.1
			
			![figure9](/assets/202006/2020-06-27_15-17-30.png)

		- 用同样的方法，Try to make it better

			$$ y = b + w_1\cdot x_{cp}+ w_2\cdot (x_{cp})^2 + w_3\cdot (x_{cp})^3 + w_4\cdot (x_{cp})^4$$

			并获得图像，

			![figure10](/assets/202006/2020-06-27_15-21-53.png)

			这时的 Average Error = 14.9，但重新取 10 只 Average Error = 28.8 变得比之前更高了

		- 继续使用更加复杂的 Model，结果会变得更加糟糕

			$$ y = b+w_1\cdot x_{cp} +w_2\cdot (x_{cp})^2 + w_3\cdot(x_{cp})^3 + w_4\cdot (x_{cp})^4 + w_5\cdot (x_{cp})^5 $$

			![figure11](/assets/202006/2020-06-27_20-54-10.png)

		- 分析这 5 个 Model，对这5次的 Training Data 的 Average Error 进行统计，如下图

			![figure12](/assets/202006/2020-06-27_20-59-37.png)

			这是因为更复杂的 Model 的 Function Space 会包含低级的 Model Space，如下图描述

			![figure13](/assets/202006/2020-06-27_21-04-39.png)

			但如果针对于，Testing Data，则情况会不同，

			![figure14](/assets/202006/2020-06-27_21-06-56.png)

			A more complex model does not always lead to better performance on **testing data**, This is **Overfitting**.

			而当 Model 的复杂程度在第 4 次和第 5 次时，就发生了 Overfitting。

+ What are the hiden factors?
	
	在计算CP值时，前面的 input 数据选用的只有杰尼龟一种，一旦要是，但是要去 make a more general model，就要考虑Pokemon的种类这一问题。

	![figure15](/assets/202006/2020-06-27_21-18-21.png)

	如何解决这个问题呢？

	- Back to step 1: Redesign the fuction set of the Model

		可以套用 `if` 语句：

		![figure16](/assets/202006/2020-06-27_21-21-42.png)

		接下来，我们需要将加入`if`语句的 Model 改写为 Linear model ($y=b+\sum{w_i x_i}$)：

		$$\begin{aligned}y=& b_{1} \cdot \delta\left(x_{s}=\text { Pidgey }\right) \\&+w_{1} \cdot \delta\left(x_{s}=\text { Pidgey }\right) x_{c p} \\&+b_{2} \cdot \delta\left(x_{s}=\text { Weedle }\right) \\&+w_{2} \cdot \delta\left(x_{s}=\text { Weedle }\right) x_{c p} \\&+b_{3} \cdot \delta\left(x_{s}=\text { Caterpie }\right) \\&+w_{3} \cdot \delta\left(x_{s}=\text { caterpie }\right) x_{c p} \\&+b_{4} \cdot \delta\left(x_{s}=\text { Eevee }\right) \\&+w_{4} \cdot \delta\left(x_{s}=\text { Eevee }\right) x_{c p}\end{aligned}$$	

		其中，

		$$ \delta(x_s = Pidgey) \ \  \left\{\begin{array}{ll}=1 & \text { If } x_{s}=\text { Pidgey } \\ =0 & \text { otherwise }\end{array}\right.$$

		这样就有:

		$$ if \ x_s = Pidgey，\\ y = b_1 + w_1\cdot x_{cp} $$

		其中，

		$$\delta(x_s = Pidgey)$$

		这一项即为 Linear model 中的 $x_i$，也就是 **feature**

		引入不同 $x_s$ 后的分析图像如下图，

		![figure17](/assets/202006/2020-06-27_21-40-34.png)

		从图中可见，不考虑伊布的曲线fit的不好，是因为伊布可以进化为不同的精灵，但其他宝可梦也有一些或多或少fit不好的情况，可能是进化时候加了一个 random number，但也可能不是 random number，也可能有其他factors

	- Are there any other hidden factors？

		![figure18](/assets/202006/2020-06-27_21-47-07.png)

		对待这个问题，有可能是很多因素导致的，如 weight，HP 等等，那么如何解决这个问题呢？我们可以将所有的能考虑到因素加进去：

		![figure19](/assets/202006/2020-06-27_22-11-13.png)

		这么复杂的 Model 给出了很低的 Training Error = 1.9，但Testing Error 却非常糟糕 = 102.3，发生了严重的 Overfitting。

		解决这个问题，我们要引出下一个概念：

	- Back to step 2: Regularization，重新定义我们的 Loss Function，将不好的去掉

		即在原有的 Loss function 后添加一项：

		$$ L = \sum_n(\hat{y}^n - (b + \sum{w_i x_i}))^2 + \lambda \sum(w_i)^2$$

		而这个 $\lambda\sum(w_i)^2$ 项，The functions with smaller w_i are better
		
		**Why smooth functions are preferred?**

		比如我们在 input $x_i$ 的基础上，增加为 $x_i + \Delta x_i$，则此时 对于 $y=b+\sum w_i x_i$ output 变为 $w_i\Delta x_i$，则当 $w_i$越小，input 对 output 影响越小，这样 function 也就会比较平滑

		**If some noises corrupt input $x_i$ when testing**，也就是是说 function 如果变得不平滑了，A smoother function has less influence。

		![figure20](/assets/202006/2020-06-27_22-30-35.png)

		首先可以确定，当 $lambda$ 越大，function 越平滑，但 function 越平滑，Traning data error 越大，这是因为：**Larger $lambda$，considering the training error less**，越倾向于考虑 $w_i$ 本来的值。

		但 Testing error 却发生不同的变化，可见：**We prefer smooth function, but don't be too smooth**。

		所以我们需要调整一个较好的 $\lambda$，这是非常重要的。

	- 另外需要注意的是，对于 Regularization 项：

		$$\lambda\sum(w_i)^2$$

		只包含有 $w_i$，但却没有 $b$，其实在考虑 Regularization时，不需要考虑 bias。因为加 bias 只会对 function 进行平移，不会影响 function 的平滑度。

+ Conclusion:

	- Gradient descent

		- Following lectures: theory and tips

	- Overfitting and Regularization

		- Following lectures: more theory behind these

	- We finally get average error = 11.1 on the testing data
		- How about another set of new data? Underestimate? Overestimate?

		- Following lectures: validation 来解决上面的问题。

	

	
		







		




			












	











