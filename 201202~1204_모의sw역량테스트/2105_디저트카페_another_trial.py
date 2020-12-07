dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def f(i, j, k, s): # k: 방향 / s: 진행한 칸 수
    global sr
    global sc
    global maxV

    if i == sr and j == sc: # 출발점에 도착한 경우
        if maxV < s:
            maxV = s
    elif i<0 or i>=N or j<0 or j>=N:
        return
    elif cafe[i][j] in dessert: #숫자가 겹치는 경우
        return
    elif k == 2 and maxV > (2 * s):
        return
    else:
        dessert.append(cafe[i][j])
        if k==0 or k==1: # 오른쪽 아래로 또는 왼쪽 아래로 가는 경우
            f(i + dr[k], j + dc[k], k, s+1) # k 방향으로 계속 가거나
            f(i + dr[k+1], j + dc[k+1], k+1, s+1) # k+1 방향으로 전환
        elif k==2:
            if i+j != sr + sc: # 출발점을 향할 때가 아니면 직진
                f(i+dr[2], j+dc[2], k, s+1)
            else:
                f(i+dr[3], j+dc[3], k+1, s+1)
        else: # k==3 직진
            f(i + dr[3], j+ dc[3], k, s+1)
        dessert.remove(cafe[i][j])


for tc in range(1, int(input()) + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for i in range(N)]
    maxV = -1
    dessert = []

    for i in range(N):
        for j in range(1, N-1):
            sr = i
            sc = j
            dessert.append(cafe[i][j])
            f(i+1, j+1, 0, 1)
            dessert.remove(cafe[i][j])
    print("#{} {}".format(tc, maxV))


