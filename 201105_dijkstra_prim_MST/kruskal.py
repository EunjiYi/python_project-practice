import heapq

def find_set(x):
    #요소의 부모와 요소가 일치하면, 해당 요소가 집합의 대표자
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

#x와 y가 포함되는 집합의 대표자를 하나로 만들어줌 :
# x와 y가 포함되는 집합을 합침
def union(x,y):
    # x와 y가 이미 같은 집합일 때 : 아무작업 안함
    # x와 y의 대표자가 다르다(집합이 다르면), 각 대표자를 하나로 만들어 줌
    a = find_set(x)
    b = find_set(y)
    if a==b: return
    else:
    #a와 b가 각 집합의 대표자 이기 때문에 둘중 하나의 부모를 상대값으로 바꾸면 된다.
        parent[b] = a
        # if a > b:   #작은 값을 대표로 하고 싶을 때,
        #     parent[a] = b
        # if a > b :  # 큰값을 대표로 하고 싶을 때
        #     parent[b] = a

# 7 11
# 0 5 60
# 0 1 32
# 0 2 31
# 0 6 51
# 1 2 21
# 2 6 25
# 2 4 46
# 3 5 18
# 3 4 34
# 4 6 51
# 4 5 40
def kruskal(queue):
    mst = list()
    while queue:
        weight, v = heapq.heappop(queue)
        if find_set(v[0]) == find_set(v[1]):
            continue
        union(v[0],v[1])
        mst.append((v,weight))

    return mst



V, E = map(int,input().split())
queue = list()
parent = list(range(V))
for i in range(E):
    s,e,w = map(int,input().split())
    # 가중치를 기준으로 정렬,
    # heapq (priority queue) : 기준을 설정해주면, 우선 되는 요소가 먼저 pop
    # 가중치가 작은 애부터 꺼내와서 검사하기
    #heappush(대상queue, 요소) : 요소의 첫번째 값이 기준이 됨
    heapq.heappush(queue,(w,(s,e)))

result = kruskal(queue)
print(result)




