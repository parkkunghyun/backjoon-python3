import sys
input = sys.stdin.readline

dir = [(-1,0), (0,1), (1,0), (0,-1)]
N = int(input())

arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    y,x = map(int,input().split())
    arr[y][x] = 1
L = int(input())
dic = {}
for _ in range(L):
    x,c = input().split()
    dic[x] =c
# 초를 계산
result = 1
y,x= 0,0
arr[y][x] = 2 # 현재 위치
dirCheck = 1 # 현재 방향

while True:
    ny,nx = dir[dirCheck]
    print("==>", dirCheck)
    if 0<=y+ny<N and 0<=x+nx<N and arr[y + ny][x+nx] != 2: # 일단 벽이 아니고 현재 위치가 2가 아니라면
        result += 1
        # 여기서 정해주기 -> 일단 사과가 있는지 확인
        if arr[y+ny][x+nx] == 1:
             arr[y + ny][x+nx] = 2
        else:
            arr[y + ny][x+nx] = 2
            arr[y][x] = 0
        # 초를 늘렸을때 해당 초가 dic안에 있다면 그거에 맞게 바꿔주
        # result는 int형이다 
        if str(result) in dic.keys():
            side = dic[str(result)] # dic
            if side == 'L':
                dirCheck -= 1
                if dirCheck < 0:
                    dirCheck = 3
            if side == 'D':
                dirCheck += 1
                if dirCheck > 3:
                    dirCheck = 0
        y = y+ny
        x = x+nx
    else:
        break
print(result)

"""
꼬리 위치를 저장하는 변수도 만들어줘야함

0 0 0 0 0 0 0 0 0 0
0 1 1 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
0 0 0 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
"""