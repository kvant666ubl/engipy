# engipy
Engipy is a tool that allows solving as fast as more any little electrical engineering problem :)


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/start.gif?raw=true)

## Contents
- [Theoretical Background](#theoretical-background)
  * [CLI](#cli)
  * [Pretty Slides](#pretty-slides)
    + [Reliability](#reliability)
- [Installation](#installation)

## Theoretical Background
In this section I prepared some basic summary information. Almost the same content is in CLI, but to learn more - follow the links below.
1. [Briefly](https://www.egr.msu.edu/~bingsen/files_publications/J-13_TPEL_Reliability.pdf)
2. [Another Briefly](https://www.iwavesystems.com/skin/frontend/default/electronicstore/pdf/Reliability_estimation_for_electronic_design.pdf)
3. [Handbook of reliability prediction](https://www.quanterion.com/wp-content/uploads/2015/09/Front-Material-for-PDF-Viewer-EPRD.pdf)
4. [Practical Reliability of Electronic Equipment and Products | Eugene R. Hnatek](http://s1.nonlinear.ir/book/Practical_Reliability_of_Electronic_Equipment_and_Products_0824708326.pdf)

## CLI
After installation dependencies, in the project directory run the ```main.py``` file and then type ```info```:

![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/info.png?raw=true)

--- 


## Pretty Slides
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-0-1.png?raw=true)
---
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-2.png?raw=true)
---
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-3.png?raw=true)
---
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-4.png?raw=true)
---
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-5.png?raw=true)
---
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-6.png?raw=true)
---
![alt text](https://github.com/kvant666ubl/engipy/blob/main/images/pt-7.png?raw=true)
---

## Installation
Install python3 modules for ANSII color formatting for output in terminal using the following commands:
```sh
$ pip3 install colorama
$ pip3 install termcolor
```
Install well-known library for creating static and interactive visualizations in Python and pretty good tables:
```sh
$ pip3 install matplotlib
$ pip3 install prettytable
```

## Example
Here is an example below, describes ```R(t)```, ```MTBF```, ```MTTF```, and ```MTTR``` calculation of 
```sh
$ python3 main.py
```
