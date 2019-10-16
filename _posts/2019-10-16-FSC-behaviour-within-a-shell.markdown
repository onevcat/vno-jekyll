---
layout: post
title: Fourier Shell Correlation 1, FSC Behaviour Within A Shell
date: 2019-10-16 21:18:24.000000000 +09:00
---

Let us first assume that the two Fourier-space 3D volumes to be compared each contain a signal "$S(r)$" with an uncorrelated additive noise component "$N(r)$". And the signal component in bothe volumes can be written as:

Eq. (1)
$$
\begin{array}{l}{F_{1}(r) \approx S(r)+N_{1}(r)} \\ {F_{2}(r) \approx S(r)+N_{2}(r)}\end{array}
$$

Here, because the noise component $N(r)$ is random, but we need the same signal $S(r)$.

We define $FSC_u$ as no-normalised, cross-correlation over a shell $r_i$ will be:

Eq. (2)
$$
\begin{aligned} \mathrm{FSC}_{\mathrm{u}}\left(r_{i}\right) \approx & \sum_{r \in r_{i}} F_{1}(r) \cdot F_{2}(r) \\ \approx & \sum_{r \in r_{i}} S^{2}(r)+\sum_{r \in r_{i}} S(r) \cdot N_{1}(r) \\ &+\sum_{r \in r_{i}} S(r) \cdot N_{2}(r)+\sum_{r \in r_{i}} N_{1}(r) \cdot N_{2}(r) \end{aligned}
$$

In (1) and (2), $F(r)$ is the ***"structure factor" at position $r$ in Fourier space***. And all Fourier-space voxels "$r$" that are contained in the shell "$r_i$"

The expected statistical behaviour of These 4 terms are important! 

Let us look at the variance of both the signal and noise components separately.

We have the average of the squares for the signal component and noise component, respectively.

Eq. (3)
$$
\overline{S^{2}}\left(r_{i}\right)=\frac{1}{n\left(r_{i}\right)} \cdot \sum_{r \in r_{i}} S^{2}(r)
$$

and

Eq. (4)
$$
\overline{N^{2}}\left(r_{i}\right)=\frac{1}{n\left(r_{i}\right)} \cdot \sum_{r \in r_{i}} N^{2}(r)
$$

Which will give this equation ( ***I didn't get clearly, hope people can tell me why?*** )

Eq. (5)

$$
\overline{N_{1} N_{2}}\left(r_{i}\right)=\frac{1}{n\left(r_{i}\right)} \cdot \sum_{r \in r_{i}} N_{1}(r) \cdot N_{2}(r) \approx \frac{1}{\sqrt{n\left(r_{i}\right)}} \cdot \overline{N^{2}}\left(r_{i}\right)
$$

Here comes a question to me, and I will try to understand it from the Saxton and Baumeister, 1982.


### Reference

1.	van Heel M, Schatz M. Fourier shell correlation threshold criteria. Journal of Structural Biology. 2005;151(3):250-262. doi:10.1016/j.jsb.2005.05.009.


