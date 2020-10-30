import sys
sys.stdin = open('123.txt', 'r')
from itertools import combinations, permutations


dic = { 0: '+', 1: '-', 2: '*', 3: '/' }

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
    #print(oper)

    oper_permu = list(permutations(oper, n-1))
    #print(numbers)
    #print(oper_permu)

    #result = set()
    result = []

    for b in range(len(oper_permu)):
        tmp2 = numbers[0]
        for c in range(n-1):
            if oper_permu[b][c] == '+':
                tmp2 = (tmp2 + numbers[c+1])
            elif oper_permu[b][c] == '-':
                tmp2 = (tmp2 - numbers[c+1])
            elif oper_permu[b][c] == '*':
                tmp2 = (tmp2 * numbers[c+1])
            elif oper_permu[b][c] == '/':
                tmp2 = int(tmp2 / numbers[c+1])
        result.append(tmp2)

    print("#{} {}".format( tc, max(result) - min(result) ))