import sys
input = sys.stdin.readline
# 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어하는데 사용되는 모듈
# stdin은 표준 입력 -> 키보드 입력이 표준 
# 사용자가 키를 하나씩 누르면 데이터가 버퍼에 들어감
# 엔터를 누르면 버퍼 입력 종료로 간주 -> 유니코드 문자열로 변환 -> 변환된 문자열 값 반환 후 종료

# 한번에 읽어서 버퍼에 저장하는 방식 / 하나씩 데이터를 주는 방식 -> 즉 버퍼 사이즈 차이가 많이 날수록 stdin.readline()이 우위에 선다

height, n = map(int, input().split())

# 이건 기본 리스트
myList = []
question = [0 for _ in range(n)]

for i in range(height):
  myList.append(list( map( int,input().split() ) ) )


# 이제부터는 각 데이터
for i in range(n):
  question[i] = list(map(int, input().split()))
# 여기부터 누적합으로 계산하기

cumulativeSum_list = [[0] * (height + 1) for _ in range(height + 1)]
# 양 가로 세로 일단 채우기
cumulativeSum_list[1][1] = myList[0][0]
for i in range(2, height + 1):
  cumulativeSum_list[1][i] += myList[0][i-1] + cumulativeSum_list[1][i-1]
  cumulativeSum_list[i][1] += myList[i-1][0] + cumulativeSum_list[i-1][1]


# 이제는 각 내부를 채우기
for i in range(2, height + 1):
  for j in range(2, height + 1): # (2,2) -> 1,2 2,1
    cumulativeSum_list[i][j] = cumulativeSum_list[i][j-1] + cumulativeSum_list[i-1][j] + myList[i-1][j-1] - cumulativeSum_list[i-1][j-1]


for i in range(len(question)):
  y1,x1,y2,x2 = question[i]
  result = cumulativeSum_list[y2][x2] - cumulativeSum_list[y2][x1-1] - cumulativeSum_list[y1-1][x2] + cumulativeSum_list[y1 -1][x1 - 1]
  print(result)
  
  


"""
22 34

11 34

0 0 0 0 0
0 1 3 6 10
0 3 8 15 24
0 6 15 27 42
0 10 24 42 64

"""