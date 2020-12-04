# case2: 구슬을 떨어뜨릴 위치를 다 정하고 나서 구슬을 발사하는 경우
from _collections import deque

# column c에 구슬을 떨어뜨렸을 때 실제 벽돌을 깨는 함수
def crack(c, bak):  # c: 구슬을 떨어뜨리는 column / bak: 벽돌

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


# 벽돌깨고 남은 벽돌수를 리턴하는 함수
def shoot():
    # step1 벽돌 복사본 만들기
    cp_org = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            cp_org[i][j] = org[i][j]

    for i in range(N):
        # p[i] column에 구슬을 떨어뜨렸을 때 실제 벽돌을 깨는 함수
        crack(p[i], cp_org) # 벽돌제거

        # step2 남은 벽돌 아래로 떨어뜨리기
        # 구슬을 한 번 떨어뜨릴 때마다 벽돌 내려줘야한다. 즉 step2 for 문이 위의 for문 안에 있어야함!
        for k in range(W):
            tmp = []
            for i in range(H-1, -1, -1): #제일 밑에서부터
                if cp_org[i][k] != 0: # 남은 벽돌을 제일 바닥부터 순서대로 모으기
                    tmp.append(cp_org[i][k])
                    cp_org[i][k] = 0 # tmp에 담고 나면 cp_org을 0으로 초기화해준다.
            # tmp에 저장된 것을 cp_org에 복사.
            for i in range(0, len(tmp)):
                cp_org[H-1-i][k] = tmp[i]

    # step3 남은 벽돌갯수세기
    count = 0
    for i in range(H):
        for j in range(W):
            if cp_org[i][j] != 0: #벽돌이 남아있으면
                count += 1 #남은 갯수 카운트
    return count


# 구슬을 떨어뜨릴 위치를 다 정하고 나서 구슬을 발사하는 경우
def bomb(n):
    global minV
    if n == N: # 구슬을 떨어뜨릴 위치를 다 정했으니, 실제로 떨어뜨리자.
        cnt = shoot() # 벽돌깨고 남은 벽돌수를 리턴하는 함수
        # 벽돌갯수의 최솟값 갱신
        if minV > cnt:
            minV = cnt
    # 백트래킹: 경우에 따라는 이 한 줄로 시간초과가 결정된다.
    elif minV == 0: # 끝까지 중복순열 다 돌기전에 이미 벽돌갯수 0이면 더 돌 필요없다.
        return

    else:
        for col in range(W): # 중복순열
            p[n] = col
            bomb(n + 1)


for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]

    p = [0] * N # 구슬을 발사할 순서를 지정(컬럼이 정해지면 구슬을 떨어뜨릴 위치가 정해지는 것: 중복순열)

    minV = 0xffffffff

    bomb(0) # 발사위치 정하기

    print("#{} {}".format(tc, minV))