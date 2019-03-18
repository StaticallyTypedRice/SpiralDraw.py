'''
Main file for SpiralDraw.py
Developed by Richie Zhang for the 2016 IB Math SL Internal Assessment.

MIT Licensed, Copyright (c) 2016 Richie Zhang
'''

import turtle

class SpiralDraw:
	'''
	Main class for SpiralDraw.py
	'''
	def main(inner_radius=1, outer_radius=4, loops=35):
		'''
		Main function. Renders the SpiralDraw image.

		Essentially, the SpiralDraw image is created by drawing
		a series of small circles consectively while simultaneously
		moving the pen in the shape of a larger circle.
		'''
		
		inner_heading = 0
		outer_heading = 0
		loop_number = loops + 1
		coordinates = []

		for loop_main in range(loop_number):
			for a in range(360):
				# Record the current coordinates
				# Records every 10 steps (36 points per inner circle)
				# The coordinates are in an array as a series of tuples, 
				# with the first value as the x-coordinate and the 
				# second value as the y-coordinate
				if a % 10 == 0:
					coordinates.append((turtle.xcor(), turtle.ycor()))

				# Begin drawing a circle
				turtle.forward(inner_radius)
				turtle.left(1)

				# Save the heading of the circle drawing process
				inner_heading = turtle.heading()

				# Move the pen around a larger circle
				outer_heading += (1 / loop_number)
				turtle.setheading(outer_heading)
				turtle.forward((outer_radius - inner_radius) / loop_number)
				
				# Restore the original heading of the pen
				# Allows the circle drawing process to continue
				turtle.setheading(inner_heading)

		return coordinates

	def outline(inner_radius=1, outer_radius=4, 
				draw={
					"outer_outline":True, 
					"center_outline":True, 
					"inner_outline":True, 
					"half_center_outline":True
				},
				color={
					"outer_outline":"red", 
					"center_outline":"green", 
					"inner_outline":"blue",
					"half_center_outline":"orange"
				}):
		'''
		Draws the outline of the SpiralDraw image
		Based on SpiralDrawMisc.circle()

		`outer_outline` draws the outline of the outer edge of the 
		SpiralDraw image.

		`center_outline` draws the outline of the circular center that is 
		created by the toridal SpiralDraw image.

		`inner_outline` draws the outline of the circle created by the inner 
		radius, between the outer and center outlines.

		`half_center_outline` draws an additional circle between the outer 
		and center outlines

		The dictonaries `draw` and `color` determine which component(s) to draw
		and what colors to draw them in respectively.
		'''

		if draw["outer_outline"]:
			# Draw the outer outline
			turtle.color(color["outer_outline"])
			for a in range(360):
				turtle.forward(outer_radius)
				turtle.left(1)

		if draw["inner_outline"]:
			# Draw the inner outline
			turtle.color(color["inner_outline"])
			for a in range(360):
				turtle.forward(inner_radius)
				turtle.left(1)

		if draw["center_outline"]:
			# Move the pen in a half circle with radius equivilent 
			# to that of the inner outline so that the pen is at the 
			# correct location
			turtle.penup()
			for a in range(180):
				turtle.forward(inner_radius)
				turtle.left(1)
			turtle.pendown()

			# Draw the center outline
			turtle.color(color["center_outline"])
			for a in range(360):
				turtle.backward(outer_radius - inner_radius * 2)
				turtle.left(1)

			# Return to the starting position
			turtle.penup()
			for a in range(180):
				turtle.forward(inner_radius)
				turtle.left(1)
			turtle.pendown()

		if draw["half_center_outline"]:
			# Move the pen in a half circle with radius equivilent 
			# to that of half the inner outline so that the pen is at 
			# the correct location
			turtle.penup()
			for a in range(180):
				turtle.forward(inner_radius / 2)
				turtle.left(1)
			turtle.pendown()

			# Draw the half-center outline
			turtle.color(color["half_center_outline"])
			for a in range(360):
				turtle.backward(outer_radius - inner_radius)
				turtle.left(1)

			# Return to the starting position
			turtle.penup()
			for a in range(180):
				turtle.forward(inner_radius / 2)
				turtle.left(1)
			turtle.pendown()

if __name__ == "__main__":

	print("SpiralDraw.py - Developed by Richie Zhang\n")

	# User inputs
	inner_radius = input("Outer Radius (leave blank for 1): ")
	outer_radius = input("Inner Radius (leave blank for 4): ")
	loops = input("Loops (leave blank for 35): ")

	if inner_radius:
		inner_radius = float(inner_radius)
	else:
		inner_radius = 1

	if outer_radius:
		outer_radius = float(outer_radius)
	else:
		outer_radius = 4

	if loops:
		loops = int(loops)
	else:
		loops = 35

	# Move the pen down a bit, so the entire image fits onscreen
	# Also sets the speed and update rate
	turtle.left(90)
	turtle.speed("fastest")
	turtle.tracer(n=50, delay=0)
	turtle.penup()
	turtle.backward(200)
	turtle.right(90)
	turtle.pendown()

	# Call the actual SpiralDraw function
	SpiralDraw.main(outer_radius=outer_radius, inner_radius=inner_radius, loops=loops)

	turtle.update()
	turtle.done()