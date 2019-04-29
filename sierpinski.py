'''
This program uses the turtle module. 
The tutrtle module allows you to draw on a canvas
turtle methods include:
    fd() # will go forwards
    bk() # will go backwards
    lt(angle = 90) # turns left
    rt(90) # turns right
    pu() # pen up
    pd() # pen down
    setheading() # sets ts the direction (180 is left)
    speed() # sets the speed, (1 - 10)
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

def eqilateral_triangle(l):
    for i in range(3):
        spen.rt(120)
        spen.fd(l)


sierpinski(5, 37.5)
# eqilateral_triangle(100)
pen.rt(100000)
