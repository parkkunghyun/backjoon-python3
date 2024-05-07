# 평균 최대 최소 구하기
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

# 피이썬 실습 예제 1 - 스택
fruit_box = []
for _ in range(3):
    fruit = input("과일을 입력하세요:")
    fruit_box.append(fruit)
print(fruit_box.pop()) # 그냥 pop으로 작성시 해당 주소가 나오게 됩니다
print(fruit_box.pop())
print(fruit_box.pop())

# 파이썬 실습 예제 2 - 친구 관리 프로그램
friend_lst = []
while True:
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    option = int(input("메뉴를 선택하시오: "))
    if option == 1:
        print(friend_lst)
    elif option == 2:
        name = input("이름을 입력하시오: ")
        friend_lst.append(name)
    elif option == 3:
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        friend_lst.remove(del_name)
    elif option == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오: ")
        new_name = input("새로운 이름을 입력하시오: ")
        for i in range(len(friend_lst)):
            if friend_lst[i] == old_name:
                friend_lst[i] = new_name
                break
    else:
        break
        