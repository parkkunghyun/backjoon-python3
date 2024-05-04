"""
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
"""

# 두번째로 큰 값 찾기
list1 = [2,1,5,15,99,3,4]
list1.sort(reverse=True)
print(list1[1])

# 콘테스트 평가
l = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print(f'제거전[{l}]')
l.remove(max(l))
l.remove(min(l))
print(f'제거후[{l}]')

# 리스트 문제 - 1-5번
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

movie_rank.append('배트맨')
print(movie_rank)

movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

movie_rank.remove('럭키')
print(movie_rank)

movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)

