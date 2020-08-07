# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    max_v = 1
    min_v = 1000000
    # 초기값은 항상 이유가 있어야 한다 *****

    for i in range(N):
        if max_v < numbers[i]:
            max_v = numbers[i]
        if min_v > numbers[i]:
            min_v = numbers[i]
    print("#%d" %tc, max_v-min_v)