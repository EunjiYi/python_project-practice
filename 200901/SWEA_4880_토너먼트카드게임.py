def game(start, end):
    if start == end: #start와 (첫번째 사람) end가(마지막사람) 같다 = 한 명인 그룹
       return start # 그 한 명 리턴

    # 절반씩 나누어서 게임 실행
    # 앞 그룹의 승자, 뒷 그룹의 승자를 각각 구한 뒤
    # 다시 승자를 결정한다.
    center = (start + end) // 2
    group1 = game(start ,center)
    group2 = game(center + 1, end)

    # 두 그룹의 승자 중 이긴 사람을 반환
    # 1: 가위 / 2: 바위  / 3: 보
    group1_card = cards[group1]
    group2_card = cards[group2]
    if group1_card == 1: # 가위
        if group2_card == 2: # 바위
            return group2
        else:
            return group1 #보
    elif group1_card == 2:  #바위
        if group2_card == 3: #보
            return group2
        else:
            return group1 #가위
    elif group1_card == 3: #보
        if group2_card == 1: # 가위
            return group2
        else:
            return group1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int,input().split()))

    result = game(0, N-1)
    print("#{} {}".format(tc,result+1)) #사람 인덱스 0부터 시작했으니까 마지막 결과는 +1 해주기
