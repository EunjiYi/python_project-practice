# permutation(순열)
N = 5
arr = [1, 2, 3, 4, 5]


def perm(idx):
    if idx >= N:
        print(arr)
        return
    # 현재 idx에서 해야할 모든 경우의 수
    # 나보다 뒤쪽에 있는 모든 요소들과 자리 바꾸기
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        #arr[i],arr[idx] = arr[idx],arr[i]  -- 바로 윗 줄이랑 완벽히 같은 건데 바로 윗 줄이 내 기준에 좀 더 이해가 편함 ㅋ

        perm(idx + 1)

        arr[idx], arr[i] = arr[i], arr[idx]
        #arr[i], arr[idx] = arr[idx], arr[i]
perm(0)