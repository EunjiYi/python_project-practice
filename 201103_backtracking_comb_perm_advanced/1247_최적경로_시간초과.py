def getsum(arr):
    s = 0
    for i in range(len(arr)-1):
        s += abs(arr[i][0] - arr[i+1][0]) + abs(arr[i][1] - arr[i+1][1])
    s += (abs(arr[0][0] - cx) + abs(arr[0][1]- cy))
    s += (abs(arr[-1][0] - hx) + abs(arr[-1][1]- hy))
    return s

def perm(idx):
    global min_sum
    if idx >= n:
        #print(result)
        sum = getsum(arr) # 순열 다 구하고 거리 구하면 바로 시간초과난다. 순열 구하면서 실시간으로 거리도 계산하자.
        if sum < min_sum:
            min_sum = sum
        return

    for i in range(idx, n):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]




for tc in range(1, int(input())+1):
    n = int(input())
    tmp = list(map(int, input().split()))

    cx, cy = tmp[0], tmp[1]
    hx, hy = tmp[2], tmp[3]

    arr = []
    for i in range(4, len(tmp), 2): #[(70, 40), (30, 10), (10, 5), (90, 70), (50, 20)]
        arr.append((tmp[i], tmp[i+1]))
    #print(arr)


    selected = [0] * n
    result = [0] * n

    min_sum = 10000000000000000000000000000000000000000
    perm(0)
    print("#{} {}".format(tc, min_sum))