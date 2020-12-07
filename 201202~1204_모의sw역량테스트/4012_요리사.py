from itertools import combinations

def getS(li_a):
    global A, B
    A, B = 0, 0
    comb_a = list(combinations(li_a, 2))
    #print(comb_a)

    visit = [True] + [False] * (N)
    #print(visit)

    for c, d in comb_a:
        A += s[c-1][d-1]
        A += s[d-1][c-1]
        visit[c] = True
        visit[d] = True

    li_b = []
    for i in range(1, len(visit)):
        if not visit[i]:
            li_b.append(i)
    #print(li_b)

    comb_b = list(combinations(li_b, 2))

    for e, f in comb_b:
        B += s[e-1][f-1]
        B += s[f-1][e-1]

for tc in range(1, int(input())+1):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]

    A, B = 0, 0

    tmp = [i for i in range(1, N+1)]
    comb = list(combinations(tmp, N // 2))
    #print(comb)

    min = 0xfffffffff
    for x in comb:
        getS(x)
        diff = abs(A - B)
        if diff < min:
             min = diff
    print("#{} {}".format(tc, min))