import sys
sys.stdin = open('123.txt', 'r')

def comb(idx, n):
    global max_cnt
    if idx == n: #끝까지 다 포함유무 탐색했으면,
        #print(selected)
        timetable = [0] * 24 # 0~23시까지
        cnt = 0
        for i in range(n):
            if selected[i]:
                cnt += 1
                for j in range(time[i][0], time[i][1]):
                    timetable[j] += 1
                    #print(time[i][0], time[i][1])
                    #print(timetable)
                    for k in range(24):
                        if timetable[k] >= 2:
                            return
                if cnt > max_cnt:
                    max_cnt = cnt
        return

    selected[idx] = 1
    comb(idx + 1, n)
    selected[idx] = 0
    comb(idx + 1, n)

for tc in range(1, int(input())+1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    #print(time)

    # n개 중 조건에 만족하는 조합을 찾자.
    selected = [0] * n
    max_cnt = 0
    comb(0, n)
    print("#{} {}".format(tc, max_cnt))
