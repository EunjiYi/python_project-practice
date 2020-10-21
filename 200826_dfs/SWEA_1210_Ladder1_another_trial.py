# import sys
# sys.stdin = open("input.txt")
#Ladder1 dfs(stack/반복문이용)로 풀이
def dfs():
    global ladder
    #갈 수 있는 방향, 좌, 우, 아래
    dr = [0,0,1]
    dc = [-1,1,0]
    #ladder의 첫번째 줄을 반복하면서 시작시점을 찾기
    for i in range(100):
        if ladder[0][i] == 1: #시작점 찾음
            #dfs 실행
            visited = [[0]*100 for _ in range(100)]
            # visited[0][i] = 1
            stack = list()
            stack.append((0,i)) # 시작지점 스택에 넣기
            while stack:
                cr,cc = stack.pop()   #현재위치
                visited[cr][cc] = 1
                for d in range(3):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if 0 <= nr < 100 and 0<=nc < 100 and visited[nr][nc] ==0:
                        if ladder[nr][nc] == 1:
                            stack.append((nr,nc))
                            break #더 이상 경로를 검사하지 않음
                        elif ladder[nr][nc] == 2:
                            return i
    return -1   # 혹시나 출구를 못찾으면 -1 반환, 이문제에서는 필요없는 코드

T = 10
for tc in range(T):
    tc = int(input())
    # 사다리 모양입력받고
    # 사다리 첫번째 줄 순회하면서, 1인지점(시작지점)을 찾음
    # 시작지점을 찾으면, dfs를 실행해서 목적지까지 도착하면
    # 해당 시작지점을 출력
    ladder = [list(map(int,input().split())) for _ in range(100)]
    result = dfs()
    print("#{} {}".format(tc,result))


