T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    numbers = list(map(int,input().split()))
    max_v = 1 * M
    min_v = 10000 * M

    for i in range(0,len(numbers)-(M-1)):
        #시작점을 다르게 하면서 구간을 반복하며 합구하기
        sum_v = 0
        for j in range(i,M+i): #구간합 구하기
            sum_v += numbers[j]
        # 구간합 최대 최소 비교
        if sum_v > max_v:
            max_v = sum_v
        if sum_v < min_v:
            min_v = sum_v
    print("#%d" % tc, max_v-min_v)
