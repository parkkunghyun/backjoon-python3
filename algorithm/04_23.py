#1
num = int(input("입력값: "))
num -= 20
if num < 0:
    print(f'출력값: 0')
elif num > 255:
    print(f'출력값: 255')
else:
    print(f'출력값: {num}')


# 3

num1 = int(input("첫번째 정수를 입력하시오 : "))
num2 = int(input("두번째 정수를 입력하시오 : "))
num3 = int(input("세번째 정수를 입력하시오 : "))

#4
height = int(input("Height(cm) : "))
weight = int(input("Weight(kg) : "))
bmi = weight / ((height / 100) * (height /100))
print(f'BMI : {bmi:.2f}')

#5
n = int(input("정수를 입력하시오 : "))
for i in range(1, n+2):
    for j in range(1,i):
        print(j, end="")
    print()
    
    
#6 ---- ---  ----   
#  |   |   |    |

width = int(input("게임판의 크기: "))
size = width * 2
for i in range(size):
    if i % 2 == 0:
        for j in range(width):
            print("---", end=" ")
    else: # 1 4 7 10
        print("|  |  |  |", end="")
    print()

#7
num = int(input("정수을 입력하시오 : "))
num = str(num)

for i in range(len(num)):
    if num[i] != num[len(num) -1 - i ]:
        print(f'{num} 꺼꾸로 정수가 아닙니다.')
print(f'{num} 꺼꾸로 정수입니다.')

#8
n = int(input("몇 번째 항까지 구할까요? "))
sum = [0,0,0,0,0,0,0,0,0,0,0]
sum[1] = 1
for i in range(2, n+1):
    sum[i] = sum[i - 1] + sum[i - 2]
for i in range(0, n+1):
    print(sum[i],end=" ")
    
#9
number = int(input("Number : "))
hour = number / 60 /60
number -= int(hour) * 60 * 60
minute = number / 60
number -= int(minute) * 60
second = number
print(f'Hour : {int(hour)}')
print(f'Minute : {int(minute)}')
print(f'Second : {int(second)}')

# 10
sum = 0
while True:
    num = int(input("정수 : "))
    if num == 0:
        break
    sum += num
print(f'합 : {sum}')
