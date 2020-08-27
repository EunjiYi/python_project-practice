T = 10
N = 100

for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    matrix = [[0] * 102 for _ in range(102)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            matrix[i+1][j+1] = arr[i][j]
            if matrix[i+1][j+1] == 2:
                a = j+1

    pick = 0
    min = 987987987987987987987987987987987987987987987987987987987987
    for j in range(1, 101):
        if matrix[1][j] == 1: #시작점에서 start
                a = j
                cnt = 0

                #i : 아래로 한 칸씩 내려감.
                for i in range(1, 101):
                    cnt += 1 #아래로 한 칸 내려갔으니까 카운트 1 추가

                    if matrix[i][a+1] == 1: #오른쪽탐색 - 오른쪽으로 갈 수 있을 때까지 쭉 간다.
                        while True:
                            cnt += 1
                            a = a + 1
                            if not matrix[i][a+1]:
                                break
                    elif matrix[i][a-1] == 1:
                        while True:
                            cnt += 1
                            a = a - 1
                            if not matrix[i][a-1]: #왼쪽탐색 - 왼쪽으로 갈 수 있을 때까지 쭉 간다.
                                break

                    if cnt > min:
                        break  # 다 찾고나서 비교하지 말고 현재 최솟값보다 크면 그냥 바로 탐색 취소하고 다음꺼한다.
                # 탐색끝
                if cnt < min:
                   min = cnt
                   pick = j - 1

    print('#{} {}'.format(tc, pick))