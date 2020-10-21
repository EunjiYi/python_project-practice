for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza = [0] + list(map(int, input().split()))

    oven = [i for i in range(1, N+1)] #피자번호
    pos = N+1 #추가될 피자 번호

    while len(oven) > 1:
        num = oven.pop(0)
        pizza[num] = pizza[num] // 2
        if pizza[num]:
            oven.append(num)
        else:
            if pos <= M:
                oven.append(pos)
                pos += 1
    print(f'#{tc} {oven[0]}')