'''
Test file for SpiralDraw.py
Developed by Richie Zhang for the 2016 IB Math SL Internal Assessment.

This file can used for trying out the SpiralDraw functions.
This was used to test different SpiralDraw images when writing the IA.

MIT Licensed, Copyright (c) 2016 Richie Zhang
'''

import turtle

from SpiralDraw import SpiralDraw
from Misc import SpiralDrawMisc

# Move the pen down a bit, so the entire image fits onscreen
# Also sets the speed and update rate
turtle.left(90)
turtle.speed("fastest")
turtle.tracer(n=50, delay=0)
turtle.penup()
turtle.backward(200)
turtle.right(90)
turtle.pendown()

# <Test code>



# </Test code>

turtle.update()
turtle.done()
