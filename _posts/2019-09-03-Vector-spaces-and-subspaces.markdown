---
layout: post
title: Vector Spaces and Subspaces
date: 2019-09-03 11:30:00:24.000000000 +09:00
tags: 数学
---
Summarized from 'Introduction to Linear algebra' from Gilbert Strang.
## Definition of The Vector Spaces
**Vector space** is a very important concept, which is denoted by $R^1, R^2, R^3 ... R^n$, which consists of a *a whole collection of vectors*. For example, $R^5$ contains all column vectors with five components, the so-called "ive-dimentional space".
> **DEFINITION** The space $R^n$ consists of all column vectors v with n components.

Here are three vector spaces other than $R^n$:
> **M** The vector space of ***all real 2 by 2 matrices*** <br>
> **F** *The vector space of ***all real functions $f(x)$*** <br>
> **Z** The vector sapce that consists only of a ***zero vector***

**PS***:The function space F is infinite-dimensional. A smaller function space is $P$, or $P_n$ containing all polynomials $a_0 + a_1x ... a_nx^n$ of degree n.
## Subspaces
A plane in three-dimensional space is not $R^2$ (even if it looks like $R^2$). The vectors have three components and they belong to $R^3$. The plane is a vector space ***inside $R^3$***.
> **DEFINITION** A subspace of a vector space is a set of vectors (including 0) that satisfies two requirements: ***If $v$ and $w$ are vectors in the subspace and $c$ is any scalar, then<br>***
> ( i ) $v+w$ is in the subspace <br>
> ( ii ) $cv$ is in the subspace

There are two facts,
1. Every subspace contains the zero vector.
2. Lines through the origin are also subspaces.

> ( $L$ ) Any line through (0, 0, 0)<br>
> ( $P$ ) Any plane through (0, 0, 0)<br>
> ( $R^3$ ) The whole space<br>
> ( $Z$ ) The single vector (0, 0, 0)

## The Column Space of A
Start with the columns of A and ***take all their linear combinations. This produces the column space of A, `It is a vector space made up of column vectors`***. $C(A)$ contains not just the $n$ columns of $A$, but all their combinations $Ax$.
> DEFINITION The ***column space*** consists of ***all linear combinations of the columns***. The combinations are all possible vectors $Ax$. They fill the column space $C(A)$.

To solve $Ax = b$ is to express b as a combination of the columns.

> ***The system $Ax = b$ is solvable if and only if b is in the column space of $A$.***

**Important:** Instead of columns in $R^m$, we could start with any set $S$ of vectors in a vector space $V$. To get a subspace $SS$ of $V$, we take all combinations of the vectors in that set:

> $S$ = set of vectors in V (probabley not a subspace)<br>
> $SS$ = all combinations of vectors in $S$<br>
> $SS$ = all $c_1v_1 + ...+ c_Nv_N$ = the subspace of $V$ "spannd" by $S$.

When $S$ is the set of columns, $SS$ is the column space. When there is noly one nonzero vector $v$ in $S$, the subspace $SS$ is the line through $v$. ALways $SS$ is the smallest subspace containing $S$.

> The subspace $SS$ is the "span" of $S$, containing all combinaitons of vectors in $S$.

## Some Problems to Learn
In the definition of a vector space, vector spaces are not necessarily column vectors. In the definition of a vector space, vector addition $x+y$ and scalar multiplicaiton $cx$ must obey the following eight rules:
1. $x+y=y+x$
2. $x+(y+z)=(x+y)+z$
3. There is a unique 'zero vector' such that $x+0=x$ for all $x$
4. For each $x$ there is a unique vector $-x$ such that $x + (-x) = 0$
5. 1 times $x$ equals $x$
6. $(c_1c_2)x=c_1(c_2x)$
7. $c(x+y)=cx + cy$
8. $(c_1+c_2)x = c_1x + c_2x$

For example:<br>
Problems, <br>
1. The possitive numbers with $x + y$ and $cx$ redefined to equal the usual $xy$ and $x^c$ do satisfy the eight rules. Test rule 7 when $c =3, x = 2, y =1$. (Then $x+y=2$ and $cx=8$.) Which number acts as the "zero vector"?
> $c(x+y)\to(xy)^c$, and zero vector is 1
2. $A$ = 
$$
 \begin{bmatrix}
 1 & 0\\
 0 & 0\\
 \end{bmatrix}
$$
and $B$ = 
$$
 \begin{bmatrix}
 0 & 0\\
 0 & -1\\
 \end{bmatrix}
$$
, if a subspace of M does contain $A$ and $B$, must it contain $I$?
> From the DIFINITION of subspace, we can find when $u$ and $w$ are two vectors in the subspace. $u + w$ is also in the subspace is also in the subspace. Because that $A - B$ = 
$$
 \begin{bmatrix}
 1 & 0\\
 0 & 1\\
 \end{bmatrix}
$$
= $I$, this subspace must contain $I$.
3. The subspaces of $R^3$ are planes, lines , $R^3$ itself, or $Z$ containing only (0, 0 ,0).
4. Show that the set of singular matrices in $M$ is not a subspace.
> Import two singular matrices, $A$ =
$$
 \begin{bmatrix}
 1&0\\
 0&0\\
 \end{bmatrix}
$$
, and $B$ = 
$$
 \begin{bmatrix}
 0&0\\
 0&1\\
 \end{bmatrix}
$$
. It's because that the sum of $A,B$ is 
$$
 \begin{bmatrix}
 1&0\\
 0&1\\
 \end{bmatrix}
$$
which is invertible, so the set of singular matrices in $M$ is not a subspace.
5. The columns of $AB$ are combinations of the columns of $A$. This means: The column space of $AB$ is contained in (possibly equal to) the column space of A. Give an example where the column spaces of $A$ and $AB$ are not equal.
> If $B$ is a zero matrix, while $A!=0$, then $AB$ is smaller than $A$ and not equal to each other.
6. If $A$ is any n by n invertible matrix, then its column space is $R^n$, WHY?
> $Ax = b$ is always solved by $x = A^{-1}b$



