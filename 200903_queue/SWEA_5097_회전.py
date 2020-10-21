T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = list(map(int, input().split()))

    for _ in range(M):
        matrix.append(matrix.pop(0))
    print(f'#{tc} {matrix[0]}')