# if elif else 문

score = int(input("점수: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 70:
    print("D")
else:
    print("F")
    

# 7번 임의의 두개 숫자 입력받고 
# 연산자 입력받아서 각 연산 해서 결과 출력하기

num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))
oper = input("연산자 : ")
if oper == "+":
  print(f'{num1} + {num2} = {num1 + num2}')
elif oper == "-":
    print(f'{num1} - {num2} = {num1 - num2}')
elif oper == "*":
    print(f'{num1} * {num2} = {num1 * num2}')
elif oper == "/":
    print(f'{num1} / {num2} = {num1 / num2}')
    
    
# 8번 문제
ph = int(input("ph : "))
if ph <= 4:
    print("강산성")
elif ph <= 6:
    print("약산성")
elif ph == 7:
    print("중성")
elif ph <= 9:
    print("약염기성")
elif ph <= 14:
    print("강염기성")

# if 심화 문제 예제 - 실습문제1
print("당신이 태이난 연도를 입력하세요")
year = int(input(""))
age = 2020 - year + 1
if 20 <= age and age <= 26:
    print("대학생")
elif 17 <= age and age < 20:
    print("고등학생")
elif 14 <= age and age < 17:
    print("중학생")
elif 8 <= age and age < 14:
    print("초등학생")
else:
    print("학생이 아닙니다.")
    
# 실습문제2: 큰수 짝수 판별하기
print("두 개의 양의 정수를 입력하세요:")
num1 = int(input())
num2 = int(input())

if num1 > num2:
    if num1 % 2 == 0:
        print(f'{num1}이 큰 수이고, 짝수이다.')
    else:
        print(f'{num1}이 큰 수이고, 홀수이다.')
elif num1 < num2:
    if num2 % 2 == 0:
         print(f'{num2}이 큰 수이고, 짝수이다.')
    else:
        print(f'{num2}이 큰 수이고, 홀수이다.')

# 실습문제3: 3개의 정수 중 가장 큰 수 출력하기
print("세 개의 양의 정수를 입력하세요:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print(f'가장 큰 수는 {num1}입니다.')
elif num2 > num3 and num2 > num1:
    print(f'가장 큰 수는 {num2}입니다.')
elif num3 > num2 and num3 > num1:
    print(f'가장 큰 수는 {num3}입니다.')
    
# 실습문제4 큰수와 홀수 출력하기
print("세 개의 양의 정수를 입력하세요:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

sum = num1 + num2 + num3
if sum % 2 == 0:
    if num1 > num2 and num1 > num3:
        print(f'세 수의 합은 짝수이고, {num1}입니다.')
    elif num2 > num3 and num2 > num1:
        print(f'세 수의 합은 짝수이고, {num2}입니다.')
    elif num3 > num2 and num3 > num1:
        print(f'세 수의 합은 짝수이고, {num3}입니다.')
else:
    print(f'세 수의 합은 홀수이고, 그 합은 {sum} 이다.')