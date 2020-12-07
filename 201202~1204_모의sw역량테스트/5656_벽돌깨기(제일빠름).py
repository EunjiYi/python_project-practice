# case1: 구슬의 위치를 정할 때마다 구슬을 발사하는 경우

from _collections import deque
# 구슬이 떨어졌을 때 실제로 벽돌을 깨는 함수.
def crack(c, bak): # c: 구슬을 떨어뜨리는 column / bak: 벽돌

    r = 0
    while(r<H and bak[r][c] == 0): #맨 위 벽돌 찾기
        r += 1
    if r == H: # 구슬을 떨어뜨린 col에 모든 벽돌이 이미 깨져있을 경우
        return

    queue = deque([(r, c)])

    while queue:
        cr, cc = queue.popleft()
        power = bak[cr][cc] # 구슬이 딱 떨어진 위치의 파워 저장.
        bak[cr][cc] = 0 # 저장했으니 없애주기

        for p in range(1, power):
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = cr + (p * dr) # 여기 p * dr이다. 조심!
                nc = cc + (p * dc)
                if 0 <= nr < H and 0 <= nc < W:
                    queue.append((nr, nc))

    # 남은 벽돌 아래로 떨어뜨리기
    for k in range(W):
        tmp = []
        for i in range(H-1, -1, -1): #제일 밑에서부터
            if bak[i][k] != 0: # 남은 벽돌을 제일 바닥부터 순서대로 모으기
                tmp.append(bak[i][k])
                bak[i][k] = 0 # tmp에 담고 나면 bak을 0으로 초기화해준다.
        # tmp에 저장된 것을 bak에 복사.
        for i in range(0, len(tmp)):
            bak[H-1-i][k] = tmp[i]


# 구슬의 위치를 정할 때마다 구슬을 발사하는 경우
def bomb(n, li):
    global minV
    if n == N: # 구슬을 다 떨어뜨렸으니 남아있는 벽돌갯수세기
        cnt = 0
        for i in range(H):
            for j in range(W):
                if li[i][j] != 0:
                    cnt += 1
        # 벽돌갯수의 최솟값 갱신
        if minV > cnt:
            minV = cnt

    # 백트래킹: 경우에 따라는 이 한 줄로 시간초과가 결정된다.
    elif minV == 0: # 끝까지 중복순열 다 돌기전에 이미 벽돌갯수 0이면 더 돌 필요없다.
        return
    else:
        for col in range(W): # 중복순열
            # 구슬 쏘고 나서 변화 일어나는 것을 이곳에 저장.
            cp_li = [[0] * W for _ in range(H)]
            for p in range(H):
                for q in range(W):
                    cp_li[p][q] = li[p][q]

            # col에 구슬을 쏜다.
            crack(col, cp_li)

            # 반복
            bomb(n + 1, cp_li)


for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]

    minV = 0xffffffff

    bomb(0, org) # 발사위치 정하기

    print("#{} {}".format(tc, minV))