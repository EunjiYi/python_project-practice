def subtree(node): # node를 루트로 하는 서브트리의 갯수를 반환하는 함수
    cnt = 1
    if node:
        for i in range(len(tree[node])):
            cnt += subtree(tree[node][i])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E , N = map(int, input().split())
    temp = list(map(int, input().split()))
    # 트리를 저장할 인접리스트
    tree = [[] for _ in range(E + 2)]
    # 트리 저장
    for i in range(0, E * 2, 2):
        tree[temp[i]].append(temp[i+1])

    print(f'#{tc} {subtree(N)}')

