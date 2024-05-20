
def print19(s, e):
    for i in range(s, e+1):
        print(i, end="")
    print()


print19()


def fadd(n, m):
    s = n+m
    print(n, "+", m, "=", s)


a = 3
b = 4
fadd(3, 4)


def gugudan(n):
    for i in range(1, 10):
        print(f'{n} * {i} = {n*i}')


d = int(input("단 : "))
gugudan(d)

s = int(input("시작값 : "))
e = int(input("끝값 : "))
if s < e:
    print19(s, e)
else:
    print("시작값이 끝값보다 작아야합니다")
