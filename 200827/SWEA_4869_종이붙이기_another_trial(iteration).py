## tips
# 여기서 N은 최대 30까지다.
# 그러니까 매번 memo만들어서 값 넣지말고, 차라리 30개짜리 리스트만들어서 하나씩 읽어오자. 꿑.
memo = [0] * (30 + 1)
memo[1], memo[2] = 1, 3
for i in range(3, 30 + 1):
    memo[i] = memo[i -1] + memo[i -2] * 2

for tc in range(1, int(input()) + 1):
    N = int(input()) // 10
    print(memo[N])

# ---------아래는 정석 풀이법----------------
# for tc in range(1, int(input()) + 1):
#     N = int(input()) // 10
#     memo = [0] * (N + 1) #초기값 0 --> 이 문제의 답을 아직 구하지 않음.
#     memo[1], memo[2] = 1, 3
#
#     for i in range(3, N + 1):  # i --> 문제의 크기를 나타내는 값
#         memo[i] = memo[i - 1] + memo[i - 2] * 2
#
#     print(memo[N])