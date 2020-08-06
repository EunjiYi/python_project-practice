#카드의 갯수를 저장하는 배열
# 배열의 인덱스에 해당하는 카드가 몇장인지 저장하는 배열

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input()))
    #[4,9,6,7,9]
    # 0~9
    counts = [0] * 10 # [0][0][0][0][1][0][0][0][0][0][0]
    for i in range(N):
        counts[cards[i]] += 1
   # counts 배열 순회하면서 최대값과 인덱스 저장
    max_v = counts[0]
    max_idx = 0
    for i in range(len(counts)):
        if max_v <= counts[i]:
            max_v = counts[i]
            max_idx = i

    print("#%d" % tc, max_idx,max_v)
