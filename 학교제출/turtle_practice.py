# 거북이 연습하기!
import turtle

t = turtle.Turtle()
t.shape("turtle")

# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)


# for _ in range(6):
#     t.forward(100)
#     t.left(360/6)
# t.circle(100)

# t.width(10)
# t.color("blue")
# t.forward(100)
# t.left(90)
# t.forward(100)

# t.speed(1)
# t.forward(100)
# t.up()
# t.goto(0, 200)
# t.down()
# t.forward(100)


# t.width(10)
# t.up()
# t.goto(-150, 0)
# t.color("blue")
# t.down()
# t.circle(100)

# def welcome(name, n="환영합니다."):
#     print(f'{n} {name}님')


# name = input("이름 : ")
# welcome(name)
# welcome(name, "반값습니다.")


# def vsum(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum


# print(f'2+3= {vsum(2,3)}')
# print(f'2+3+4= {vsum(2,3,4)}')
# print(f'2+3+4+5= {vsum(2,3,4,5)}')


# n = int(input("몇각형 : "))


# def draw_n(n):
#     for _ in range(n):
#         t.forward(100)
#         t.left(360/n)


# for _ in range(12):
#     t.left(10)
#     draw_n(8)

# def draw_hexa():
#     for _ in range(6):
#         t.forward(100)
#         t.left(360/6)


# for _ in range(6):
#     draw_hexa()
#     t.forward(100)
#     t.right(360/6)

# def draw_line():
#     t.forward(100)
#     t.backward(100)


# for x in range(12):
#     t.right(30)
#     draw_line()
