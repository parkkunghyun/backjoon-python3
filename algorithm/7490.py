from collections import product, permutations, combinations

import sys
input = sys.stdin.readline


def solve(n):
    if


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [x for x in range(1, n+1)]


"""
1-N
+ - 그리고 숫자 이어붙이기? 를 넣어서 0이 되게 만들기
순서 상관안하고 조합 상관안하는형태로

product -> 순서 중복 상관안함
permutations -> 서로 다른 n개중 r개를 고르는거 - 순열 
combinations -> 중복 신경쓰고 순서 신경씀 즉 뒤집어서 앞뒤같으면 같은거 - 조합


마지막 수까지 돌면 끝 -> 그리고 계산해서 맞으면 출력 아니면 패스
만들 수 있는 문장을 일단 계속 저장하다가
이거에 대한 결과가 0이면 출력

"""
