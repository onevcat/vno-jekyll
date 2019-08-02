---
layout: post
title: Inverse Matrices
data: 2019-08-02 08:33:24.000000000 +09:00
---
##Something to note
> The matrix A is invertible if there exists a matrix $A^{-1}$

Two-sided inverse: 
$$
A^{-1}\cdot A = I
$$ 
Not all matrices have inverses. There are six note:<br>
1. The inverse exists if and only if elimination produces n pivots (row exchanges are allowed).
2. The matxi A cannot have two different inverses.
3. If A is invertible, the one and only solution to Ax = b is $x = A^{-1}b$.
4. (important) Suppose tehre is a nonzero vector x such that Ax = 0. Then A cannot have an inverse. No matrix can bring o back to x.
> If A is invertible, then Ax = 0 can only have the zero solution when $x = A^{-1}\cdot 0 = 0$.
5. A 2 by 2 matrix is invertible if an only if ad-bc is not zero:
> 2 by 2 Inverse:
$
  \begin{bmatrix}
  a & b\\
  c & d\\
  \end{bmatrix}
^{-1}=\frac{1}{ad-bc}
  \begin{bmatrix}
  d & -b\\
  -c & a\\
  \end{bmatrix}
$
<br>ad-bc is the determinant of A
6. A diagonal matrix has an inverse provided no diagonal entries are zero:
<br>
if $
A = 
  \begin{bmatrix}
  d_1 &      &  \\
     &\ddots&  \\
     &      &d_n\\
  \end{bmatrix}
$
then
$
A^{-1} = 
  \begin{bmatrix}
  \frac{1}{d_1} &      &  \\
     &\ddots&  \\
     &      &\frac{1}{d_n}\\
  \end{bmatrix}
$



