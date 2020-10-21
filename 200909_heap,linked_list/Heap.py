#최소힙 : 루트가 가장작음
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value

    #만약에 새롭게 정의된 자식이 부모노드보다 작으면,
    #부모노드와 위치를 바꿔줘야 함
    cur = heapcount
    # 이진트리를 배열로 표현할 때 부모노드의 인덱스는 (자식노드 인덱스)//2
    parent = cur//2
    #부모노드가 더 크거나, 부모노드가 root일 때 까지 계속 반복
    # if heap[cur] < heap[parent]:
    #     heap[parent], heap[cur] = heap[cur], heap[parent]
    while parent > 0 and heap[cur] < heap[parent]: #parent > 0  = parent에 값이 있으면
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur//2


def heappop():
    global heapcount
    result = heap[1]    # root를 없애기전 저장(반환해야 하니까)
    # heap의 마지막 인덱스에 있는 노드를 root로 바꿔줌
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1  # 마지막 노드는 없어짐
    # 자식들 중에서 작은 애가 부모가 되어야 함
    parent = 1
    child = parent * 2  # 부모와 위치를 바꿔줄 자식의 인덱스, 초기값 왼쪽으로
    #오른쪽 자식이 있으면, 오른쪽이 작은지 왼쪽이 작은지 비교
    if child + 1 <= heapcount: #마지막노드보다 작으면 오른쪽자식이 무조건 있다는 뜻이니까.
       if heap[child] > heap[child+1]:
           child = child+1 #heap[child]자체를 바꾸는게 아니고 그냥 child라는 변수의 값만 왼쪽,오른쪽자식 중 작은값을 넣는 거다.

    #만약에 자식이 존재하고, 부모노드보다 자식노드가 더 작으면 바꿔줌
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child #부모 바꿈
        child = parent * 2
        if child + 1 <= heapcount: # 새로운 부모에 대해서 위에서와 같이 오른쪽 자식 있는지 확인.
            if heap[child] > heap[child + 1]:
                child = child + 1
    return result


tmp = [7, 2, 5, 3, 4, 6]
N = len(tmp)
heap = [0] * (N + 1) # 넉넉하게 만들자.
heapcount = 0 #현재 마지막 노드가 들어있는 인덱스

# for i in range(N):
#     heappush(tmp[i])
# 아니면
for i in tmp:
    heappush(i)
print(heap)


for i in range(N):
    print(heappop(), end = " ") #2 3 4 5 6 7
print()
print(heap)

