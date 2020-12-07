move = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

for tc in range(1, int(input())+1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    max_drt = -1
    stack = []
    for fy in range(N -2):
        for fx in range(1, N-1):
            stack.append([fx, fy, 0, [desserts[fy][fx]]])
            while stack:
                x, y, go, eat = stack.pop()
                if go < 3:
                    if go == 2 and y == fy:
                        continue
                    for i in range(go, go+2):
                        nx, ny = x + move[i][0], y + move[i][1]
                        if -1 < nx < N and -1 < ny < N and desserts[ny][nx] not in eat:
                            stack.append([nx, ny, i, eat + [desserts[ny][nx]]])
                        elif fx == nx and fy == ny and max_drt < len(eat):
                            max_drt = len(eat)
                else:
                    nx, ny = x + move[go][0], y + move[go][1]
                    while desserts[ny][nx] not in eat and nx < fx and fy < ny:
                        eat.append(desserts[ny][nx])
                        nx += move[go][0]
                        ny += move[go][1]
                    if fx == nx and fy == ny and max_drt < len(eat):
                        max_drt = len(eat)
    print("#{} {}".format(tc, max_drt))