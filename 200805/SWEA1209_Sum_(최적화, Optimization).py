T = 10
N = 100
for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 주어진 2차원 배열 받기
    ans = -float('inf') # 최대합을 저장할 변수, 초기값으로 음의 무한
    ## float('inf') : 부동소수점수(float)에는 특별히 무한을 표현할 수 있는 방법이 있다!
        diagonal_sum = 0    # \ 대각선 합
    de_diagonal_sum = 0 # / 대각선 합
    for i in range(N):
        row_sum = 0 # 행의 합
        col_sum = 0 # 열의 합
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i] # i, j를 바꾸면 행렬이 대칭이 됨
        ans = max(ans, row_sum, col_sum)
        diagonal_sum += arr[i][i]
        de_diagonal_sum += arr[i][N - i - 1] #y랑 x좌표 더하면 N-1이잖아.
    ans = max(ans, diagonal_sum, de_diagonal_sum) # 최대값 비교도 한 번에 하자.
    print('#%d %d' % (tc, ans))