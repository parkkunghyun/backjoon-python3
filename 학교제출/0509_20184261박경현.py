# 1 - 슬라이스 기법 활용 문제
a_tuple = (4,5,2,3,8,1,0)
for i in range(len(a_tuple)):
    print(a_tuple[:len(a_tuple) - i])
    
# 딕셔너리
dic_exam = {'홍길동':'과학', '임꺽정':'영어'}
print(dic_exam)

# 8-10 딕셔너리로 학생 평균 점수 구하기
members = {'choi' : 93, 'han': 50, 'jung':92, 'kang': 68, 'kim' :80, 
           'lee':90, 'moon':65, 'na':100, 'park':75, 'song':75}
total = 0
for x in members.values():
    total += x
print(f"회원 점수 평균 = {total/len(members)}")

# 8-11
books = {'여행의 이유':13500, '소년미로': 13000, '회랍인 조르바': 9000, '세 여자':14000, '아픔이 길이 되려면': 18000}
print("검색 가능 도서 :", list(books.keys()))
print('-'*35)

while True:
    bookName = input("도서명 입력(검색 종료는 0) : ")
    if bookName in books:
        print(f'{bookName} = {books[bookName]}, 원')
    elif bookName == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("검색 가능한 도서가 아닙니다")