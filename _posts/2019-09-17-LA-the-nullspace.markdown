---
layout: post
title: LA3.2 The Nullspace of A
date: 2019-09-17 08:50:24.000000000 +9:00
---

### The Nullspace of A
> The nullspace $N(A)$ consists of all solutions to $Ax=0$. These vectors $x$ are in $R^n$.

The solution vectors $x$ have $n$ components. They are vectors in $R^n$, so the *nullspace is a subspace of $R^n$*. The $C(A)$ is a subspace of $R^m$.
The $N(A)$ contains all the combinations of the ***special solutions*** to $Ax=0$.

**Example** $x+2y+3z=0$ comes from the 1 by 3 matrix $A=$
$$\begin{bmatrix}1&2&3\\\end{bmatrix}$$
. Then $Ax=0$ produces a plane. All vectors on the plane are perpendicular to $(1, 2, 3)$.The plane is the nullspace of $A$. Set two free variables $y$ and $z$ to $0$ and $1$.

$$\begin{bmatrix}1&2&3\\\end{bmatrix}$$
$$\begin{bmatrix}1\\2\\3\\\end{bmatrix}$$
$$=0$$
has two special solutions $s_1$=
$$\begin{bmatrix}-2\\1\\0\\\end{bmatrix}$$
and $s_2$=
$$\begin{bmatrix}-3\\0\\1\\\end{bmatrix}$$
.

Those vectors $s_1$ and $s_2$ lie on the plane $x+2y+3z=0$. All vectors on the plane are combinations of $s_1$ and $s_2$. 

We notice the last two components are free, because they were assigned $0$ or $1$.

> The two key steps of this section:
1. Reducing A to its **row echelon form $R$**.
2. Finding the **special solutons** to $Ax=0$

#### Pivot Columns and Free Columns

Let's continue to find something to make this system more stable. $C=$
$$\begin{bmatrix}1&2&2&4\\3&8&6&16\\\end{bmatrix}$$
becomes $U=$
$$\begin{bmatrix}1&2&2&4\\0&2&0&4\\\end{bmatrix}$$
. In $U$, columns 1 and 2 are pivot columns and columns 3 and 4 are free columns.

From this view, we can find elimination doesn't change solutions --- This is also the nullspace of $U$. To think about this, I will make a consideration of equations, because the value at the right side is always 0, so the elimination will not affect the solutions of the nullspace.

#### The Reduced Row Echelon Form R

$U(A)$ is a very easy way to get the special solutions to $Us=0$, however, not the easiest way. Now let's see the **Reduced Row Echelon Form** $R$ ($rref(A)$).

How to make a $rref(A)$?

1. ***Produce zeros above the pivots***. Use pivot rows to eliminate upward in $R$.
2. ***Produce ones in the pivots***. Divide the whole pivot row by its pivot.

It's same with $U(A)$, $N(A)$ also does not change the zero vector on the right side, another word, $N(A)=N(U)=N(R)$. This nullspace becomes the easiest to see when we reach the ***reduced row echelon form*** $R=rref(A)$. And through the operations of $N(R)$, we can easy get a very beautiful attribution, ***The pivot columns of R contain*** $I$.

Have an example:


$U=$
$$\begin{bmatrix}1&2&2&4\\0&2&0&4\\\end{bmatrix}$$
becomes $R=$
$$\begin{bmatrix}1&0&2&0\\0&1&0&2\\\end{bmatrix}$$
.

To get the special solutions, we can very easily value the free components (columns) $1$ or $0$ to get $s_1=(-2,0,1,0)$ and $s_2=(0, -2, 0, 1)$. Thanks to the rref operations, we can get the value at the pivot components very easily, just assign it a 'minus' to the free components which were given the $1$ in the nullspace. There is an example to help understand this process:

> Pivot Varibles and Free Variables in the Echelon Matrix

**$p$ means pivot columns** while **$f$ means free columns**

$A=$
$$\begin{bmatrix}p&p&f&p&f\\|&|&|&|&|\\|&|&|&|&|\\|&|&|&|&|\\\end{bmatrix}$$
$R=$
$$\begin{bmatrix}1&0&a&0&c\\0&1&b&0&d\\0&0&0&1&e\\0&0&0&0&0\\\end{bmatrix}$$
$s_1=$
$$\begin{bmatrix}-a\\-b\\1\\0\\0\\\end{bmatrix}$$
$s_2=$
$$\begin{bmatrix}-c\\-d\\0\\-e\\1\\\end{bmatrix}$$
. 

Now let's talk something more interesting. About the ***dimension***.

> See the $N(R)$ below, think about what are the column space and the nullspace for this matrix $R$?

$R=$
$$\begin{bmatrix}1&0&x&x&x&0&x\\0&1&x&x&x&0&x\\0&0&0&0&0&1&x\\0&0&0&0&0&0&0\\\end{bmatrix}$$

The columns of $R$ have four components (rows) so they lie in $R^4$. The column space $C(R)$ consists of all vectors of the form $(b_1, b_2, b_3, 0)$. Counting the pivots leads to an extremely important theorem. Suppose $A$ has more columns than rows. ***With $n>m$ there is at least one free variable***. The system **$Ax=0$ has at least one special solution and this solution is not zero**!

For a *Short Wide* matrix ($n>m$), in its nullspce always has nonzero vectors. And there must be at least $n-m$ free variables, since the number of pivots cannot exceed $m$. Here is the point: **When there is a free variable, it can be set to $1$. Then the equation $Ax=0$ has at least a line of nonzero solutions**.

> About the dimension of nullspace

Nullspace is a subspace. Its dimension is the number of *free variables*.

#### The Rank of a Matrix

Sometimes we need to get the **true size** of a linear system, some rows may be a combination of other rows and becomes zero in the $U$ or the $rref$, and we don''t want to count them. So there comes the ***Rank***, ***the true size of $A$***.

Here is an example:

$A=$
$$\begin{bmatrix}1&1&2&4\\1&2&2&5\\1&3&2&6\\\end{bmatrix}$$
and $R=$
$$\begin{bmatrix}1&0&2&3\\0&1&0&1\\0&0&0&0\\\end{bmatrix}$$

The first two columns of $A$ are $(1, 1, 1)$ and $(2, 2, 2)$, **going in different directions**, which will be pivot columns. What we need to be attention, column 3 and column4 is free column,

> $Column 3 =2(column 1) + 0(column 2)$  ---->   $s_1=(-2, -0, 1, 0)$<br>
  $Column 4 =3(column 1) + 1(column 2)$  ---->   $s_2=(-3, -1, 0, 1)$

Actually, ***Every free column is a combination of earlier pivot columns. It is the special solutions $s$ that tell us those combinations***.

#### Rank One

Matrices of **rank one** have only one pivot. The column space of a rank one matrix is 'one-dimensional'. 

For example,
$A=$
$$\begin{bmatrix}1&3&10\\2&6&20\\3&9&30\\\end{bmatrix}$$
---->
$R=$
$$\begin{bmatrix}1&3&10\\0&0&0\\0&0&0\\\end{bmatrix}$$

Here all columns are on the line through $u= (1, 2, 3)$. The columns of $A$ is $u, 3u, 10u$. Put those numbers into the row $v^T=$
$$\begin{bmatrix}1&3&10\\\end{bmatrix}$$
and you have the special rank one form $A = uv^T$

> $A = column times row = uv^T$<br>
$$\begin{bmatrix}1&3&10\\2&6&20\\3&9&30\\\end{bmatrix}$$
$=$
$$\begin{bmatrix}1\\2\\3\\\end{bmatrix}$$
$$\begin{bmatrix}1&3&10\\\end{bmatrix}$$

With rank one, $Ax=0$ is easy to understand. That equation $u(v^Tx)=0$ leads us to $u^Tx = 0$. All vectors $x$ in the nullspace must be othogonal to $v$ in the row space. This is the geometry when $r=1$: ***row space = line, nullspace = perpendicular plane***.

$A$ and $U$ and $R$ also have ***r independent columns*** (pivot columns).

The ***rank r*** is the '***dimension***' of the column space. It is also the ***dimension of the row space***. There is a very great thing: ##

> The ***Dimension of the nullspace*** = $n-r$ ##

Very important!
