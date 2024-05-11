import sys
from collections import deque

input = sys.stdin.readline
result = 0
def bfs(v):
    global result
    visited[v] = True
    que = deque([v])
    while que:
        computer = que.popleft()
        for node in graph[computer]:
            if not visited[node]:
                que.append(node)
                result+=1
                visited[node] = True

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    start,end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for g in graph:
    g.sort()
bfs(1)
print(result)


"""
1번이 감염
개수만 세면 되서 bfs를 사용
"""