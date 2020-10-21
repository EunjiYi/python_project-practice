def in_order(v):
    if v > N:
        return
    in_order(v*2)
    print(tree[v],end="")
    in_order(v*2+1)

T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    for i in range(1,N+1):
        info = input().split()
        tree[i] = info[1]


    print("#{}".format(tc),end=" ")
    in_order(1)
    print()