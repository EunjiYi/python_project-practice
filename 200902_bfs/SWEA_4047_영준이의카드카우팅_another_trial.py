T = int(input())
for tc in range(1,T+1):
    cards = input()
    #카드 무늬별로 카드를 세기 위한 배열생성
    #무늬 S,D,H,C
    s_arr = [0] * 14
    d_arr = [0] * 14
    h_arr = [0] * 14
    c_arr = [0] * 14
    #D03,D13
    result = False #카운팅이 정상종료 되었는지 표시하는 변수
    for i in range(0,len(cards),3):
        shape = cards[i]
        number = int(cards[i+1] + cards[i+2])
        # number = cards[i+1:i+3]
        if shape == 'S':
            if s_arr[number] == 1:  # 해당 카드가 있으면 종료
                break   #더이상 검사하지 않음
            s_arr[number] = 1
            s_arr[0] += 1 # 0번 인덱스를 총 보유한 카드 갯수로 활용하는 것이 참신하다.
        elif shape == 'D':
            if d_arr[number] == 1:  # 해당 카드가 있으면 종료
                break   #더이상 검사하지 않음
            d_arr[number] = 1
            d_arr[0] += 1
        elif shape == 'H':
            if h_arr[number] == 1:  # 해당 카드가 있으면 종료
                break   #더이상 검사하지 않음
            h_arr[number] = 1
            h_arr[0] += 1
        elif shape == 'C':
            if c_arr[number] == 1:  # 해당 카드가 있으면 종료
                break   #더이상 검사하지 않음
            c_arr[number] = 1
            c_arr[0] += 1
    else:
        #겹치는 카드 없이 정상종료
        result = True

    if result: # 정상종료, 카운팅이 잘 끝난경우
        #카드장수 출력
        print("#{} {} {} {} {}".format(tc,13-s_arr[0],13-d_arr[0],13-h_arr[0],13-c_arr[0]))
    else:
        print("#{} ERROR".format(tc))