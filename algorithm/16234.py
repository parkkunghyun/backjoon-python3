import sys
input = sys.stdin.readline
from collections import deque

def bfs(si,sj): # 시작 i,j를 받음
    q = deque()
    q.append((si,sj)) # q의 초기 데이터 삽입
    v[si][sj] = 1 #방문표시
    alst = [(si,sj)] # 연합에 추가
    sm = arr[si][sj] # 합계
   
    while q:
       ci,cj = q.popleft()
       # 네방향 범위내, 미중복 , 조건L R맞으면
       for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):
           ni,nj = ci+di , cj+dj
           if 0 <= ni < N and 0<= nj <N and v[ni][nj] == 0 and L <= abs(arr[ci][cj] - arr[ni][nj] ) <= R:
               q.append((ni,nj))
               v[ni][nj] = 1
               alst.append((ni,nj))
               sm += arr[ni][nj]
    if len(alst) > 1: #연합인 경우 평균 값 각각 처리
        for ti,tj in alst:
            arr[ti][tj] = sm // len(alst)
        return 1 #연합이있었었음 
    return 0 #연합이 혼자면 즉 이제 계산할게 없으면 끝
    

N,L,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while ans <= 2000:
    v = [[0]* N for _ in range(N)]
    flag = 0
    # 1 - 전체를 순회화면서, 미방문-> bfs로 연결된 연합을 처리
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0: #미방문
                flag = max(flag, bfs(i,j)) # 연합이 있었는지만 리턴
    if flag == 0: # 이동이 없었다
        break #여기서 나감
    ans+=1      
print(ans)
                
                
                

