import sys
# command + [
input = sys.stdin.readline

dir_y = [0, -1, -1, -1, 0, 1, 1, 1]
dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]

diagnal = [(-1, -1), (1, 1), (-1, 1), (1, -1)]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-2, 1), (N-1, 1), (N-2, 0)]

for _ in range(M):
    d, s = map(int, input().split())
    new_cloud = []  # 여기에 이동한 영역 담기
    for y, x in cloud:
        now_y = (dir_y[d-1] * s + y) % N
        now_x = (dir_x[d-1] * s + x) % N
        new_cloud.append((now_y, now_x))
        arr[now_y][now_x] += 1
    # 여기서 한번 더 new_cloud 보고 대각선 확인하기
    for y, x in new_cloud:
        count = 0
        for dia_y, dia_x in diagnal:
            if 0 <= dia_y + y < N and 0 <= dia_x + x < N and arr[dia_y+y][dia_x+x] != 0:
                count += 1
        arr[y][x] += count
    # 이제 arr전체 돌면서 new_cloud에 안들어있으면서 2이상인애 찾기
    cloud.clear()
    for i in range(N):
        for j in range(N):
            if (i, j) not in new_cloud:
                if arr[i][j] >= 2:
                    arr[i][j] -= 2
                    cloud.append((i, j))
result = 0
for l in arr:
    result += sum(l)
print(result)

"""
한바퀴 도는 건 (x+dx[d-1]*s) % 5
모든 될 수 있는 테트로미노를 구해서 전부 대입해보기
1 - (N,1)(n+1,1)(n+2,1)(n+3,1)
←, ↖, ↑, ↗, →, ↘, ↓, ↙
대각선

일단 구름을 지정


"""
