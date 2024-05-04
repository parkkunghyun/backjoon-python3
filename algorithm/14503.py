import sys
from collections import deque
input = sys.stdin.readline

#   0 1 2 3
# [-1 0 1 0]
# [0 1 0 -1]
# 북의 왼방향 -> 서 -> 남 -> 동 -> 북 = 3 2 1 0 
# 2 1 0 3
# [1] - 만약 4개중 빈칸이 있으면
#   그 해당 위치로 좌표 옮기고, 방향도 글로 옮기기
# [2] - 4개 중 빈칸이 없다면
#   후진하는데 -> 
#   [3] 후진할때 뒤가 1이면 -> 개수 반환하고 종료
#   [4] 후진할때 뒤가 0이면 -> 뒤로 좌표 옮기고 방향은 그대

# 위 오른 아래 왼
di = [-1,0,1,0]
dj = [0,1,0,-1]

def solve(ci,cj,dr):
    cnt = 0 # 청소 구역 개수세기
    # 이건 [2]를 돌다가 언제 나올지 정함
    while True: #일단 무한 반복으로 후진이 1이 나오기 전까지는 계속 돌아야함
        cnt += 1 #일단 현재칸은 0이어서 들어온거니까 +1하기
        arr[ci][cj] = 2 # 즉 여기는 이미 돌았다는걸 표시!
        flag = 1
        while flag == 1: #즉 현재 위치에서 for문을 도는데 뒤에가 0이면 나오기
            # 현재 방향을 기준으로 왼쪽->하다 내방향까지 돌기
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                # 일단 방향 바꾸기
                ni,nj = ci + di[nd], cj + dj[nd] #즉 현재 위치에서 왼쪽 보기 7,3
                if arr[ni][nj] == 0: #즉 청소구역이다 -> flag탈출
                    ci,cj,dr = ni,nj,nd
                    flag = 0
                    break
            else: #일단 청소는 다 끝남 -> 이제 후진해서 나갈수있는지 없는지 결정
                # 후진한 곳이 1인지 확인 -> 방향따라 후진
                bi,bj = ci-di[dr], cj-dj[dr] # 
                if arr[bi][bj] == 1: # 그러면 종료하기
                    return cnt
                else: # 일단 후진하는데 방향은 고정
                   ci,cj = bi,bj
N,M = map(int,input().split())
si,sj,dr = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = solve(si,sj,dr)
print(result)