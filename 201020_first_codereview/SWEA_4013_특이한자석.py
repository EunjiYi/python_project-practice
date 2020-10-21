# target 리스트를 시계 방향으로 1 회전 시키는 함수
def clockwise(target):
    tmp = target.pop(-1)
    target.insert(0, tmp)

# target 리스트를 반시계 방향으로 1 회전 시키는 함수
def anticlockwise(target):
    tmp = target.pop(0)
    target.append((tmp))


for tc in range(1, int(input()) + 1):
    K = int(input())
    gear = {
        1: list(map(int, input().split())),
        2: list(map(int, input().split())),
        3: list(map(int, input().split())),
        4: list(map(int, input().split())),
    }
    #print(K, gear[1], gear[2], gear[3], gear[4])

    for _ in range(K):
        num_origin, clock = map(int, input().split())
        #print(num, clock)

        # 인덱스 번호는 톱니바퀴 번호
        # input 받을 때마다 새로 리셋되어야해서 for문 안에 넣음
        cc = [0] * 5 # 시계 방향으로 돌려야하면 True
        ac = [0] * 5 # 반시계 방향으로 돌려야하면 True
        #print(cc, ac)

        num = num_origin
        if clock == 1: # 시계방향
            cc[num] = 1 # 1번 톱니바퀴를 시계방향으로 한 칸 돌려야한다는 의미
        else: # 반시계방향
            ac[num] = 1

        # num보다 번호가 큰 톱니바퀴 체크
        while num + 1<= 4:
            if ( cc[num] or ac[num] ) and (gear[num][2] != gear[num+1][6]): # 뭔가 이동이 있고, 자성이 다를 때
                if cc[num] == 1:
                    ac[num + 1] = 1 # 반시계 방향으로 한 칸 돌려라.
                elif ac[num] == 1:
                    cc[num + 1] = 1
            num = num + 1


        # num 보다 번호가 작은 톱니바퀴 체크
        num = num_origin
        while num - 1 >= 1:
            if ( cc[num] or ac[num] ) and (gear[num][6] != gear[num-1][2]):
                if cc[num]:
                    ac[num - 1] = 1
                else:
                    cc[num - 1] = 1
            num = num - 1

        # checking 해 놓은 것들을 실제로 돌린다.
        for i in range(1, 5):
            if cc[i]:
                clockwise(gear[i])
            elif ac[i]:
                anticlockwise(gear[i])

    #print(gear[1], gear[2], gear[3], gear[4])
    score = 0
    for i in range(1, 5):
        if gear[i][0] == 1:
            score += 2 ** (i - 1)
    print("#{} {}".format(tc, score))