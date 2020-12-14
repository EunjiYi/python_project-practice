#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(1, int(input())+1):
    n = int(input())
    atom = []
    ans = 0
    for _ in range(n):
        r, c, dir, e = map(int, input().split())
        atom.append([r*2, c*2, dir, e])
    # print(atom)

    for t in range(4001): #0.5초를 1로 했으니 2000이 아닌 4000
        dic = {}
        for a in range(n):
            if atom[a][3] != 0:
                atom[a][0] = atom[a][0] + dr[dir]
                atom[a][1] = atom[a][1] + dc[dir]
                nr, nc = atom[a][0], atom[a][1]

                if nr <= 2000 and nc <= 2000: #0.5초를 1로 했으니 좌표도 *2
                    if (nr, nc) not in dic:
                        dic[(nr, nc)] = a
                    else: #먼저와있는 애가 있다.
                        ans += (atom[dic[(nr, nc)]][3] + atom[a][3])
                        atom[a][3] = 0
                        atom[dic[(nr, nc)]][3] = 0

    print("#{} {}".format(tc, ans))

