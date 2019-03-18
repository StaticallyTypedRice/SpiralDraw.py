#SpiralDraw.py

This program aims to simulate the patterns created by the
[Spiral Draw](https://www.amazon.com/Spiral-Draw-Klutz/dp/0545459923) toy by Klutz Press using Python's
Turtle Graphics package. It can also be used to draw other shapes such as spirals and circles,
though these features were more meant for testing during development.

It was written by Richie Zhang for the 2016 IB Math SL Internal Assessment.

This program was created using Microsoft Visual Studio 2015 (Community Edition) and was written
using Python 3.5.0.

This program is licenced under the MIT license. See `LICENSE.txt` for more information.

##Usage:

This program requires [Python](https://www.python.org/) to be installed on your computer.

To render a demo Spiral Draw curve, simply run the file `SpiralDraw.py` (Found in the `SpiralDraw` folder). It will ask for parameters
through the command line. Enter these parameters to customize your curve, or leave blank for the
default graph.

`Test.py` can also be used as a file for trying out the different functions.

##Functions and Classes:

There are two classes in this project: `SpiralDraw` which contains the main function, and `SpiralDralMisc` that contains miscellaneous functions that were mostly used for debugging. The functions are as follows:

* `SpiralDraw.main(radius=1, advance=1, loops=35)` draws the main curve.

* `SpiralDraw.outline(inner_radius=1, outer_radius=4, draw={...}, color={...})` Draws an outline of the SpiralDraw curve (some parameters are too long to be listed here, refer to the code itself, which has more detailed documentation in the comments). 

* `SpiralDrawMisc.circle(radius=1)` draws a circle (this does not use `turtle.circle()`).

* `SpiralDrawMisc.spiral(radius=1, advance=1, loops=3)` draws a spiral.
