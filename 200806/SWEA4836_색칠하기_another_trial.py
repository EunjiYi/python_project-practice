#for tc in range(1, int(input())+1):
#    N = int(input())
arr = [[0] * 10 for _ in range(10)]

#방법1 좌상단 우하단 좌표 이용하기
#    for _ in range(N):
#        x1, y1, x2, y2, color = map(int, input().split())

        # for i in range(x1, x2+1):
        #     for j in range(y1, y2+1):
        #         arr[i][j] += color #겹쳐지는 부분의 색은 3

#방법2 좌상단좌표와 사이즈 이용하ㅣ. 이때 사이즈 넘어가서 인덱스레인지오류 안나도록 처리가 필요함.
x, y = 3, 4
size = 3
# x부터 x+size-1까지
for i in range(x, x + size):
    for j in range(y, y + size):
        arr[i][j] = 1

for lst in arr:
    print(*lst)


