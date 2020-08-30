T = int(input())

for tc in range(1, T+1):
    N, C = map(int, input().split())
    listlist = list(map(int, input().split()))

    result = []
    for i in range(N-C+1):
        result.append(sum(listlist[i:i+C]))

    print(f'#{tc} {max(result)-min(result)}')