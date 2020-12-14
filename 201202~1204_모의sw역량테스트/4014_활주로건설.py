def check(line): # line에서 활주로 건설이 가능하면 1, 가능하지 않으면 0을 반환하는 함수
    flag = 1 # flag가 1이면 건설가능.
    check = [0] * N # 경사로 설치 된 곳 체크

    for i in range(0, N-1):
        if line[i] == line[i+1]:
            continue

        # 인접한 높이 차이가 2 이상이면
        if abs(line[i] - line[i+1]) >= 2:
            flag = 0
            break

        if line[i] < line[i+1]:
            for k in range(i, i-x, -1):
                # if 0 <= k and check[k] == 0 and line[k] == line[i]:
                #     check[k] = 1
                if k < 0 or check[k] or line[k] != line[i]: #이게 같지 않으면 평평하지 않다는 소리고 그러면 경사로 설치를 못한다.
                    flag = 0
                    break
            # break가 한 번도 안걸렸으면,
            else:
                for k in range(i, i - x, -1):
                    check[k] = 1


        if line[i] > line[i+1]:
            for k in range(i+1, i+x+1):
                # if k < N and check[k] == 0 and line[k] == line[i]: # 이렇게 하면 3(i) 2(i+1) 1(i+2)이고 x =2일 때, 안되는 건데 2(i+1)에 check[k] = 1을 해버린다. 즉, 구간 x에 대해서 다 검사하고 check[k]를 해야하기 때문에 else문에 적는다.
                #     check[k] = 1
                if k >= N or check[k] or line[k] != line[i+1]:
                    flag = 0
                    break
            # break가 한 번도 안걸렸으면,
            else:
                for k in range(i + 1, i + x + 1):
                    check[k] = 1

    if flag:
        return 1
    else:
        return 0


for tc in range(1, int(input())+1):
    N, x = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 가로 확인
    for hor in matrix:
        # print(hor)
        ans += check(hor)

    # 세로 확인
    for i in range(N):
        val = list(list(zip(*matrix))[i])
        # print(val)
        ans += check(val)

    print("#{} {}".format(tc, ans))
