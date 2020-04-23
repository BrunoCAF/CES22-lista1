import turtle as tt
from math import sin, cos, pi

def draw_poly(tortoise, n, size):
    tortoise.penup()
    (x, y) = -size*1/2, -size*sin(2*pi/n)/(2*(1-cos(2*pi/n)))
    tortoise.setpos(x, y)
    tortoise.pendown()
    for k in range(n):
        tortoise.forward(size)
        tortoise.left(360/n)
    
    return

wn = tt.Screen()
tito = tt.Turtle()

wn.bgcolor("lightgreen")
tito.color("magenta")
tito.pensize("3")

draw_poly(tito, 8, 50)

wn.mainloop()