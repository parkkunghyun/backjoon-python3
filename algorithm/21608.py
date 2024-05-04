import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
school_class = [[0 for _ in range(N)] for _ in range(N)]
f_student = []
for _ in range(N*N):
    f = list(map(int,input().split()))
    f_student.append(f)

# f[0] = 학생 번호 f[1:] -> 이게 좋아하는 학생 번호
for i in range(N*N):
    student = f_student[i][0]
    favorites = f_student[1:]
    if i == 0: #즉 맨 처음 시작할때 - 1,1로 통일 
        school_class[1][1] = student
    else: #이제부터는 계산
        f_check = 0
        e_check = 0
        # 반복하기
        for y in range(N):
            for x in range(N):
                if school_class[y][x] == 0:
                    # 인접 살피기
                    # 일단 인접에 좋아하는애 개수 체크!
                    
                    