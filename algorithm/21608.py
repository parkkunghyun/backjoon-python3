import sys
input = sys.stdin.readline

N = int(input())
arr = [[-1]*(N+2)] + [[-1] + [0] * N  + [-1] for _ in range(N)] + [[-1] * (N+2)] 
input_lst = [list(map(int, input().split())) for _ in range(N*N)]
sorted_lst = [[0]* 5] + sorted(input_lst)

# 1 - 전체를 순회하면서 빈자리에 친한친구 순 > 빈자리수 > 좌석행렬
for lst in input_lst:
    mx = empty_mx = -1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] > 0: continue # 즉 빈자리 아니면 패스
            cnt = empty_cnt = 0
            for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
                ni,nj = i + di, j + dj
                if arr[ni][nj] in lst[1:]: # 좋아하는 친구인가
                    cnt+=1
                if arr[ni][nj] == 0:
                    empty_cnt += 1
            if mx < cnt or (mx == cnt and empty_cnt > empty_mx):
                mx, empty_mx = cnt, empty_cnt
                ei,ej = i,j
    #모든 위치 체크 후 최종자리 결정
    arr[ei][ej] = lst[0]
    
# 2 - 배치된 자리에 따른 점수 누적
ans = 0
tbl = [0,1,10,100, 1000]
for i in range(1, N+1):
    for j in range(1, N+1):
        # 4방향
        cnt = 0
        for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
                ni,nj = i + di, j + dj
                if arr[ni][nj] in sorted_lst[arr[i][j]]: # 좋아하는 친구인가
                    cnt+=1
        ans += tbl[cnt]
print(ans)              
"""
-1 -1 -1 -1 -1
-1  0  0  0 -1
-1  0  0  0 -1
-1  0  0  0 -1
-1 -1 -1 -1 -1

비어있는 칸중 인접 제일많은
비어있는게 제일 많은
열과 행 작은 순

이게 처음은 무조건 1,1임
처음은 자기 번호, 그리고 4개는 좋아하는 번호
0 10 100 1000

처음만 저장하고 나머지는 규칙 만들어서 반복이라 이걸 정하면 끝
배열을 하나 만들기 -> visited[()][좋아하는거, 빈칸, 행열] 

전체에서 비어있는곳을 도는데 현재 비어있는데마다 번호 4개를 확인 
1. 번호 4개가 상하좌우에 있는지 확인하기
2. 그 다음 빈칸 몇개인지 확인
3. 그리고 열 행 확인

정해지면 거기는 -1
"""

"""
전체순회
빈자리, 좋아하는수, 빈칸수, => 자리잡기 
empty_cnt를 -1로 해서 처음부터 갱신되게
for i in (1, N+1):
    for j (1, n+1):
    빈자리면 아래 돌기 > 0 - continue
        4방향 cnt, empty_cnt 세기
        if max < cnt or max==cnt and e_max < e_cnt
            ei,ej <-i,j max,e_max갱신

----- 
인원 합 구하기
9번이면 9가 좋아하는 애들 4개가 몇개나 있는지
lookup table사용 -> 일단 정렬하기 

전체 순회
4방향 
    arr[ni][nj] in lookup table 내부에 있으면 됨
    

"""
