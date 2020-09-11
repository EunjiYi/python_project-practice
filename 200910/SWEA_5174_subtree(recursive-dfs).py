for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    # 문제에서 정점번호가 1 ~ E+1라고 했으니까 E+2까지 만든다.
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2): # arr[i] -> arr[i+1]
        p, c = arr[i], arr[i + 1]

        if L[p]: R[p] = c
        else: L[p] = c
        P[c] = p


    def traverse(v):
        if v == 0: return 0
        return traverse(L[v]) + traverse(R[v]) + 1

    print(traverse(N))

