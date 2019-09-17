---
layout: post
title: LA3.2 The Nullspace of A
date: 2019-09-17 08:50:24.000000000 +9:00
---

### The Nullspace of A
> The nullspace $N(A)$ consists of all solutions to $Ax=0$. These vectors $x$ are in $R^n$.

The solution vectors $x$ have $n$ components. They are vectors in $R^n$, so the *nullspace is a subspace of $R^n$*. The $C(A)$ is a subspace of $R^m$.
The $N(A)$ contains all the combinations of the ***special solutions*** to $Ax=0$.

**Example** $x+2y+3z=0$ comes from the 1 by 3 matrix $A$ = $$\begin{bmatrix}1&2&3\\\end{bmatrix}$$. Then $Ax=0$ produces a plane. All vectors on the plane are perpendicular to $(1, 2, 3)$.The plane is the nullspace of $A$. Set two free variables $y$ and $z$ to $0$ and $1$.

$$\begin{bmatrix}1&2&3\\\end{bmatrix}$$ $$\begin{bmatrix}1\\2\\3\\\end{bmatrix}$$ $$=0$$ has two special solutions $s_1$=$$\begin{bmatrix}-2\\1\\0\\\end{bmatrix}$$ and $s_2$=$$\begin{bmatrix}-3\\0\\1\\end{bmatrix}$$.

Those vectors $s_1$ and $s_2$ lie on the plane $x+2y+3z=0$. All vectors on the plane are combinations of $s_1$ and $s_2$.

