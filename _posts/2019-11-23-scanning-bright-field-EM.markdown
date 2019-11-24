---
layout: post
title: Scanning EM VS Bright Field EM
date: 2019-11-24 13:16:24.000000000 +09:00
tags: cryo-EM
---

First of all, let's introduce the definition of the Scannning EM and the Bright field EM respectively:

> Scanning EM

Take the incoming beam of electrons and focused on very small point, rather that small point back and forth across the image as if you are shining a flashlight on a poster.

> Bright Field EM

Illuminate the whole sample all at once, like lift your flashlight.

When the incident electrons light on the conduction, as seen in the figure,

![figure1](/assets/201911/2019-11-24_13-25-56.png)

> Reflection:

About the reflected electrons, there were two applications:

| .EXMA | ..Hard x-ray                       | ...Hard x-ray with high energy  |
| .     | ..Soft x-ray                       | ...Soft x-ray with lower energy |
| .     | ..Cathodoluminescene visible light | ...                             |

EXMA: measure wave length, get information about what elements are present in your sample (Because different elements will emit x-rays with different characteristics)

| .SEM | ..Back scattered primaries | ...                                                                                             |
| .    | ..Secondaries angle        | ...Electrons interact with the electrons in the sample and cause sample electorns to be emitted |
| .    | ..Positive ions            | ...Electrons interacte with nuleus                                                              |

SEM: Detector counting the number of charged particles coming back out of the sample, when it's iluminated you can build up an image pixel by pixel by counting all of these charged particles as they emrge and correlating that counting with the position on the sample that your're illuminating. Always you can find the detector this formations,

![figure2](/assets/201911/2019-11-24_14-16-43.png)

Get a much better looking image if you coat the surface with some form of metal often platinum.

> About the Speciemn on the conduction:

As electrons are being ejected from the sample they leave unmet positive charges within the sample and because the sample is clamped into a sample holder and that's connected to the rest of the metal of the microscope, electrons will flow in from the mecroscope into the sample slowly to compensate for unmet charges, which is **can be measured**.

> Transmission

| .Primaries STEM (scanning + transmission) | ..Wide-angle elastic   |
| .                                         | ..Inelastic            |

| .Primaries TEM | ..Unscattered          |
| .              | ..Inelastic            |
| .              | ..Narrow-angle elastic |

Bright field mode, for the TEM, not only counting detector bu also an imaging detector like CCD.



