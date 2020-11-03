# def getsum(arr):
#     s = 0
#     for i in range(len(arr)-1):
#         s += abs(arr[i][0] - arr[i+1][0]) + abs(arr[i][1] - arr[i+1][1])
#     s += (abs(arr[0][0] - cx) + abs(arr[0][1]- cy))
#     s += (abs(arr[-1][0] - hx) + abs(arr[-1][1]- hy))
#     return s

def perm(idx, x, y, sum):
    global min_sum

    if sum >= min_sum: 
        return

    if idx >= n:
        sum += abs(x-hx) + abs(y - hy) # 마지막고객 방문 후 집으로 감.
        if sum < min_sum:
            min_sum = sum
        return

    for i in range(n):
        if selected[i] == 0:
            selected[i] = 1
            result[idx] = arr[i] # 다음 자리 결정
            nx = result[idx][0]
            ny = result[idx][1]
            perm(idx+1, nx, ny, sum+abs(x - nx) + abs(y - ny))
            selected[i] = 0



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
    perm(0, cx, cy, 0) #회사에서 출발한다.
    print("#{} {}".format(tc, min_sum))