import sys
from collections import deque
input = sys.stdin.readline

def rot(t, dir):
    t.rotate(dir)

def turnTobni4(num,dir):
    if t4[6] == t3[2]:
        rot(t4, dir)
    else: # 이제는 t2랑 t3만 보기
        rot(t4, dir)
        if t3[6] == t2[2]:
            rot(t3,dir)
        else:
            rot(t3, dir)
            if t2[6] == t1[2]:
                rot(t2,dir)
            else:
                rot(t2, dir)
                rot(t1,dir)

def turnTobni3(num,dir):
    if t3[2] == t4[6]:
       if t3[6] == t2[2]:
           rot(t3,dir)
       else:
           rot(t3, dir)
           if t2[6] == t1[2]:
               rot(t2,dir)
           else:
               rot(t2, dir)
               rot(t1, dir)
    else:
       rot(t4,dir)
       if t3[6] == t2[2]:
           rot(t3,dir)
       else:
           rot(t3, dir)
           if t2[6] == t1[2]:
               rot(t2,dir)
           else:
               rot(t2, dir)
               rot(t1, dir)
def turnTobni2(num,dir):
   if t2[6] == t1[2]:
       if t2[2] == t3[6]:
           rot(t2,dir)
       else:
           rot(t2, dir)
           if t3[2] == t4[6]:
               rot(t3,dir)
           else:
               rot(t3, dir)
               rot(t4, dir)
   else:
       rot(t1,dir)
       if t2[2] == t3[6]:
            rot(t2,dir)
       else:
           rot(t2, dir)
           if t3[2] == t4[6]:
                rot(t3,dir)
           else:
               rot(t3, dir)
               rot(t4,dir)

def turnTobni1(num,dir):
    if t1[2] == t2[6]:
        rot(t1, dir)
    else: # 이제는 t2랑 t3만 보기
        rot(t1, dir)
        if t2[2] == t3[6]:
            rot(t2,dir)
        else:
            rot(t2, dir)
            if t3[2] == t4[6]:
                rot(t3,dir)
            else:
                rot(t3, dir)
                rot(t4,dir)

t1 = deque(map(int, input().rstrip())) #sys.stdin.readline은 \n을 포함함
t2 = deque(map(int, input().rstrip()))
t3 = deque(map(int, input().rstrip()))
t4 = deque(map(int, input().rstrip()))

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    if num == 1:
        turnTobni1(num,dir)
    elif num == 2:
        turnTobni2(num,dir)
    elif num == 3:
        turnTobni3(num,dir)
    else:
        turnTobni4(num,dir)

sum = 0
if t1[0] == 1:
    sum += 1
if t2[0] == 1:
    sum += 2
if t3[0] == 1:
    sum += 4
if t4[0] == 1:
    sum += 8
print(sum)