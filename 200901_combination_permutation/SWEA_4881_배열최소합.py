# 백트래킹 연습하기
# backtracking 문제 풀 때 조심해야할 것
# DFS와 유사하지만 가지치기를 해야한다.
# 가지치기를 해야한다 = 경로 선택 후 그 부분이 틀려서 다시 돌아와야하면
# 방문했던 경로 or 조건값을 다시 원래대로 되돌려놔야한다. *연습필요*

def getResult(y): # y행에서 하나의 값을 골라서 sum에 누적해서, 그 중에 min값을 찾는 함수
    global sum, min

    # 아 이 한 줄을 빼먹어서 진짜 오래걸렸다...ㅠ
    # 재귀니까 이 함수가 호출되기 전 함수들에서, 케이스 하나 제대로 다 나왔으면 min값이 inf에서 특정값으로 바꼈을 거다.
    # 그러니까 또 다른 경우의 수를 구할 때는 직전에 구한 케이스보다 sum이 크게 되는 순간, 더이상 구할 필요가 없는 거다.
    # 잘 안보였다 ㅠㅠㅠ
    if min < sum:
        return

    if y == N:
        if sum < min:
            min = sum
            return

    for x in range(N): # y가 고정되어있으니 x열에서 하나를 고른다.
        if not visited[x]: # 직전 단계에서 고르지 않았다면
            visited[x] = 1 # 고르고나서
            sum += matrix[y][x] # sum에 더해주기

            getResult(y+1) # 그 다음 것 진행

            visited[x] = 0 #아니라면 원복
            sum -= matrix[y][x] # 원복


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sum = 0
    min = float('inf')

    getResult(0) # 0행에서 시작

    print(f'#{tc} {min}')