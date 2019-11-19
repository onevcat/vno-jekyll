---
layout: post
title: First Glimpse on Fourier Shell Correlation - FSC Behaviour Within A Shell
date: 2019-10-16 21:18:24.000000000 +09:00
tags: cryo-EM
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

Which will give this equation ( ***I didn't get it here clearly, hope people can tell me why?*** )

Eq. (5)

$$
\overline{N_{1} N_{2}}\left(r_{i}\right)=\frac{1}{n\left(r_{i}\right)} \cdot \sum_{r \in r_{i}} N_{1}(r) \cdot N_{2}(r) \approx \frac{1}{\sqrt{n\left(r_{i}\right)}} \cdot \overline{N^{2}}\left(r_{i}\right)
$$

This is called the cross-term, which might ( I think ) reflect the relationship between the situation of two different components respectively cross interacted and the situation of the mixed components work together to show, maybe the real situation.

The explanation of the cross-term is discussed in (Saxton and Baumeister, 1982).

From the Eq. (5), we can get the cross-term estimation of signal and noise:

Eq. (6)

$$
\overline{S N}\left(r_{i}\right)=\frac{1}{n\left(r_{i}\right)} \cdot \sum_{r \in r_{i}} S(r) \cdot N_{1}(r) \approx \frac{1}{\sqrt{n\left(r_{i}\right)}} \cdot \bar{S}\left(r_{i}\right) \cdot \bar{N}\left(r_{i}\right)
$$

Here, $SN$ was once thought to be $zero$, because it's wrongly thought to be that the signal is not correlated to the noise.

We substitute (6), (5) into (2), and get,

Eq. (7)

$$
\begin{aligned} \mathrm{FSC}_{\mathrm{u}}\left(r_{i}\right) \approx & n\left(r_{i}\right) \cdot \overline{S^{2}}\left(r_{i}\right)+2 \sqrt{n\left(r_{i}\right)} \cdot \bar{N}\left(r_{i}\right) \cdot \bar{S}\left(r_{i}\right) \\ &+\sqrt{n\left(r_{i}\right)} \cdot \overline{N^{2}}\left(r_{i}\right) \end{aligned}
$$

Which I called it the mixed data. Without Signal and Noise cross-term.

To obtain the expected behaviour of the normalised FSC, we must also look at the behaviour of the FSC norm.

Eq. (8)

$$
\mathrm{FSC}_{n}\left(r_{i}\right)=\sqrt{\left(\sum_{r \in r_{r}} S^{2}(r)+\sum_{r \in r_{r}} 2 \cdot S(r) \cdot N_{1}(r)+\sum_{r \in \epsilon_{r}} N_{1}^{2}(r)\right) \cdot\left(\sum_{r \in r_{r}} S^{2}(r)+\sum_{r \in r_{r}} 2 \cdot S(r) \cdot N_{2}(r)+\sum_{r \in r_{r}} N_{2}^{2}(r)\right)}
$$

Which can also processed from substitution (6,5 to eq. 2)

Eq. (9)

$$
\begin{aligned} \mathrm{FSC}_{n}\left(r_{i}\right) \approx & \sum_{r \in r_{r}} S^{2}(r)+\sum_{r \in r_{r}} 2 \cdot S(r) \cdot N(r)+\sum_{r \in r_{r}} N^{2}(r) \\ \approx & n\left(r_{i}\right) \cdot \overline{S^{2}}\left(r_{i}\right)+2 \sqrt{n\left(r_{i}\right)} \cdot \bar{N}\left(r_{i}\right) \cdot \bar{S}\left(r_{i}\right) \\ &+n\left(r_{i}\right) \cdot \overline{N^{2}}\left(r_{i}\right) \end{aligned}
$$

In this way, finally we get the FSC:

Eq. (10)

$$
\begin{aligned} \operatorname{FSC}\left(r_{i}\right) &=\frac{\mathrm{FSC}_{\mathrm{u}}\left(r_{i}\right)}{\mathrm{FSC}_{n}\left(r_{i}\right)} \\ & \approx \frac{n\left(r_{i}\right) \cdot \bar{S}^{2}\left(r_{i}\right)+2 \sqrt{n\left(r_{i}\right)} \cdot \bar{N}\left(r_{i}\right) \cdot \bar{S}\left(r_{i}\right)+\sqrt{n\left(r_{i}\right)} \cdot \overline{N^{2}}\left(r_{i}\right)}{n\left(r_{i}\right) \cdot \bar{S}^{2}\left(r_{i}\right)+2 \sqrt{n\left(r_{i}\right)} \cdot \bar{N}\left(r_{i}\right) \cdot \bar{S}\left(r_{i}\right)+n\left(r_{i}\right) \cdot \overline{N^{2}}\left(r_{i}\right)} \end{aligned}
$$

For short and better illustration,

Eq. (11)

$$
\mathrm{FSC}_{12}\left(r_{i}\right)=\frac{\sum_{r \in r_{i}} F_{1}(r) \cdot F_{2}(r)^{*}}{\sqrt{\sum_{r \in r_{i}} F_{1}^{2}(r) \cdot \sum_{r \in r_{i}} F_{2}^{2}(r)}}
$$

Where $F(r)$ is the complex "structure factor" at position in Fourier space, and "$*$" denotes complex conjugation.

Here, actually, I only get some information from a very blur aspect. And next, I will learn something more about ***cross correlation***.

### Reference

1.	van Heel M, Schatz M. Fourier shell correlation threshold criteria. Journal of Structural Biology. 2005;151(3):250-262. doi:10.1016/j.jsb.2005.05.009.

2.	SAXTON WO, BAUMEISTER W, microscopy WBJO, 1982. The correlation averaging of a regularly arranged bacterial cell envelope protein. Wiley Online Library.
