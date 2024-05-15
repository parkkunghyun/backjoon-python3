import turtle
numbers = set([1, 2, 3, 1, 2, 3])

A = {"apple", "banana", "kiwi"}
B = {"apple", "banana", "kiwi", "grape"}
c = A | B
print(c)

# 거북이 삼각형

# t = turtle.Turtle()
# t.shape("turtle")
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# 거북이 사각형

# t2 = turtle.Turtle()
# t2.shape("turtle")
# t2.forward(100)
# t2.left(90)
# t2.forward(100)
# t2.left(90)
# t2.forward(100)
# t2.left(90)
# t2.forward(100)

# 거북이 다각형 및 원
# t = turtle.Turtle()
# t.shape("turtle")
# for _ in range(6):
#     t.forward(100)
#     t.left(60)
# t.circle(100)

# 거북이 예제3번
# t = turtle.Turtle()
# t.shape("turtle")
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

# 예제 5번
# t = turtle.Turtle()
# t.shape("turtle")
# t.width(10)
# t.forward(100)
# t.left(90)
# t.forward(100)

# 예제 6번
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
# t.forward(100)

# 예제 6번
# t.shape("square")
# t.forward(100)

# 예제 7번
# t = turtle.Turtle()
# t.shape("turtle")
# t.forward(100)
# t.left(150)
# t.up()
# t.forward(100)
# t.right(150)
# t.down()
# t.forward(100)

# 7번 -2

# t.up()
# t.goto(0, 0)
# t.down()
# t.forward(300)
# t.up()
# t.goto(0, 100)
# t.down()
# t.forward(300)

# 8번
# t.width(10)

# t.up()
# t.goto(-150, 0)
# t.color("blue")
# t.down()
# t.circle(100)

# t.up()
# t.goto(40, 0)
# t.color("black")
# t.down()
# t.circle(100)

# t.up()
# t.goto(220, 0)
# t.color("red")
# t.down()
# t.circle(100)

# t.up()
# t.goto(-80, -120)
# t.color("yellow")
# t.down()
# t.circle(100)

# t.up()
# t.goto(130, -120)
# t.color("green")
# t.down()
# t.circle(100)


# 9번
# for count in range(6):
#     t.circle(100)
#     t.left(60)

# 10번
# s = turtle.textinput("박경현", "몇각형을 원하시나요?:")
# n = int(s)
# for i in range(n):
#     t.forward(100)
#     t.left(360/n)

# 11번
# myPen = turtle.Turtle()
# t.speed(1)
# t.color("red")
# for j in range(1, 10):
#     for i in range(1, 6):
#         t.left(144)
#         t.forward(200)
#     t.left(10)

# 12번

# t.up()
# t.goto(0, 200)
# t.down()

t = turtle.Turtle()
t.shape("turtle")
t.up()
t.goto(0, 200)
t.down()

for _ in range(4):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
