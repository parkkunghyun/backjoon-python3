from turtle import *
color("yellow", "gray")


def draw_circle():
    begin_fill()
    circle(100)
    end_fill()


for i in range(3):
    goto(0, i*20)
    draw_circle()


def draw_circle(x, y, r):
    goto(x, y)
    begin_fill()
    circle(r)
    end_fill()


for i in range(3):
    draw_circle(0, i*20, 100)

draw_circle(300, 0, 100)
draw_circle(-300, 0, 100)


def draw_circle2(x, y, r=100):
    goto(x, y)
    begin_fill()
    circle(r)
    end_fill()
    return (3.14*r**2)


print("원의 면적 = ", draw_circle2(0, 0))
print("원의 면적 = ", draw_circle2(300, 0, 50))
