import sys
sys.stdin = open('SWEA_10888_음식배달_input.txt')


def comb(idx):
    global result
    if idx == len(food):
        csum = 0
        for h in range(len(home)):
            cmin = float('inf')  # cost min값을 이렇게 지정해서, selected가 공집합일 때 if result > csum:로 넘어간다.
            for f in range(len(selected)):
                if selected[f]:
                    cmin = min(cmin, dist[f][h])  # 집과 가장 가까운 음식점 사이의 거리 더하기
            csum += cmin
        for f in range(len(selected)):
            if selected[f]:
                csum += food[f][2]  # 운영비 더하기
        if result > csum:
            result = csum

    # 요소의 포함/미포함 여부 결정
    else:
        selected[idx] = 1
        comb(idx + 1)
        selected[idx] = 0
        comb(idx + 1)


if __name__ == "__main__":
    for tc in range(1, int(input()) + 1):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]

        home, food = [], []
        # 전처리 #집모으기 #음식점모으기
        for r in range(N):
            for c in range(N):
                if matrix[r][c] == 1:
                    home.append((r, c))  # 집 좌표
                elif matrix[r][c] > 1:
                    food.append((r, c, matrix[r][c]))  # 가게 좌표와 운영비

        # 모든 집과 모든 음식점 사이의 거리를 미리 다 계산해두기 - 계속 반복해서 쓰니까, 퍼포먼스 향상
        dist = [[0] * len(home) for i in range(len(food))]
        for i in range(len(food)):
            for j in range(len(home)):
                dist[i][j] = abs(food[i][0] - home[j][0]) + abs(food[i][1] - home[j][1])

        selected = [0] * len(food)
        result = float('inf')
        comb(0)
        print("#%d" % tc, result)

