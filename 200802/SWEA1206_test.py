import sys
sys.stdin = open("input.txt", "r")



for k in range(1, 3):
    num = int(input())  # 갯수입력받음 #지금 100
    height = list(map(int, input().split()))  # 땅 정보 받음
    cnt = 0  # 뷰좋은갯수, 즉 정답
    for i in range(2, len(height)-1):
        target = height[i]
        while target > 0:
            if target > height[i-1] and target > height[i-2] and target > height[i+1] and target > height[i+2]:
                cnt = cnt + 1
                target = target-1
            else:
                break;

    print(f'#{k} {cnt}')