import sys
sys.stdin = open('123.txt', 'r')


def backtrack(idx, ans):
    global maxx, minn
    if idx == n-1: # 사칙연산자는 n-1개
        if maxx <= ans: # 최댓값
            maxx = ans
        if minn <= ans:
            minn = ans # 최솟값
        return

    else:
        for i in range(idx, n-1):
            if oper[i] == '+':
                ans = (ans + numbers[idx + 1])
            elif oper[i] == '-':
                ans = (ans - numbers[idx + 1])
            elif oper[i] == '*':
                ans = (ans * numbers[idx + 1])
            elif oper[i] == '/':
                ans = int(ans / numbers[idx + 1])
            backtrack(idx+1, ans)

dic = {0: '+', 1: '-', 2: '*', 3: '/'}

for tc in range(1, int(input())+1):

    n = int(input())
    tmp = list(map(int, input().split())) # n-1개
    numbers = list(map(int, input().split())) # n개

    maxx = -100000001
    minn = 100000001


    oper = []
    for i in range(4):
        for j in range(tmp[i]):
            oper.append(dic[i])

    backtrack(0, numbers[0])
