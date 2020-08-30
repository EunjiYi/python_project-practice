# import sys
# sys.stdin = open("input.txt")

def dfs():
    global min_cnt, result
    #해야할일
    # 모든 시작점 검사하면서 경로 길이 재기
    # 좌,우, 아래
    dr = [0,0,1]
    dc = [-1,1,0]
    for i in range(len(ladder)):
        if ladder[0][i] == 1:
            visited = [[0] * 100 for _ in range(100)]
            stack = list()
            stack.append((0,i))
            cnt = 1 #경로의 길이를 재기 위한 변수
            while stack: #스택이 비어있지 않으면 계속 반복
                #사다리타기 이기 때문에 경로는 한가지, 가장 빨리 가는길만 가면된다.
                # 되돌아와서 모든 경로를 탐색할 필요가 없으니 pop
                cr,cc = stack.pop()
                visited[cr][cc] = 1
                for d in range(3):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if 0<= nr < len(ladder) and 0 <= nc < len(ladder) and not visited[nr][nc] and ladder[nr][nc]:
                        stack.append((nr, nc))
                        cnt += 1
                        if nr == 99: #사다리 끝까지 도착
                            # 여태 까지 왔던 경로가 최단 경로인지 확인
                            if min_cnt > cnt:
                                min_cnt = cnt
                                result = i
                        break   #이미 경로를 찾았으니 다른 경로는 생각할 필요가 없다.


T = 10
for x in range(T):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    min_cnt = 10000
    result = 0
    dfs()
    print("#{} {}".format(tc, result))