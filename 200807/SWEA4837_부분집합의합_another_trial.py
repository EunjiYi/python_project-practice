# 4bit 2진수 -> 0~15
# 4bit로 표현할 수 있는 모든 경우 중에 1이 2번 포함된 경우
#1100 1010 1001 ...


# #arr = [1,2,3,4]
# for bits in range(1 << 4):
#     cnt = S = 0
#     for i in range(4):
#         if bits & (1 << i):
#             cnt += 1
#             #S += arr[i]
#
#     if cnt == 2:
#         for i in range(3, -1, -1):
#             if bits & (1<<i): print(1, end='')
#             else: print(0, end='')
#         print()

N, K = map(int, input().split())
#N: 부분집합 원소수
#K: 부분집합의 합
#arr = [i for i in range(1, 12+1)]
ans = 0
for bits in range(1, 1 << 12):
    cnt = S = 0
    for i in range(12):
        if bits & (1 << i):
            cnt += 1
            S += i + 1 #arr[i]로 안해도 간단하네? i가 1부터 12니까.

    if cnt == N and S == K:
        ans += 1
