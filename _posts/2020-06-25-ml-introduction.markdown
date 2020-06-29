---
layout: post
title: ml-P1 Machine Learning Introduction
date: 2020-06-25 21:31:24.000000000 +09:00
tags: MachineLearning
---

整理自[李宏毅教授 2020 机器学习课程](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html)

## 什么是机器学习

机器学习就是自动找一个函数关系式

+ Speech Recognition

+ Image Recognition

+ Playing Go

+ Dialogue System

## 机器学习的第一步

> 你自己想要找什么样的函数关系式

+ Regression: 现在要找的函数的输出是一个数值。

	- 作业1，预测未来某个时刻的PM2.5，输出值是一个scalar

+ Binary Classification: 输出只有两个可能，Yes or No。

	- 作业 RNN，输入句子，输出句子是正面的还是负面的。

+ Multi-class Classification: 让机器来做选择题，选出正确的。

	- 作业 CNN，输入图片，选出这个图片对应的种类

但是机器学习不只有Regression 和 Classification。

其他的种类被称为Generation（生成）

产生有结构的复杂产物

+ Generation：GAN
	- 让机器画图

## 怎么告诉机器，你想要找什么样的函数关系式

+ Supervised Learning：最为常见的，比如知道输入是一张图片，输出是该图片的类别。

	1. 给定一些图片，把理想的图片规定为哪一种类，这一过程称为Label
	
	2. 评估这个函数关系式的好坏，也就是Loss，给定几张来用某一函式来评价对错，并计算错误率，该错误率称为Loss，Loss越小越好。
	
+ Reinfocement Learning：以围棋为例。

	- Supervised：给机器一个input，告诉理想的是什么样的，然后输出下一步最应该落子的位置在哪里

	- Reinforcement Learning: 让机器和其他人去下，赢了或输了让机器自己分析，赢了或者输了就叫做Reward，Alpha Go is supervised learning + reinforcement learning

## 机器怎么实际找出想要找出的函数式呢

+ 给定函数式寻找范围 Network Architecture

	- RNN
	 
	- CNN

+ 怎么从范围中找出最好的函数式呢？Deep Learning Framework

	- Gradient Descent

## 前沿研究

+ Expainable AI：以认猫为例，如何告诉用户是一只猫的理由是什么？
	
	- CNN required

+ Adversarial Attack：假设辨识非常强了，用户怀恶意去特意攻击这个函数式，会发生什么？

+ Network Compression：如何将硕大的Network缩小，比如移植到手机上

+ Anormaly Detection：如果输入了错误的数据，会发生什么。如何让机器知道他不认识这个错误的数据

+ Transfer Learning （Domain Adversarial Learning），输入数据时输入了不同类型的数据，比如正常是灰度的数字，而实际上却输入了彩色的数字。即，如何在输入数据和测试数据不同的时候，仍然能够让机器学到东西

+ Meta Learning：比机器学习更进一步，机器是让机器具有学习的能力。Meta Learning则令机器具有了学习如何学习的能力。因为先在的学习效率很低，需要有更好的学习效果。

+ Life-long learning：让机器一连串的任务，终生不断学习。又称为Continuous Learning或者Never Ending Learning

## General Regulations

+ Environment

	- 建议用Linux或macOS
	- python 3.6.8
	- Pyenv

+ Kaggle：是一个庞大的资料科学社群，上面有各种资料分析的竞赛。

+ Github

	```
	git config --global user.name "name" # 设置用户名
	git config --global user.email "name@gmail.com" 
	git config --list # 检查是否设定完成
	git init
	git add example.sh # 将特定档案加入追踪
	git add --all
	git rm --cache train.csv
	git commit -m "Description"
	git remote add origin http://... # 与Github地址连起来
	git push -u origin
	```

	







	


