def dfs(r, c): # 좌표(y,x)를 시작으로 이동할 수 있는 방의 갯수를 세기 함수
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    cnt = 1
    for d in range(4):
        cr = r + dr[d]
        cc = c + dc[d]
        if 0 <= cr < N and 0 <= cc < N and matrix[cr][cc] == matrix[r][c] + 1:
            cnt += dfs(cr, cc)
    return cnt

if __name__ == "__main__":

    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        count = [0] * (N*N+1) # 각 방번호별 최대 이동횟수 저장
        location = [] # 방번호의 좌표값을 저장하는 배열
        room_num = 0
        for i in range(N):
            for j in range(N):
                room_num += 1
                location.append((i, j))
                count[room_num] = dfs(i, j)

        min = float('inf')
        max_count = max(count)
        for num in range(1, N*N+1):
            if count[num] == max_count:
                y = location[num - 1][0]
                x = location[num - 1][1]
                if matrix[y][x] < min:
                    min = matrix[y][x]

        print(f'#{tc} {min} {max_count}')