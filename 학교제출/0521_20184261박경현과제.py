# 1
import turtle


def print_python():
    print("파이썬")


print_python()

# 2


def welcome():
    for _ in range(3):
        print("환영합니다.")


welcome()

# 3


def welcome2(name):
    print(f'환영합니다. {name} 님')


name = input("이름 : ")
welcome2(name)

# 4


def print_str(string, cnt):
    for _ in range(cnt):
        print(string)


string = input("문자열 : ")
cnt = int(input("횟수 : "))
print_str(string, cnt)


# 5
def welcome3(name, msg="환영합니다."):
    print(f'{msg} {name} 님')


name = input("이름 : ")
welcome3(name)
welcome3(name, "반갑습니다")

# 6


def circle_area(radius):
    print(f'반지름 {radius} 의 넓이 : {radius*radius*3.141592}')


radius = int(input("반지름 : "))
circle_area(radius)

# 7


def pow_xy(x, y):
    print(f'3 * {x}**{y} + 5 = {3* 2**4 + 5}')


pow_xy(2, 4)

# 8


def pzn(n):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        return 1


while True:
    n = int(input("정수 : "))
    if pzn(n) == 0:
        print(0)
        break
    elif pzn(n) == 1:
        print("양수")
    else:
        print("음수")


# 9 -> 가변 vsum(*num)
def vsum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum


print(f'2+3={vsum(2,3)}')
print(f'2+3+4={vsum(2,3,4)}')
print(f'2+3+4+5={vsum(2,3,4,5)}')


# 10 ->
t = turtle.Turtle()
t.speed(0)
t.left(60)


def draw_n(n):
    for _ in range(n):
        t.forward(100)
        t.left(360/n)


for _ in range(12):
    t.left(10)
    draw_n(6)


# 11


def draw_hexa():
    for _ in range(6):
        t.forward(100)
        t.left(360/6)


for _ in range(6):
    draw_hexa()
    t.forward(100)
    t.right(360/6)


# 12
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)


def draw_line():
    t.forward(100)
    t.backward(100)


for x in range(12):
    t.right(30)
    draw_line()
