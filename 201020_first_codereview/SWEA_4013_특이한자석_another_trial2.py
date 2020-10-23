# import sys
# sys.stdin = open('특이한자석.txt')

def activation(idx,dir,signal):

    global magnet

    # 왼쪽에 있는 톱니바퀴가 다른 극성의 자석인지 확인
    if signal != 1 and idx != 0 and magnet[idx][-2] != magnet[idx-1][2]:
        activation(idx-1,-dir,-1)

    # 오른쪽
    if signal != -1 and idx != 3 and magnet[idx][2] != magnet[idx+1][-2]:
        activation(idx+1,-dir,1)

    if dir == 1:
        magnet[idx].insert(0,magnet[idx].pop())
    else:
        magnet[idx].append(magnet[idx].pop(0))
    # print(magnet, idx, dir)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #
    magnet = [list(map(int,input().split())) for _ in range(4)]

    active = [list(map(int,input().split())) for _ in range(N)]

    print(active)
    print(magnet)

    for i in range(N):

        activation(active[i][0]-1,active[i][1],0)

    summ = 0
    # print(magnet)
    for a in range(4):
        if magnet[a][0]:
            summ += 2**a
    print(f'#{tc}',summ)
