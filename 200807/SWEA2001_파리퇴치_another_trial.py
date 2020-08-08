N, M = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(N) ]

#자료를 한 줄씩 입력받아서 처리할 때는 이런식으로 많이 한다.
# for _ in range(N):
#     arr.append((list(map(int, input().split()))))

#모든 사각영역의 좌상단 좌표
for x in range(0, N-M+1):
    for y in range(0, N-M+1):

        S = 0
        #(x,y)이고 크기가 M인 사각영역을 처리
        for i in range(x, x+ M):
            for j in range(y, y,+M):
                S += arr[i][j]