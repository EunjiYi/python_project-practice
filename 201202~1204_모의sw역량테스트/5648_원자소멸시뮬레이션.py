#상하좌우 - 일반 2차원배열 상하좌우와 다르다. xy좌표상에서의 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    atom = []
    ans = 0
    for _ in range(n):
        x, y, dir, e = map(int, input().split())
        atom.append([x*2, y*2, dir, e])
    # print(atom)

    for t in range(4001): #0.5초를 1로 했으니 2000이 아닌 4000
        dic = {} # 매 시간마다 새로 갱신해야한다. = 매 시간마다 초기화!
        for a in range(n):
            if atom[a][3] != 0:
                atom[a][0] = atom[a][0] + dx[atom[a][2]] ## x, y 잘보기!!!!!!!!  여기서는 r, c보다 x, y가 더 정확하다.
                atom[a][1] = atom[a][1] + dy[atom[a][2]]
                nx, ny = atom[a][0], atom[a][1]

                if nx <= 2000 and ny <= 2000: #0.5초를 1로 했으니 좌표도 *2
                    if (nx, ny) not in dic:
                        dic[(nx, ny)] = a
                    else: #먼저와있는 애가 있다.
                        ans += (atom[dic[(nx, ny)]][3] + atom[a][3])
                        atom[a][3] = 0
                        atom[dic[(nx, ny)]][3] = 0

    print("#{} {}".format(tc, ans))

