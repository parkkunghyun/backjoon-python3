import sys
input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
people = [0] * (m)
for i in range(m):
    people[i] = int(input())

second = 0
cnt = 0
flag = False

for i in range(100000):
    if flag == True:
        break
    for j in range(m):
        if i % people[j] == 0:
            cnt += 1
            if cnt == (n-s):
                print(j + 1)
                flag = True

"""
n
m 명 1- m
마지막 소보루 집은 사람 번호 구하기

s가 왜 있을까 - 
1 2 3 - 1s
1 - 2s
1 - 3s
1 - 4s
1,2 - 5s

초로 나누는데 이때 0이 되면 그 순서대로 각 빵을 집는것으로 표현
그리고 집은 빵이 m개일때 그걸 집은 인덱스를 출력하기
"""
