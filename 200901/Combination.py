# 부분 집합중에 요소의 개수가 특정 수 인 집합
# [1][2][3] >> 이거 중에 2개 골라라
# N개 중에 3개 고르기
N = 5
selected = [0] * N
T = 3
def comb(idx,cnt):
    # idx : 인덱스, cnt : 현재 부분집합이 포함하는 요소 개수
    # idx가 벗어나거나, 원하는 만큼의 요소를 이미 선택했을 때
    # 더이상 진행할 필요가 없음
    if cnt == T: # 필요한 개수만큼 선택함
        print(selected)
        return
    if idx >=N: # 범위 벗어남
        return

    # 요소의 포함/미포함 여부 결정
    selected[idx] = 1
    comb(idx+1,cnt+1)
    selected[idx] = 0
    comb(idx+1,cnt)

comb(0, 0)


