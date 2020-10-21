from heapq import heapify

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    heapify(arr) #최소힙
    # 얘는 루트노드가 0이다.

    # 그래서 마지막 노드는 N - 1
    v = (N - 1)
    print(arr)

    # 루트노드가 0 이므로
    # 본인노드가 i일 때
    # 왼쪽자식 =  2 * i + 1   --->곱하기 2해서 부모찾으면 i + 0.5
    # 오른쪽자식 = 2 * i + 2  --->곱하기 2해서 부모찾으면 i + 1
    # 즉, 그러니까 부모노드는,
    # 부모 =  (i -1) // 2