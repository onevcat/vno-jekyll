---
layout: post
title: 单颗粒3D分类较低要求流程的摸索
date: 2019-11-4 21:56:24.000000000 +09:00
---

流程备忘

```
*** Cryosparc

import
  |
  V
MotionCorrection
  |
  V
CTF Estimation
  |
  V
Picker
  |
  V
2D Class
  |
  V
Down Sample
  |
  V
Ab-initio  # 这里可以在eman2运行，见下
```
```
*** relion           *** eman2

particles -> e2import particle sets
  |                  |
  V                  V
csparc2star  e2initialmodel 
  |           |
  V           |
Class3D <-----|
```
