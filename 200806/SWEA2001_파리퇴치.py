T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 2차원배열 입력받자.
    mylist = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            sum_value = 0

            for a in range(i, i + M):
                for b in range(j, j + M):
                    sum_value += mylist[a][b]

            if max_value < sum_value:
                max_value = sum_value

    print("#{} {}".format(tc, max_value))