books = [234,82,128,50,155]
total = 0
for x in books:
    total += x
print("판매 수량 합계 =", total)
print("판매 수량 평균 =", total/len(books))

contact = ['정약용', '이순신', '김유신', '유관순']
contact.sort()
print(contact)

# apple orange grape
apple = input("과일을 입락헤사요:")
banana = input("과일을 입락헤사요:")
grape = input("과일을 입락헤사요:")

l = []
l.append(apple)
l.append(banana)
l.append(grape)
print(l.pop())
print(l.pop())
print(l.pop())


# 도서목록 관리하기
book = ''
bookList = []
number = 0
print("입력을 종료하려면 [Enter]키를 누르세요.")
print('=' * 30)

while True:
    book = input("도서명 입력 : ")
    if book == '':
        break
    bookList.append(book)
bookList.sort()
print('='*30)
for b in bookList:
    number += 1
    print(f'{number} : {b}')

# 친구관리 프로그램
