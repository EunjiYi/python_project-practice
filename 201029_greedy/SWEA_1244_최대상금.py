import sys
sys.stdin = open('123.txt', 'r')

def permu(h):
    global result

    number = int(''.join(card))
    selected.append([h, number])

    if h == 0:
        if number > result:
            result = number
        return

    for i in range(len(card)):
        for j in range(i + 1, len(card)):
            card[i], card[j] = card[j], card[i]
            if [h - 1, int(''.join(card))] not in selected:
                permu(h - 1)
            card[i], card[j] = card[j], card[i]


for tc in range(1, int(input())+1):
    tmp, t = input().split()
    card = list(tmp)
    h = int(t)

    selected = []
    result = float('-inf')
    permu(h)

    print('#{} {}'.format(tc, result))
