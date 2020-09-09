
def inorder(node): #node를 루트로 하는 트리를 중위순회하여 방문노드 순서를 order에 저장하는 함수
    if node:
        inorder(tree[node][1])
        order.append(node)
        inorder(tree[node][2])

T = 10
for tc in range(1, T + 1):
    V = int(input()) #정점
    tree = [[0] * 3 for _ in range(V+1)]
    order = []
    # tree 저장
    for node in range(1, V+1):
        temp = list(input().split())
        tree[node][0] = (int(temp[0]), temp[1])
        if len(temp) >= 3:
            tree[node][1] = int(temp[2])
        if len(temp) >= 4:
            tree[node][2] = int(temp[3])
    #print(tree)

    inorder(1) # 중위순회

    print(f'#{tc}', end = " ")
    for node in order:
        print(tree[node][0][1], end = "")
    print()

