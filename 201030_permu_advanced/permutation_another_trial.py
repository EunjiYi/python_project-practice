def perm(idx, k, n):
    if idx == k:
        print(p)
    else:
        for i in range(n):
            if selected[i] == 0: #arr[i]가 사용전일 때
                selected[i] = 1
                p[idx] = arr[i]
                perm(idx+1, k, n)
                selected[i] = 0


arr = [1,2,3,4,5]
p = [0] * 3 # k == 3
selected = [0] * 5 # n == 5
perm(0, 3, 5)