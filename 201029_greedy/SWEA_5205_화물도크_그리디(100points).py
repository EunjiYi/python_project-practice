# import sys
# sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]

    time = sorted(time, key = lambda x: x[1]) #빨리 끝나는 순서대로 정렬
    #print(time)

    cnt = e = 0
    for i in range(n):
        if time[i][0] >= e:
            cnt += 1
            e = time[i][1]
    #print(cnt)
    print("#{} {}".format(tc, cnt))