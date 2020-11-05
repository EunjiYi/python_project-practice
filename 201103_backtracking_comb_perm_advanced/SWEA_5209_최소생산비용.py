def perm(idx, sum):
    global min_sum
    if sum >= min_sum:
        return

    if idx >= n:
        if sum < min_sum:
            min_sum = sum
        return


    for i in range(n):
        if col[i] == 0:
            col[i] = 1
            perm(idx+1, sum + arr[idx][i])
            col[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 98798797897978978979789879879879879879
    col = [0] * n
    perm(0, 0)
    print("#{} {}".format(tc, min_sum))