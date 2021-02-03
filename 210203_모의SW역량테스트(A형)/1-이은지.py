import sys
sys.stdin = open('input.txt')

def comb(idx):
    global ans
    if idx >= len(people):
        # print(selected)
        # selected가 0이면 1번비상구로 탈출
        # selected가 1이면 2번비상구로 탈출
        e0 = []
        e1 = []
        tmp = [0] * len(people)
        for p in range(len(people)):
            if selected[p] == 0:
                e0.append((dist[0][p], p))
            elif selected[p] == 1:
                e1.append((dist[1][p], p))

        e0 = sorted(e0, key = lambda x: x[0])
        e1 = sorted(e1, key = lambda x: x[0])

        time0 = 0
        for x in range(len(e0)):
            if x == 0:
                tmp[e0[x][1]] = e0[x][0] + 1
                time0 = e0[x][0] + 1
            else:
                if time0 >= e0[x][0]:
                    tmp[e0[x][1]] = time0 + 1
                    time0 = time0 + 1
                else:
                    tmp[e0[x][1]] = e0[x][0] + 1
                    time0 = e0[x][0] + 1

        time = 0
        for y in range(len(e1)):
            if y == 0:
                tmp[e1[y][1]] = e1[y][0] + 1
                time = e1[y][0] + 1
            else:
                if time >= e1[y][0]:
                    tmp[e1[y][1]] = time + 1
                    time = time + 1
                else:
                    tmp[e1[y][1]] = e1[y][0] + 1
                    time = e1[y][0] + 1

        mtmp = max(tmp)
        if ans > mtmp:
            ans = mtmp
        return

    selected[idx] = 1
    comb(idx+1)
    selected[idx] = 0
    comb(idx+1)

for tc in range(1, int(input())+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    people = []
    emerge = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
               people.append((i, j))
            elif matrix[i][j] == 2:
                emerge.append((i, j))

    INF = float('inf')
    # 각 사람이 비상구까지 걸리는 시간을 저장한 배열.
    dist = [[INF] * len(people) for _ in range(len(emerge))]
    for e in range(len(emerge)):
        for p in range(len(people)):
            dist[e][p] = abs(people[p][0] - emerge[e][0]) + abs(people[p][1] - emerge[e][1])
    # print(dist)

    selected = [0] * len(people)
    ans = INF

    comb(0)

    print("#{} {}".format(tc, ans))