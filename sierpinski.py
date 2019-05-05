'''
This program uses the turtle module. 
The tutrtle module allows you to draw on a canvas
turtle methods include:
	import turtle # imports turtle
	pen = turtle.Turtle() #creates an instance of turtle
    pen.fd() # will go forwards 
    pen.bk() # will go backwards
    pen.lt(angle) # turns left default 90
    pen.rt(angle) # turns right default 90
    pen.pu() # pen up
    pen.pd() # pen down
    pen.setheading(angle) # sets ts the direction (180 is left)
    pen.speed(n) # sets the speed, (1 - 10)
'''

import turtle  
pen = turtle.Turtle() 
pen.speed(10) # sets the pen draw speed to max
# spen = turtle.Turtle() 
# spen.speed(4) # sets the pen draw speed to max
# position the pen in the bottom corner
pen.setheading(180)
pen.pu()
pen.fd(300)
pen.lt(90)
pen.fd(300)
pen.pd()

def sierpinski(n, width = 30):
    '''draws order n sierpinski's triangle'''    
    if n == 1:
        pen.setheading(180)
        for i in range(3):
            pen.rt(120)
            pen.fd(width)
    else:
        sierpinski(n - 1, width)
        pen.rt(120)
        pen.fd(width * 2 ** (n - 2))
        sierpinski(n - 1, width)
        pen.lt(120)
        pen.fd(width * 2 ** (n - 2))
        sierpinski(n - 1, width)
        pen.fd(width * 2 ** (n - 2))

def draw_triangle(length):
    pen.setheading(180) # set the direction of the pen to left
    for i in range(3): # draw 3 sides
        pen.rt(120) # rotate the pen 120 degrees clockwise
        pen.fd(length) # draw side
	# pen will end up facing left (180)

def sierpinski_order_two(length):
	draw_triangle(length)
	pen.rt(120)
	pen.fd(length)
	draw_triangle(length) 
	pen.lt(120)
	pen.fd(length)
	draw_triangle(length)
	pen.fd(length)

def sierpinski_order_two_recursive(n, length):
	if n == 1:
		draw_triangle(length)
	else:
		sierpinski_order_two_recursive(n - 1, length) # this is just like calling draw_triangle()
		pen.rt(120)
		pen.fd(length)
		sierpinski_order_two_recursive(n -1, length)
		pen.lt(120)
		pen.fd(length)
		sierpinski_order_two_recursive(n - 1, length)
		pen.fd(length)

def sierpinksi_order_three_recursive(n, length):
	if n == 1:
		draw_triangle(length)
	else:
		sierpinksi_order_three_recursive(n - 1, length) # this is just like calling draw_triangle()
		pen.rt(120)
		pen.fd(length * (n - 1))
		sierpinksi_order_three_recursive(n -1, length)
		pen.lt(120)
		pen.fd(length * (n - 1))
		sierpinksi_order_three_recursive(n - 1, length)
		pen.fd(length * (n - 1))

def sierpinski_order_n_recursive(n , length):
	if n == 1:
		draw_triangle(length)
	else:
		sierpinski_order_n_recursive(n - 1, length) # this is just like calling draw_triangle()
		pen.rt(120)
		pen.fd(length * 2 ** (n - 2))
		sierpinski_order_n_recursive(n -1, length)
		pen.lt(120)
		pen.fd(length * 2 ** (n - 2))
		sierpinski_order_n_recursive(n - 1, length)
		pen.fd(length * 2 ** (n - 2))

# sierpinski(5, 37.5)
# eqilateral_triangle(100)
sierpinski_order_n_recursive(4,80)
# pen.fd(1000)
pen.rt(1000)
