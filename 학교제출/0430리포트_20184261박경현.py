l = []
while True:
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print(l)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        l.append(name)
    elif menu == 3:
        name = input("삭제하고 싶은 이름을 입력하시오: ")
        l.remove(name)
    elif menu == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오: ")
        new_name = input("새로운 이름을 입력하시오: ")
        for i in range(len(l)):
            if old_name == l[i]:
                l[i] = new_name
    elif menu == 9:
        break
        
        
        