N = 5
parent = list(range(N+1))

# 요소 x가 포함되는 집합의 대표자를 반환
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

print(parent)
union(0,1)
union(2,3)
union(4,5)
union(1,5)
print(parent)
print(find_set(0))

std
