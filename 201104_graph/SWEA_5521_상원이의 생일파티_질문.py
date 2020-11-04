from collections import deque

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    #print(n, m)
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    #print(adj)
    visit = [0] * (n+1)

    queue = deque()
    queue.append((1, 1, 0)) # 상원이가 1번 / 레벨1 / cnt = 0 상원이는 카운트에 포함 안됨.
    visit[1] = 1 # 방문 체크

    while queue:
        c_node, level, cnt = queue.popleft()

        for n_node in adj[c_node]:
            if visit[n_node] == 0:
                if level <= 2: #1, 2 일 때만 돌게
                    queue.append((n_node, level+1, cnt+1))
                    visit[n_node] = 1

    print("#{} {}".format(tc, cnt))

'''
	
append 하면서 cnt를 증가 시키면

상원이를 몇 단계 거쳐서 알게 되느냐? 하는 그 거리가 되어 버려요

그러니 친구 2, 친구3, 친구4  가 전부 2가 되는거죠 근데 우리는 사람 수가 필요한거니까 

1,2,3,4 가 되어야 되져..
'''
### 와... 진짜 바보네요.. 바로 이해됐어요  설명 감사합니다....