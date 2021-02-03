import sys
sys.stdin = open('input2.txt')

# 한 도로에서 각 집까지의 최소 거리 중 최대값 찾기
def c(roads):
    INF = float('inf')
    result = [INF] * len(home)
    ans = INF

    for r in roads:
        for h in range(len(home)):
            hr = home[h][0]
            hc = home[h][1]

            tmp2 = INF
            for i in range(len(r)):
                rr = r[i][0]
                cc = r[i][1]
                tmp = abs(hr - rr) + abs(hc - cc)
                if tmp2 > tmp:
                    tmp2 = tmp
            result[h] = tmp2

        mtmp = max(result)
        if ans > mtmp:
            ans = mtmp

    return ans

# 모든 도로 다 그어보기. 가능한 도로 찾기.
# flag가 False면 도로 그을 수 없음.
def f():
    flag = False

    # 가로 road3
    road3 = []
    for i in range(h):
        b = False
        tmp = []
        for j in range(w):
            if matrix[i][j] == 1:
                b = True
                break
            elif matrix[i][j] == 0:
                tmp.append((i, j))
        if b:
            continue
        else:
            road3.append(tmp)
    # print(road3)
    if len(road3) != 0:
        flag = True


    # 세로 road4
    road4 = []
    for j in range(w):
        b = False
        tmp = []
        for i in range(h):
            if matrix[i][j] == 1:
                b = True
                break
            elif matrix[i][j] == 0:
                tmp.append((i, j))
        if b:
            continue
        else:
            road4.append(tmp)
    # print(road4)
    if len(road4) != 0:
        flag = True


    # 대각선 road
    road = []
    for n in range(1, w + h -2):
        b = False
        tmp = []
        for i in range(h):
            for j in range(w):
                if i + j == n and matrix[i][j] == 0:
                    tmp.append((i, j))
                elif i + j == n and matrix[i][j] == 1:
                    b = True
                    break
            if b:
                break
        if b:
            continue
        else:
            road.append(tmp)
    # print(road)
    if len(road) != 0:
        flag = True


    # 반대쪽 대각선 road2
    road2 = []
    for n in range(-(w-2), h-1):
        b = False
        tmp = []
        for i in range(h):
            for j in range(w):
                if i - j == n and matrix[i][j] == 0:
                    tmp.append((i, j))
                elif i - j == n and matrix[i][j] == 1:
                    b = True
                    break
            if b:
                break
        if b:
            continue
        else:
            road2.append(tmp)
    # print(road2)
    if len(road2) != 0:
        flag = True


    roads = road3 + road4 + road + road2
    # print(roads)

    if flag == False:
        return -1
    else:
        return c(roads)


for tc in range(1, int(input())+1):
    w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]

    home = []
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                home.append((i, j))
    # print(home)

    result = f()
    print("#{} {}".format(tc, result))