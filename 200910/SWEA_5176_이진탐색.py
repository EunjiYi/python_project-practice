# # 이진탐색트리
# 1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
# 이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
# 추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.

def inputtree(node): # node의 부모, 자식의 값을 넣는 함수
    global number
    if node > N:
        return
    inputtree(2 * node) #왼쪽자식 넣기
    tree[node] = number
    number += 1
    inputtree(2 * node + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    number = 1
    inputtree(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
