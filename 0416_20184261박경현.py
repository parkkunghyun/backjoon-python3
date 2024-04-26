evenSum = 0
oddSum = 0

for i in range(1,101):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
    i += 1
print(f'홀수 합: {oddSum}')
print(f'짝수 합: {evenSum}')

# 실습 2번재 
sum = 0 
for i in range(3, -4, -1):
  print(i, end=" ")
  sum += i
print()
print(sum)

# 1번 문제
s = int(input("단 : "))
for i in range(1, 10):
    print(f'{s} * {i} = {s*i}')
    i += 1
    


# 2번
for _ in range(4):
  for j in range(1, 5):
    print(j, end="")
  print()
  
# 3번
for i in range(1,6):
  for _ in range(i):
    print("*", end="")
  print()
  i += 1
  
# 4번
triangle = int(input("밑변, 높이 : "))
for i in range(1,triangle + 1):
  for _ in range(i):
    print("*", end="")
  print()
  i += 1