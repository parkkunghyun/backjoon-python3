import sys
from collections import deque
input = sys.stdin.readline

# 북 동 남 서
dir = {0: (-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

#입력받기
N,M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 기본 설정
arr[r][c] = 2
result = 1
que = deque([(r,c)])
while que:
    flag = False # 4방향 전부 확인용
    y,x = que.popleft()
    for i in ((d+3)%4, (d+2)%4, (d+1)%4, d%4):
        ny,nx = dir[i]
        if 0<= ny+y <N and 0<=nx+x <M and arr[ny+y][nx+x] == 0:
                # 즉 반시계로 돌면서 빈칸 확인 되면 일로 가기
                y,x = ny+y, nx+x
                que.append((y,x))
                result+=1
                arr[y][x] = 2
                d = i
                flag = True
                break
    if not flag: # 즉 4방향 확인했는데 0이 없으면
        # 후진 하는 곳이 벽이면 종료 / 아니면 후진
        ny,nx = dir[d]
        if 0 <= abs(ny-y) <N and 0<= abs(nx-x) <M and arr[abs(ny-y)][abs(nx-x)] != 1:
            que.append((abs(ny-y), abs(nx-x)))
            flag = False # 다시 돌리기
        else:
            break
print(result)
"""
0123
북동남서
(-1,0) (0,1) (1,0) (0,-1)
동서남북

"""