n = int(input(""))
num = input("")
sum = 0
num = list(num)
for i in range(0, len(num)):
    sum += int(num[i])
print(sum)


# 다른 사람 답
# map(function, iterable) -> 요소 적용할 함수 // 데이터 집합
# 성능 - 내부가 c언어로 구현이라 파이썬 반복문보다 빠름
# 메모리 사용량 - map은 새로운 리스트가 아닌 iterator객체를 반환하므로 메모리 사용량 최소화
# 
"""
num = input()
numbers = list(map(int, input()))
print(sum(numbers))   

def square(x):
    return x**2
numbers = [1,2,3,4,5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))
"""