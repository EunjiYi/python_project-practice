import sys
sys.stdin = open('123.txt', 'r')

dic2 = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: int(x/y)
}

def backtrack(idx, ans):
    global maxx, minn
    if idx == n-1: # 사칙연산자는 n-1개
        if maxx <= ans: # 최댓값
            maxx = ans
        if minn >= ans:
            minn = ans # 최솟값
        return

    else:
        for i in range(idx, n-1):
            if (idx == i) or (idx != i and oper[idx] != oper[i]): # 이 조건을 줘서 10초 앞당김 그러나 여전히 시간초과
                oper[idx], oper[i], = oper[i], oper[idx]
                ans_tmp = dic2[oper[idx]](ans, numbers[idx+1]) # 지금 연산자
                backtrack(idx + 1, ans_tmp)
                oper[idx], oper[i] = oper[i], oper[idx]


        # for i in range(idx, n-1):
        #     if oper[i] == '+':
        #         ans = (ans + numbers[idx + 1])
        #     elif oper[i] == '-':
        #         ans = (ans - numbers[idx + 1])
        #     elif oper[i] == '*':
        #         ans = (ans * numbers[idx + 1])
        #     elif oper[i] == '/':
        #         ans = int(ans / numbers[idx + 1])
        #     backtrack(idx+1, ans)

dic = {0: '+', 1: '-', 2: '*', 3: '/'}

for tc in range(1, int(input())+1):

    n = int(input())
    tmp = list(map(int, input().split())) # n-1개
    numbers = list(map(int, input().split())) # n개
    #print(tmp)
    maxx = -100000001
    minn = 100000001


    oper = []
    for i in range(4):
        for j in range(tmp[i]):
            oper.append(dic[i])

    #print(oper)

    backtrack(0, numbers[0])

    print("#{} {}".format(tc, maxx - minn))






