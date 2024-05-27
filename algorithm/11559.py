from collections import deque
import sys

input = sys.stdin.readline


def bfs(y, x):
    que = deque()
    que.append((y, x))
    visited[y][x] = True
    sum_blocks = []
    sum_blocks.append((y, x))
    while que:
        y, x = que.popleft()
        for sy, sx in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ny, nx = sy+y, sx+x
            if 0 <= ny < 12 and 0 <= nx < 6 and not visited[ny][nx] and arr[ny][nx] == arr[y][x]:
                sum_blocks.append((ny, nx))
                que.append((ny, nx))
                visited[ny][nx] = True
    return sum_blocks


def delete(sum_blocks):
    for y, x in sum_blocks:
        arr[y][x] = '.'


def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[k][i] == '.' and arr[j][i] != '.':
                    arr[k][i] = arr[j][i]
                    arr[j][i] = '.'


arr = [list(input().rstrip()) for _ in range(12)]
cnt = 0

while True:
    pang = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visited[i][j]:
                sum_blocks = bfs(i, j)
                if len(sum_blocks) >= 4:
                    pang = True
                    delete(sum_blocks)
    if pang:
        down()
        cnt += 1
    else:
        break
print(cnt)

"""
아래 바닥이나 다른 뿌요가 나올때까지 아래로 떨어짐
상하좌우 4개 이상 연결되면 바로 사라짐 - bfs
뿌요들이 없어지고 - delete함수
위에 다른 뿌요 있으면 아래로 내리기

동시에 터트리기
"""
