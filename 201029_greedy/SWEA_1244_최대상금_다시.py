import sys
sys.stdin = open('123.txt', 'r')


def permu(idx, scnt): #scnt = switch count 교환횟수
    global remain, find_max, max_tmp

    # 이게 없으면 4번, 5번 케이스 안 맞음.
    #원래답 #4 87664 -> 내꺼 출력 #4 87646
    #원래답 #5 88832 -> 내꺼 출력 #5 88823

    if find_max == True: #-> 이 내용을 case 1 if문에 넣으면 4번만 정상동작, 따로 return 시켜야함        return
        return           # case 1 if문에 max_tmp2 < int(''.join(card))로 해도 5번은 88823으로 출력됨.

    # case 1
    # 교환횟수 전에 최댓값 나왔을 때
    if scnt <= h and card_desc == card:
        remain = h - scnt
        find_max = True # case 1, 2번을 구분하는 flag
        return

    # case 2
    # 교환횟수가 다 지나도 최댓값 안 나왔을 때
    if scnt >= h and card_desc != card:
        find_max = False
        tmp2 = int(''.join(card))
        if max_tmp < tmp2:
            max_tmp = tmp2 # 현재 교환횟수 중에서 나올 수 있는 최댓값
        return

    if idx >= N:
        return

    for i in range(idx + 1, N): # 자기자신이랑 비교할 필요 없으니 idx+1부터 for문 시작.
        if card[idx] < card[i]: #card[idx]현재(커서)카드 < card[i]현재보다 뒤의 카드가 더 커야 교환가능
            card[idx], card[i] = card[i], card[idx]
            permu(idx + 1, scnt + 1)
            card[i], card[idx] = card[idx], card[i]
        else:
            permu(idx + 1, scnt) # 안크면 교환 안하고 다음으로 진행.


for tc in range(1, int(input())+1):
    tmp1, h = input().split()
    card = list(tmp1)
    h = int(h)
    N = len(card)
    #print(card)

    #최댓값 먼저 알기
    card_desc = sorted(card, reverse = True) #내림차순정렬
    #print(card_desc)
    cardmaxnumber = ''
    for t in card_desc:
        cardmaxnumber += t
    #print(cardmaxnumber)

    remain = -1
    find_max = False
    max_tmp = 0

    # 순열돌리기
    permu(0, 0)

    # case 1
    if find_max:
        if remain % 2: # 남은 교환횟수가 홀수일 때
            # 중복이 있으면 그 두 개를 바꾼다.
            for i in range(len(card)):
                if card.count(card[i]) >= 2:
                    print("#{} {}".format(tc, cardmaxnumber))
                    break
            else:# 중복이 없으면 최댓값에서 가장 마지막자리 두 개를 교환한다.
                card_desc[-1], card_desc[-2] = card_desc[-2], card_desc[-1]
                result = int(''.join(card_desc))
                print("#{} {}".format(tc, result))
        else: # 짝수 일 때 최적해 바로 출력(바꾼거 다시 바꾸면 제자리니까)
            print("#{} {}".format(tc, cardmaxnumber))
    # case 2
    else:
        print("#{} {}".format(tc, max_tmp))