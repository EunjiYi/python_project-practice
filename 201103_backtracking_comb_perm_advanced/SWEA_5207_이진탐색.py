def binarysearch(s, e, k):
    isboth = -1 # 왼쪽 1 오른쪽 0 맨처음 -1
    while s <= e:
        mid = (s + e) // 2
        if a[mid] == k:
            return True
            #return mid
        elif a[mid] < k: #오른쪽검사해야함.
            #if isboth != 1: # 직전에 왼쪽이 아니었으면, -> 이렇게 하니까 맨 처음에 바로 찾는 것도 걸려버림 ㅜ
            if isboth == 0: # 직전에도 오른쪽이었으면
                return False
            else:
                isboth = 0 # 직전에 왼쪽이었으면 이번엔 오른쪽이라고 표시해준다.
                s = mid + 1
        else: #a[mid] > k: #왼쪽 검사해야함.

            #if isboth != 0: # 직전에 오른쪽이 아니었으면  -> 이렇게 하니까 맨 처음에 바로 찾는 것도 걸려버림 ㅜ
            if isboth == 1: #직전에도 왼쪽이었으면
                return False
            else:
                isboth = 1 #직전에 오른쪽이었으면 이번에는 왼쪽이라고 알려준다.
                e = mid - 1
    return False


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()

    cnt = 0
    for k in b:
        isBoth = binarysearch(0, n-1, k)
        if isBoth:
            cnt += 1

    print("#{} {}".format(tc, cnt))
