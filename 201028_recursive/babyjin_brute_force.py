arr = ["124783","667767","054060","101123"]

# baby-jin 완전탐색으로 풀기
# 조합으로 풀어보기  6가지 중에 3가지 숫자를 선택후 정렬
N = 6
K = 3
selected = [0] * N
def comb(selected,idx,cnt):
    if cnt == K:    # 조합에 포함되는 모든 요소를 선택했다.
        print(selected)# 모든 조합을 골랐으니, run과 triplet을 검사
        return
    if idx == N:
        return
    # idx에 해당하는 요소를 조합에 포함할지 안할지 결정
    selected[idx] = 1
    comb(selected, idx + 1,cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)

# selected[0] = 1
comb(selected,1,1)