#완전 이진 트리
def findvalue(node): # node의 값을 반환하는 함수
    if node > N + 1:
        return 0

    if tree[node]:
        return tree[node]

    return findvalue(2 * node) + findvalue(2 * node + 1)



T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)
    for _ in range(M):
        leap_node, leap_value = map(int, input().split())
        tree[leap_node] = leap_value

    print(f'#{tc} {findvalue(L)}')
