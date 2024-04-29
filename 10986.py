for x in range(5):
    print("환영합니다")
    
for x in range(1,20,2):
    print(x)

for x in range(100,0,-10):
    print(x)

sum = 0
for x in range(10):
    sum += x
print(sum)


num = int(input("어디까지 계산할까요: "))
sum = 0
for n in range(1,num):
    sum += n
print(f'1부터 {num}까지의 정수의 합= {sum}')


num = int(input("정수를 입력하시오: "))
sum = 1.0
for i in range(1,num+1):
    sum *= i
print(f'{num}!은 {sum}이다.')

for faci in range(0,110,10):
    print(f'{faci} -> {((faci - 32) * 5/ 9):.2f}')
