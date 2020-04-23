import turtle as tt

def square(tortoise, size, center):
    tortoise.penup()
    tortoise.setpos(center[0]-size/2, center[1]-size/2)
    tortoise.pendown()
    for k in range(4):
        tortoise.forward(size)
        tortoise.left(90)
    
    return

wn = tt.Screen()
tito = tt.Turtle()

wn.bgcolor("lightgreen")
tito.color("magenta")
tito.pensize("3")

for k in range(5):
    square(tito, 20+k*20, (0,0))

tito.penup()
tito.setpos(-60,-60)

wn.mainloop()