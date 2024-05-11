import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    que = deque([v])
    visited[v] = True
    while que:
        s = que.popleft()
        print(s, end=" ")
        for i in arr[s]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
    
def dfs(v):
    visited[v] = True
    print(v, end=" ")
    # 여기는 재귀
    for j in arr[v]:
        if not visited[j]:
            dfs(j)
        
    

N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    start,end = map(int,input().split())
    arr[start].append(end)
    arr[end].append(start)

for i in arr:
    i.sort()

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)

"""
일단 행렬을 만들어서 저장할건지?
 
"""