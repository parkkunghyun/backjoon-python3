# 실습 8-3
atuple = 10,20,30,40,50
alist=['A','B','C']
a,b,c,d,e = atuple
print(a,b,c,d,e)
x,y,z = alist
print(x,y,z)

# 회원가입 여부 확인하기
members = (('choi',93), ('han',50), ('jung',92), ('kang',68), ('kim',80)
           ('lee',90),('moon',65), ('na',100), ('park',75), ('song',75))

search = input("검색할 아이디 입력 : ")
idList = []
for x in members:
    idList.append(x[0])
if search in idList:
    print("가입한 회원입니다.")
else:
    print("회원이 아닙니다.")
    

# 8-5
memberId = ''
num = 0
for x,y in members:
    if y > num:
        memberId = x
        num = y
print("만족도 점수가 가장 높은 회원은 %s, 점수는 %d입니다.", %(memberId, num))

# 딕셔너리
adic = {'a': 90, 'b':70, 'c':60, 'd':70}
bdic = {}
type(adic)
type(bdic)

adic['b'] = 80
adic
adic['f'] = 100
del adic['f']
adic

