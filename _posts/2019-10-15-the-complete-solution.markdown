---
layout: post
title: LA3.3 The Complete Solution to Ax=b
date: 2019-10-15 16:07:24.000000000 +09:00
---

### Simply show the Row Echelon Form R with b at the right side

At the LA3.2, we didn't pay much attention to the right side $b$, it is **because $b$ is $0$ when we only talk about the nullspace of A**.

For now, in LA3.3, $b$ is not zero. As the Row Echelon Form $R$ is very important which can show clearly how the free column is combinated by the pivot column (LA3.2). How to make show the Row Echelon Form R? We use the augmented matrix to make like this,<br>
$$\begin{bmatrix}A&b\\\end{bmatrix}$$
---> 
$$\begin{bmatrix}R&d\\\end{bmatrix}$$
 and make this transformation very naturally and simply.

### One Particular Solution $Ax_p = b$

For an easy solution $x_p$, choose the free variables to be zero, and from **free variables = zero**, we can get the ***pivot variables from d***.

> For a solution to exist, zero rows in $R$ must also be zero in $d$. Since $I$ is in the pivot rows and pivot columns of $R$, the pivot variables in $x_{particular}$ come from $d$.

Now we get 2 equations, as seen below:

$x_{particular}$ solves $Ax_p=b$<br>
$x_{nullspace}$ solves $Ax_n=0$

Here we introduce the complete solution of x, and very very gracefully.

$x = x_p + x_n=$
$$\begin{bmatrix}1\\0\\6\\0\\\end{bmatrix}$$
 + 
$x_2$
$$\begin{bmatrix}-3\\1\\0\\0\\\end{bmatrix}$$
 + 
$x_4$
$$\begin{bmatrix}-2\\0\\-4\\1\\\end{bmatrix}$$
, for example.

> Here come an easy question. When $m = n =r$, what will happen? <br>
The particular solution is the one and the only solution $x_p = A^{-1}b$. There are no special or free variables. $R=I$ has no zero rows. The only vector in the nullspace is $x_n=0$. The complete solution is $x=x_p+x_n=A^{-1}b+0$.

Every matrix $A$ with **full column rank** $(r=n)$ has all these properties:

1. All columns of $A$ are pivot columns.
2. There are no free variables or specitial solutions.
3. The nullspace $N(A)$ contains only the zero vector $x=0$.
4. If $Ax=b$ has a solution (it might not) then it has only one solution.

> With full column rank, $Ax=b$ has one solution or *no solution* ($m>n$, overdetermined).

### The Complete Solution

Now let's talk about the other extreme case, ***full row rank***.

Every matrix $A$ with ***full row rank*** $(r=m)$ has all these properties:

1. All rows have pivots, and $R$ **has no zero rows**.
2. $Ax = b$ has a **solution for every right side b.
3. The column space is the whole space $R^m$.
4. There are $n-r=n-m$ special solutions in the nullspace of $A$.

> If $m<n$ the equation $Ax=b$ is underdetermined (many solutions).

In this case with $m$ pivots, the rows are "***linearly independent***". So the columns of $A^T$ are linearly independent. The nullspace of $A^T$ is the zero vector.

> It's because, the columns can't be in the same plane to make the the nullspace of $A^T$ to be zero vector.

