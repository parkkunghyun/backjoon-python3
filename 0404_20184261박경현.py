# 3
num1 = int(input("첫 번째 정수 입력 : "))
num2 = int(input("두 번째 정수 입력 : "))
num3 = int(input("세 번째 정수 입력 : "))

if num1 > num2 and num1 > num3:
    print(f'가장 작은 수 = {num1}')
elif num2 > num1 and num2 > num3:
    print(f'가장 작은 수 = {num2}')
elif num3 > num1 and num3 > num2:
    print(f'가장 작은 수 = {num3}')
    
# 4번
coffee = int(input("메뉴선택(1:진한커피 2:연한커피) : "))
if coffee == 1:
    print("진한커피를 내립니다.")
    print("잠시 기다리세요...")
    print("컵을 꺼내세요.")
else:
    print("연한커피를 내립니다.")
    print("잠시 기다리세요...")
    print("컵을 꺼내세요.")
    
# 5
shape = int(input("도형 선택 (1:사각형, 2:삼각형, 3:원) : "))
if shape == 1:
    width = int(input("가로 입력 : "))
    height = int(input("세로 입력 : "))
    print(f'도형의 넓이 = {width * height}')
elif shape == 2:
    width = int(input("밑변 입력 : "))
    height = int(input("높이 입력 : "))
    print(f'도형의 넓이 = {width * height / 2}')
elif shape == 3:
    radius = int(input("반지름 입력 : "))
    print(f'도형의 넓이 = {radius * radius * 3.14}')
else:
    print("잘못된 입력입니다.")

