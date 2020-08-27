T = int(input())
for tc in range(1,T+1):
    str1 = input()
    #ABAA
    str2 = input()
    # A B C D E F G H I J K L
    # 0 1 2 3 4 5 6 7 8 9 10 12
    #[1][2][1][1][][][][][][][][][][][][][][][][][][]
    used_arr = [0] * 26 # str1에 포함된 알파벳을 표시하기 위한 배열
    cnt_arr = [0] * 26 #각 알파벳이 몇번씩 사용되었는지 표시하기 위한 배열

    for c in str1:
        #A => 0 B = 1 C = 2
        # ord(A) - ord(A) =  0
        used_arr[ord(c)-ord("A")] = 1
    for c in str2:
        #str2 BACDAAA
        if used_arr[ord(c)-ord("A")] == 1:
            cnt_arr[ord(c)-ord("A")] += 1

    print("#{} {}".format(tc,max(cnt_arr)))

