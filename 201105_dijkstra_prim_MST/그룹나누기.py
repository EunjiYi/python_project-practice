def find(x):
    if parents[x] == x:
        return x
    p = find(parents[x])
    parents[x] = p
    return p

def union(a, b):
   pa = find(a)
   pb = find(b)
   if pa != pb:
       parents[pb] = pa

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    #print(n, m)
    tmp = list(map(int, input().split()))
    #print(tmp)
    parents = [i for i in range(n+1)]
    #print(parents)

    for i in range(0, m*2, 2):
        union(tmp[i], tmp[i+1])

    result = set()
    for i in parents:
        i_root = find(i)
        result.add(i_root)

    print('#{} {}'.format(tc, len(result)-1)) #0번 빼야되니까 -1
