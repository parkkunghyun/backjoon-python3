import sys
input = sys.stdin.readline

# n으로 nxn 2차원 배열만들기
# m만큼 테스트가 들어옴
n,m = map(int,input().split())

l = []
# 누적합 저장할 리스트-> 크기는 n+1로 해서 0을 채울 수 있게 했습니다 
new_list = [ [0 for _ in range(n+1)] for _ in range(n+1)]

test = []
# 여기에 n만큼 입력받기
for _ in range(n):
  mini_list = list(map(int,input().split()))
  l.append(mini_list)

for _ in range(m):
  mini_list = list(map(int,input().split()))
  test.append(mini_list)

# 누적합 계산하기
for i in range(1,n+1):
  for j in range(1, n+1):
    new_list[i][j] = new_list[i-1][j] + new_list[i][j-1] + l[i-1][j-1] - new_list[i-1][j-1]

# 그리고 m만큼 테스트 받고 바로 출력하기
for i in range(len(test)):
  y1,x1,y2,x2 = test[i]
  result = new_list[y2][x2] - new_list[y2][x1 - 1] - new_list[y1 - 1][x2] + new_list[y1-1][x1-1]
  print(result)