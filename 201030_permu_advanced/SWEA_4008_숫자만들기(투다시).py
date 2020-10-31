# import sys
# sys.stdin = open('123.txt', 'r')

dic = {
    0: lambda x, y: x+y,
    1: lambda x, y: x-y,
    2: lambda x, y: x*y,
    3: lambda x, y: int(x/y)
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
        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1
                ans_tmp = dic[i](ans, numbers[idx + 1])
                backtrack(idx + 1, ans_tmp)
                oper[i] += 1

for tc in range(1, int(input())+1):

    n = int(input())
    oper = list(map(int, input().split())) # n-1개
    numbers = list(map(int, input().split())) # n개

    maxx = -100000001
    minn = 100000001

    #print(oper)

    backtrack(0, numbers[0])

    print("#{} {}".format(tc, maxx - minn))