
def preorder(node): #전위순회를 하면서 node를 루트로 하는 서브트리의 갯수를 반환하는 함수
    global cnt
    if node:
        #print(node, end = " ")
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

def findAncestor(n1, n2): # n1과 n2 노드의 가장 가까운 공통조상을 찾아서 반환하는 함수
    parent = [0] * (V+1)
    color = [0] * (V+1)
    for i in range(E):
        p, c = temp[i*2], temp[i*2+1]
        parent[c] = p #c위에 p가 있다.

    while True:
        color[n1] = True
        if n1 == 0: #root에 도착하면 종료
            break
        n1 = parent[n1]

    while True:
        if color[n2] == True:
            return n2

        # n1과 달리 if n2 == 0할 필요없다. 어차피 가장 최종 공통조상은 root니까.

        color[n2] =  True
        n2 = parent[n2]


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        # 정점 간선 노드2개
        V, E, n1, n2 = map(int, input().split())
        temp = list(map(int, input().split()))

        tree = [[0] * 3 for _ in range(V+1)]

        # 트리 입력
        for i in range(E):
            p, c = temp[i*2], temp[i*2+1]
            if tree[p][0] == 0:
                tree[p][0] = c      #Left
            else:
                tree[p][1] = c      #Right
            tree[c][2] = p          #parent

        # 트리 출력
        # for t in tree: # 출력순서: 왼쪽자식 오른쪽자식 부모.
        #     print(*t)

        # 공통조상 찾기
        ancestor = findAncestor(n1, n2)

        # 서브트리 갯수세기
        cnt = 0
        preorder(ancestor) # 전위순회로 함

        print(f'#{tc} {ancestor} {cnt}')