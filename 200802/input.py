#input()
#표준입력을 받아옴: 기본설정 >> 콘솔키보드 입력
#기본입력을 파일에서 읽어오도록 변경해야한다.
# 변경을 하려면 sys패키지를 import

import sys
sys.stdin = open("input.txt", "r") #표준입력 : stdin

for i in range(10):
    a = int(input()) #입력하나에 input.txt 한줄 한줄 #int():숫자형태의 문자열을 숫자로 바꿈
    b = list(map(int, input().split())) #문자열을 읽어오는것 #숫자형태의 문자열이 여러개 -> 즉 숫자배열로 만들어야한다.
# 띄어쓰기 기준으로 분리 .split()
#map: int 함수를 collection의 모든 요소에 적용한다.
#map을 사용하고나면, list가 아니다.! = 즉 인덱스 접근이 안됨.
#그래서 다시 리스트로 만들어야한다. list()

    print(a, "///", b)