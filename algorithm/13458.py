import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
B,C = map(int,input().split())

result = 0
# 나누기를 그이상으로 해주기!
for i in range(N):
    l[i] -= B
    result+=1

for i in range(N):
    if l[i] > 0:
        div = l[i] // C
        mod = l[i] % C
        if mod != 0:
            result += div + 1
        else:
            result += div
print(result)
