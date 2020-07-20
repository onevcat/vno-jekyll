---
layout: post
title: JavaScript 基础
date: 2020-07-16 22:24:24.000000000 +09:00
tags: blog
---

<!-- TOC GFM -->

* [什么是 JavaScript](#什么是-javascript)
* [三种方式添加 JavaScript](#三种方式添加-javascript)
* [总汇](#总汇)
* [字符串方法](#字符串方法)
* [逻辑操作符](#逻辑操作符)
* [变量与常量](#变量与常量)
* [运算符](#运算符)
* [控制结构](#控制结构)
* [循环](#循环)
	- [`while` 循环](#while-循环)
	- [作用域](#作用域)
	- [`for` 循环](#for-循环)
* [判断](#判断)
	- [三元操作符](#三元操作符)
	- [`switch`](#switch)
* [对象](#对象)
* [数组](#数组)
* [函数](#函数)
* [闭包](#闭包)

<!-- /TOC -->

## 什么是 JavaScript

+ 一种编程语言，可以在网页上实现复杂的功能，交互等
+ 解释型语言
+ 运行在客户端
+ 面向对象语言

## 三种方式添加 JavaScript

+ 内部的 JavaScript

	```js
	<script>
		// Your JavaScript
	</script>
	```

+ 外部的 JavaScript

	```js
	<script src="script.js"></script>
	```

+ 内联的 JavaScript (不推荐🙅‍♀️)

	```js
	<button
	onclick="createParagraph()">
	Click me
	</button>
	```

## 总汇

+ 类型
	- JavaScript 不区分整数型和浮点型，采用的双精度 64 位格式。
	
	```js
	> 0.1 + 0.2
	< 0.30000000000000004
	```

	```js
	> Math.PI
	> Math.sin(3)
	```
	
+ 对象
+ 变量
+ 数组
+ 运算符
+ 函数
+ 控制结构
+ 闭包

## 字符串方法

可以使用 `"".` 来查看字符串方法。

以下举一些例子：

```js
alert("Hello" + " world");

console.log("hello".length);   /*输出文字*/

console.log("hello".charAt(0));    /*输出文字特定位置字*/

console.log("hello, world".replace("hello", "goodbye"));

console.log("hello,world".toUpperCase());
```

## 逻辑操作符

```js
> 1 === 1
< true

> 1 > 2
< false

> 1>= 1
< true

> true && false   <!--&& 判断前后两个值是否都为真-->
< false

> false && false
< false

> true || true    <!--判断前后两个值是否有一个为真-->
< true

> true || false
< true

> true
< true

> !true
< false
```

## 变量与常量

```js
var name = "DasAuto";
console.log(name);     <!--打印 name 变量-->
                       <!--name 变量可以被更改-->

<!--也可以使用 let 来新建变量-->
let a = 1;
console.log(a);

<!--const 可以用于定义常量，注意不能进行更改-->
const Pi = 3.14;
console.log(Pi);
Pi = 3.141
> Uncaught TypeError: Assignment to constant variable.
	at main.js:21
```

## 运算符

```js
var x = 5;
console.log(x + 5);

<!--x 可以被重新赋值-->
// x = x + 5;
x += 5;

// x = x + 1;
x ++;

<!--同理也有自减符号-->
// x = x - 1;
x -= 1;
x --;

console.log(x);

<!--注意区分数字与字符串-->
x = "3" + "4";  // 结果为 34

x = "3" + 4 + 5;  // 结果为 345，其等同于
                  // x = "3" + "4" + "5"

x = 3 + 4 + "5";  // 结果为 75

<!--判断符号-->
<!--== 带有自动转换，=== 则不能-->
console.log(123 == "123"); // "123" "123"，ture
console.log(123 === "123"); // 123 "123"，false
1 == ture // ture
1 === ture //  false
```

## 控制结构

`if (条件)`，成立后执行方法。不成立，检查 `else if (条件)` 是否成立。 不成立最终执行 `else` 中的方法。

```js
var name = "Simon":
var age = 20

if (name == "Simon" && age == 21) {
	console.log{"Simon"};
} else if (name == "John") {
	console.log("John");
} else {
	console.log("Stranger");
}
```

## 循环

### `while` 循环

`while (条件)`，成立后进入循环。

```js
while (true) {
	console.log("ture");
}
<!--会一直循环-->
```

`do {} while ()` 先执行 `do {}` 中的内容，进行后进入 `while (条件)` 来判断是否继续循环。

```js
var age = 20
var a = 19

do {
	a ++;
	console.log(a);
} while (age == a);
```

### 作用域

变量可以用 `let` 或者 `var` 新建，对于 `var` 而言是没有作用域的，即在所有地方都可以对 `var` 来进行访问。

如下面代码中：

```js
if (true) {
	var age = 20;
}

var a = 19;

do {
	a++;
	console.log(a);d

} while (age == a);
```

如果将 `var age = 20;` 改为 `let age = 20;`，则会出现在后面 `do {} while ()` 语句中无法访问 `age` 的情况。

值得注意的是，`const` 同样受作用域制约。

### `for` 循环

`for(初始化条件;条件;做什么){}'

如下代码：

```js
for(let i = 0; i < 5; i++){
	age++;
	console.log(age)  \\ 该命令后 执行 `i++`
}
```
## 判断

### 三元操作符

```js
var name = "Daniel";
var age = 20;

var allowed = (age >= 18) ? "Yes" : "No"; \\ `:` 为二选一，`?` 为将二选一中满足条件的，赋值给 allowed

console.log(allowed);
```

### `switch`

给 `switch` 传入几个 `case` 来做判断。

```js
swicth(name) {
	case 'Simon':
		console.log("Simon");
		break;
	case 'John':
		console.log("John");
		break;
	default:
		console.log("Stranger");
}
```

## 对象

```js
var obj = new Object();
var obj2 = {};

obj = {
	name: "Simon",
	age: '20',
	email: "Simon@gamil.com",
	contact: {
		phone: "1234567"
		Telegram: "@Simon"
	}
}

console.log(obj.contact.phone);
// console.log(["contact"]["phone"]);
```

+ 使用 `obj.property` 的形式来提取出对应属性。

+ 也可以用 `["contact"]["phone"];` 达到相同的目的。

+ 对应属性的值可以进行更改。

+ 当添加新的属性，将自动添加对应的新属性以及值。
	
	`obj.contact.WeChat = "abcd"`

## 数组

```js
var a = new Array();
var b = [];
// 两者都可以用来新建数组

a[0] = "dog";

console.log(a);

// 可以用 a.length 访问其长度属性
console.log(a.length);

a[1] = "cat";
a[5] = "tiger";

console.log(a);
// 这时会打印 ["dog", "cat", empty * 3, "tiger"]
// 并且长度 length属性变为 6

console.log(a[2]);
// 当我们调用 empty 处位置值时，会提示未定义

// 当然我们也可以直接定义一个数组，保证不会出现隔空
b = ["dog", "cat", "tiger"];
console.log(b);

// 打印出数组 b 中的所有项
for (let i = 0; i < b.length; i++) {
	console.log(b[i]);
}

// 也可以使用这种方法
for(let i in a) {
	console.log(a[i]);
}
// 注意虽然 a 中有三个空项，但使用 for in 的方法不会打印空项
// dog
// cat
// tiger

// 相对的，如果使用普通的 let 方法，在数组中 empty 的位置会出现 undefined
for (let i = 0; i < b.length; i++) {
	console.log(a[i]);
}
// dog
// cat
// undefined

a.forEach(function(value)) {
	console.log(value);
});


// 在数组中最后添加项
b.push("sheep");

// 在数组中末尾删除项
b.pop();

// 倒叙数组
b.reverse();

// 删除第一个项
b.shift();

// 在第一个位置添加
b.unshift("lion");
```

关于数组方法，更多的可以访问:

[**mozilla 数组文档**](https://developer.mozilla.org/en-US/docs/WebJavaScript/Reference/Global_Objects/Array)

## 函数

```js
let a = 1;

// 定义函数
function add() {
	a++;
}

consloe.log(a);

// 执行函数
add();

// 函数中传入值
function add(x) {
	a += x // a = a + x;
}

add(4);
console.log(a);

// 较复杂的情况，求和函数
function add() {
	let sum = 0;
	// arguments 为 add() 函数中传入的参数
	for (let i = 0, j = arguments.length; i < j; i++) {
		sum += arguments[i];
	}
	return sum;
}
let sum = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
console.log(sum);
```

## 闭包

```js
function makeAdder(a) {
	return function(b) {
		return a + b;
	};
}

var x = makeAdder(5);
var sum = x(6);

console.log(sum);

// 闭包即返回一个函数
```






























