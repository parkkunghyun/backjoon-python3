import sys
input = sys.stdin.readline

n,m = map(int,input().split())
l = list(map(int, input().rstrip().split()))

sums = [0 for _ in range(n)]
sums[0] = l[0] % m

for i in range(1,n):
    sums[i] = (sums[i-1] + l[i]) % m
result = 0
# 이제 일단 0의 개수 찾기
for i in range(n):
    if(sums[i] == 0):
        result +=1
print(result)
# 짝 찾기
mList = [0 for _ in range(m)]

for i in range(n):
    mList[sums[i]] +=1

for i in range(m):
    if mList[i] > 1:
        result += (mList[i] * (mList[i]-1)) //2
print(result)

"""
한칸씩 줄여가면서 계산하기 -> N x (n*1)/2
누적합 -> 1 3 6 7 9 -> 3개
시간을 어떻게 줄일 수 있을까?

(a+b)%c == ((a%c) + (b%c)) % c
1 2 3 1 2
1 2 0 1 2
구간배열 s[i] - s[j]는 j+1부터 i까지의 합임

3 2 4 5 1
3 5 9 14 15
0 2 0 2 0

m = 3
s[i] s[j]가 같은쌍을 찾기
(2,2)
s[3] - s[1] = 4+5 = 9
즉 남은 구간합이 떨어진다

12312
13679
10010 - 0인부분은 처음부터 여기까지 더했을때 나눠진다 - 그냥 더하면 됨

이제 나랑 같은애가 몇개인지 찾기
각 개수에서 2개를 뽑는 개수를 마저 더해주면 끝
"""