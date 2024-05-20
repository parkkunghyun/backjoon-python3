import sys
input = sys.stdin.readline

result = 0
N = int(input())
arr = [[0]*101 for _ in range(101)]

for _ in range(N):
    left, under = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[under + i][left + j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for y, x in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                if arr[i+y][j+x] == 0:
                    result += 1

print(result)
