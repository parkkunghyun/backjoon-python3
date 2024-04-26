x = 0
while x < 10:
    print(x, end=' ')
    x+=1
    
sum = 0
x = 1
while x < 11:
    sum +=x
    x += 1
print(f'합계={sum}')


sum = 1
x = 1
while x < 11:
    sum *=x
    x += 1
print(f'10!은 {sum}입니다.')

x = 1
sum = 0
while x < 101:
    if x % 3 == 0 :
        sum += x
    x += 1
print(f'1부터 100사이의 모든 3의 배수의 합은 {sum}입니다.')


# 예제 1번
list = [1,3,5,7,9]
sum = list[0]
print(f'{list[0]} {sum}')
for i in range(1, len(list)):
    sum += list[i]
    print(f'{list[i]} {sum}')
    

