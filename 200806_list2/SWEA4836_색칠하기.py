T = int(input())
for tc in range(1, T+1):
    paper = [[0] * 10 for _ in range(10)]  # 파이썬은 인터프리터가 줄 단위로 읽어오니까


    num = int(input()) #색칠횟수

    for _ in range(num):
        y1, x1, y2, x2, color = map(int,input().split())
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                paper[i][j] += color

    cnt = 0
    #완전탐색으로 3인 것의 갯수 구하기
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                cnt += 1

    print("#{} {}".format(tc, cnt))