def getSum(node): # node의 조상들의 값을 합을 반환하는 함수
    if node < 1:
        return 0

    if node == 1:
        return tree[1]

    return tree[node] + getSum(node // 2)

def getTree(node): #node부터 시작해서 최소힙을 만족하는 tree[]를 채우는 함수

    if node * 2 > N:
        return

    if tree[node] > tree[node * 2] and tree[node * 2] != 0: #왼쪽자식
        tree[node], tree[node * 2] = tree[node * 2], tree[node]
    elif tree[node] > tree[node * 2 + 1] and tree[node * 2 + 1] != 0: # 오른쪽자식
        tree[node], tree[node * 2 + 1] = tree[node * 2 + 1], tree[node]
    getTree(node + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) #마지막 노드
    tree = [0] * (N + 2)

    for value in map(int, input().split()):
        node 시작은 1
        if not tree[node]:
            tree[node] = value
        else:
            if tree[node] > value:
                if not tree[node * 2] and tree[node *  2] > value:
                    tree[node * 2] = tree[node]

                tree[1] = value

    result = getSum(N//2)
    print(f'#{tc} {result}')