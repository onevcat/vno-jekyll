---
layout: post
title: Vector Spaces and Subspaces
date: 2019-09-03 11:30:00:24.000000000 +09:00
---
Summarized from 'Introduction to Linear algebra' from Gilbert Strang.
### Definition of The Vector Spaces
**Vector space** is a very important concept, which is denoted by $R^1, R^2, R^3 ... R^n$, which consists of a *a whole collection of vectors*. For example, $R^5$ contains all column vectors with five components, the so-called "ive-dimentional space".
> **DEFINITION** The space $R^n$ consists of all column vectors v with n components.

Here are three vector spaces other than $R^n$:
> **M** The vector space of ***all real 2 by 2 matrices*** <br>
> **F** *The vector space of ***all real functions $f(x)$*** <br>
> **Z** The vector sapce that consists only of a ***zero vector***

****PS***:The function space F is infinite-dimensional. A smaller function space is $P$, or $P_n$ containing all polynomials $a_0 + a_1x ... a_nx^n$ of degree n.
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
