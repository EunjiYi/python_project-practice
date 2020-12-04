def bomb(n, k, li): # 구슬의 위치를 정할 때마다 구슬을 발사하는 경우
    global minV
    if n == k: # 구슬을 다 떨어뜨렸으니 남아있는 벽돌갯수세기
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
        for i in range(W): # 중복순열
            cp_org = [[0] * W for _ in range(H)]


for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]

    p = [0] * N # 구슬을 발사할 순서를 지정(컬럼이 정해지면 구슬을 떨어뜨릴 위치가 정해지는 것: 중복순열)

    minV = 0xffffffff

    bomb(0, N, org) # 발사위치 정하기

    print("#{} {}".format(tc, minV))