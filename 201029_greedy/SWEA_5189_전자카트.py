import sys
sys.stdin = open('123.txt', 'r')

def car():
    tmp = 0
    r = 0
    c = arr[0]-1
    tmp += matrix[r][c]
    for i in range(1, len(arr)):
        r = c
        c = arr[i] - 1
        tmp += matrix[r][c]
    tmp += matrix[arr[-1]-1][0]
    return tmp

# permutation(순열)
def perm(idx):
    global min_sum
    if idx >= N-1:
        #print(arr) #[2, 3] [3, 2]
        sum = car()
        if sum < min_sum:
            min_sum = sum
        return
    # 현재 idx에서 해야할 모든 경우의 수
    # 나보다 뒤쪽에 있는 모든 요소들과 자리 바꾸기
    for i in range(idx, N-1):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]


for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    arr = [0] * (N-1)
    for i in range(2, N+1):
        arr[i-2] = i
    #print(arr) #[2, 3]
    perm(0)
    print("#{} {}".format(tc, min_sum))