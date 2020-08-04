T = int(input())
for tc in range(1, T+1):
    num_count = int(input())
    numbers = input()

    cnt = [0] * 10  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in numbers:
        cnt[int(num)] += 1

    max = 0
    index = 0
    for i in range(len(cnt)):
        if cnt[i] >= max:
            max = cnt[i]
            index = i

    print('#{} {} {}'.format(tc, index, max))