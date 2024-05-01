# 1번 
num = int(input("정수 : "))
if (num < 100):
    print(num)

# 2번 
num = int(input("정수 : "))
if (num % 2 == 0):
    print("짝수")
    
# 4번 
num = int(input("정수 : "))
if (num < 100):
    print(num * 0.9)
else:
    print(num*1.1)
# 5번 
a = int(input("a : "))
b = int(input("b : "))
if (a+b - b*b >= 0):
    print(a+b - b*b)
else:
    print("음수")
    
# 6번
num = int(input("정수 : "))
if (num % 2 == 0 or num % 3 == 0):
    print("나누어짐")
else:
    print("나누어지지 않음")
    
# 9번
year = int(input("년도 : "))
if ((year % 4 == 0 and year % 100 != 0) 
    or (year % 100 == 0 and year % 400 == 0)):
    print("윤년")
else:
    print("평년")
    
