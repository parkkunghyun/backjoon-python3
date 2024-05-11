#import sys
#input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    N,M,P = map(int,input().split())
    result = 0
    sum = 1
    for i in range(1,N,2):
        for j in range(1,M,2):
            result+=1
    for i in range(1, result+1):
        sum *= i
        sum = sum % P
    print(f'#{t} {sum}')
"""
k개의 경우의 수를 구하기

- 정사각형일때
0 0 0 0 0
0 1 0 1 0 
0 0 0 0 0 
0 1 0 1 0 
그냥 (1,1) ()
홀수 부분의 가로 +2씩 띄어가며 개수세기

k개의 개수를 구했으면 이걸 놔두는 방식 팩토리얼쓰기

- 직사각형일때도 마찬가지?
0 0 0 0 0 0
0 1 0 1 0 1
0 0 0 0 0 0
0 1 0 1 0 1
"""