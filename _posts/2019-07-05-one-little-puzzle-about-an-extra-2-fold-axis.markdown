---
layout: post
title: One Little Puzzle About An Extra Two-fold Axis
date: 2019-07-05 21:30:24.000000000 +09:00
---
## The Puzzle

I have resolved a strucutre with space group of P21, with cell angles: 90.0 99.50 90.00.
![The resolved structure packaged in a unit cell](../assets/20190705/image1.jpg)
The cell content analysis has shown that there are two units in an asym unit.
Actually, this structure is quite a simple one, I have found the correct resolution by molecular replacement after searching for one unit model.  
When I have the self rotation function, however, one thing puzzled me a lot. Why there are two 2-fold peaks?
![The result of SRF,](../assets/20190705/srf.png)

## The Answer

The reason is similar to 'Why there is no P22 space group', a 2-fold screw axis has been interacted with the 2-fold axis of the asym unit.
First step, find the 2-fold screw axis vertical to the screen.
![The 2-fold screw axis](../assets/20190705/image2.jpg)
And then, you can find the generated 2-fold screw axis from the side.
![The generated 2-fold screw axis](../assets/20190705/image3.jpg)
This is why there are two 2-fold peaks.



