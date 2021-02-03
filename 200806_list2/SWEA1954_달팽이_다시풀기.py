def check(a, b):
    return 0 <= a < n and 0 <= b < n

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    cnt = n * n
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    d = 0
    num = 1
    while num <= cnt:
        if check(r, c) and not arr[r][c]:
            arr[r][c] = num
            num += 1
        else: #범위에서 벗어나면 원복.
            r = r - dr[d]
            c = c - dc[d]
            d = (d+1) % 4

        r = r + dr[d]
        c = c + dc[d]

    print("#{}".format(tc))
    for row in arr:
        # print(row)
        print(" ".join(map(str,row)))