import copy
#연산자 나열의 모든 경우의 수 구하기
def solve(idx,order):
    global min_v,max_v
    if idx >= N-1:
        # 0 : 더하기
        # 1 : 빼기
        # 2: 곱하기
        # 3 : 나누기
        numbers_copy = copy.deepcopy(numbers)
        for i in range(N-1):
            if order[i] == 0:
                numbers_copy[i + 1] = numbers_copy[i] + numbers_copy[i+1]
            elif order[i] == 1:
                numbers_copy[i + 1] = numbers_copy[i] - numbers_copy[i + 1]
            elif order[i] == 2:
                numbers_copy[i + 1] = numbers_copy[i] * numbers_copy[i + 1]
            elif order[i] == 3:
                numbers_copy[i + 1] = int(numbers_copy[i] / numbers_copy[i + 1])

        if numbers_copy[-1] > max_v:
            max_v = numbers_copy[-1]
        if numbers_copy[-1] < min_v:
            min_v = numbers_copy[-1]

    #사용가능한 연산자 살펴보기
    for i in range(4):  #연산자의 종류가 4개
        if opers[i] > 0: #사용가능한 연산자가 남아있으면, 선택
            order[idx] = i
            opers[i] -= 1   #사용했으니, 연산자의 개수를 1줄인다.
            solve(idx+1,order)
            opers[i] += 1   #원상복귀



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    opers = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    max_v = -1000000000
    min_v = 1000000000
    order = [-1] * (N-1)
    solve(0,order)
    print("#{} {}".format(tc,max_v - min_v))