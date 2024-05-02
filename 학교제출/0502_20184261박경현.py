l = []
check = 0
for _ in range(5):
    grade = int(input("성적을 입력하시요: "))
    l.append(grade)
print(f'성적 평균= {sum(l)/len(l)}')
print(f'최대점수= {max(l)}')
print(f'최소점수= {min(l)}')
for i in range(len(l)):
    if l[i] >= 80:
        check+=1
print(f'80점 이상= {check}')