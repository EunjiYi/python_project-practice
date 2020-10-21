T = int(input())
for tc in range(1, T+1):
    # 화덕의 크기(N) 피자갯수(M)
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    queue = []
    for i in range(N):
        queue.append([i+1, data[i]])

    lastnum = N
    while len(queue)!= 1:
        queue[0][1] = queue[0][1] // 2

        if queue[0][1] <= 0:
            if lastnum < M:
                queue.pop(0)
                queue.append([lastnum + 1, data[lastnum]])
                lastnum += 1
            else:
                queue.pop(0)

        # 맨 앞에 있던 걸 맨 뒤로.
        else:
            queue.append(queue.pop(0))

    print(f'#{tc} {queue[0][0]}')