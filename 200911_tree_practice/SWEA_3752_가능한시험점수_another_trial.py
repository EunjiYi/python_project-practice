T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    sum = set()
    sum.add(0)

    for i in range(len(scores)):
        tmp = []
        for j in sum:
            tmp.append(j + scores[i])
        sum.update(tmp)

    print(f'#{tc} {len(sum)}')
