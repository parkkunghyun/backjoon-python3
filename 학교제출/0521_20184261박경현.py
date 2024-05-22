def fadd(n, m):
    s = n + m
    return s


a = 3
b = 4
r = fadd(a, b)
print("반환값 = ", r)


def avg(a, b, c):
    return (a+b+c) / 3


avg(10, 11, 12)


# 함수 연습문제

# 1번
def get_max(a, b):
    if a > b:
        return a
    return b


a, b = map(int, input("두 개의 정수를 입력하시요 : ").split())
print(f'두수중에서 큰수는 {get_max(a,b)}입니다')

# 2번


def asterisk(star):
    for i in range(1, star + 1):
        for j in range(i):
            print("*", end="")
        print()


star = int(input("숫자입력 : "))
asterisk(star)

# 3번


def multiple(num):
    for i in range(1, 10):
        print(f'{num} * {i} = {num * i}')


num = int(input("단입력 : "))
multiple(num)
# 4번


def total_average(s1, s2, s3):
    total, avg = s1+s2+s3, (s1+s2+s3)/3
    print(f'총점 : {total} , 평균 : {avg}')


s1, s2, s3 = map(int, input("세 과목의 점수를 입력하세요 : ").split())
total_average(s1, s2, s3)
