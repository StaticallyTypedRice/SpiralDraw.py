'''
Miscellaneous functions for SpiralDraw.py
Developed by Richie Zhang for the 2016 IB Math SL Internal Assessment.
The class 'SpiralDrawMisc' was mostly used for testing during development 
but was also used occasionally when writing the IA.

MIT Licensed, Copyright (c) 2016 Richie Zhang
'''

import turtle

class SpiralDrawMisc:
	'''
	Miscellaneous functions for SpiralDraw.py
	Mostly used for testing during initial development
	'''
	def circle(radius=1):
		'''
		Draw a circle without the use of turtle.curcle()

		First moves the pen forward "radius" pixels, and left by 1 degree.
		Repeat 360 times, causing the curve to loop back around into a circle.
		'''
		for a in range(360):
			# Move forward by "radius".
			# "radius" is actually how far to move each time, which *indirectly*
			# controls the actual radius of the circle.
			turtle.forward(radius)

			# Move left by 1 degree
			turtle.left(1)


	def spiral(radius=1, advance=1, loops=3):
		'''
		Draw a straight spiral

		When the pen begins to draw a circle, also move the
		pen left (relative to the canvas) {advance} units during
		each step of the circle drawing process. This creates
		one loop in of the spiral. Simply repeat this action to
		achieve the desired spiral length.
		'''
		for loop_main in range(loops):
			spiral_heading = 0

			for a in range(360):
				# Begin drawing a circle
				turtle.forward(radius)
				turtle.left(1)

				# Save the heading of the circle drawing process
				spiral_heading = turtle.heading()

				# Move the pen right by {advance / 10}
				# Because advancing by 1 pixel is too large
				turtle.setheading(0)
				turtle.forward(advance / 10)

				# Restore the original heading of the pen
				# Allows the circle drawing process to continue
				turtle.setheading(spiral_heading)

