# 문제푸는 순서
# 점화식을 찾는다 -> 기저조건을 쓴다 -> 제귀로 만든다. -> 메모이제이션하기

def f(n): # n : 문제의 크기(식별값)
    # 기저조건
    if n == 1: return 1
    if n == 2: return 3

    # 일반 사례 - 메모이제이션
    if memo[n]:
        return memo[n] # 구해놓은게 있으면 이거 쓰자!
    # 일반 사례 - 메모에 없으면 새로 구하기
    memo[n] = f(n - 1) + f(n - 2) * 2
    return memo[n]

for tc in range(1, int(input()) + 1):
    N = int(input()) // 10
    memo = [0] * (N + 1)
    print(f(N))