'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v):
    Q = []

    #enQ
    Q.append(v)
    visit[v] = 1
    print(v, end = " ")

    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                visit[w] = visit[v] + 1
                print(w, end = " ")

# 입력 -> 인접리스트
V, E = map(int, input().split())
temp = list(map(int, input().split()))

# # 인접리스트
# G = [[] for _ in range(V+1)]
G = {i:[] for i in range(1, V+1)}
# print(G) # {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

visit = [0] * (V+1)

for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)

print(G)
bfs(1)
print()
#1에서 가장 멀리 떨어져있는 정점을 구하는 건?
maxI = 0
for i in range(1, V+1):
    if visit[maxI] < visit[i]:
        maxI = i
print(maxI, visit[maxI]-1)