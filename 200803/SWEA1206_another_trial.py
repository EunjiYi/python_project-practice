import sys
sys.stdin = open("input.txt","r")
T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    #print(buildings) #입력 제대로 되는 것 꼭 확인하고 코드짜기. 디버깅 열심히 했는데 한줄 입력 덜 받으면 omg
    #print('#%d' % tc)

# 각 건물의 왼쪽, 오른쪽 조망권을 구하고
# (왼쪽, 오른쪽 다 ) 옆건물 옆옆건물의 높이 중 더 높은 건물의 높이를
# 현재 건물의 높이에서 빼면, 각 방향 조망권을 계산할 수 있다.
# 왼쪽, 오른쪽 조망권을 더 적은 값이 건물의 조망권이 확보된 세대의 수이다.
# 단 조망권의 크기는 1이상일 경우에만 생각한다.


#시작해야할 인덱스 : 2부터 (길이-1)-2까지.
    total = 0
    for i in range(2, N-2):

        #print(buildings[i], end = " ") #for문 인덱스 확인
        # 1. 왼쪽 조망권 구하자
        # 왼쪽 옆건물, 옆옆건물 중 큰 값 선택
        left = 0 # 왼쪽 옆/ 옆옆건물 중 큰 값 고른것을 넣는다.
        left_view = 0

        if buildings[i-1] > buildings[i-2]:
            left = buildings[i - 1]
        else:
            left = buildings[i - 2]

        left_view = buildings[i] - left

        # 2. 오른쪽 조망권 구하자
        right = 0  # 오른쪽 옆/ 옆옆건물 중 큰 값 고른것을 넣는다.
        right_view = 0

        if buildings[i + 1] > buildings[i + 2]:
            right = buildings[i + 1]
        else:
            right = buildings[i + 2]

        right_view = buildings[i] - right

        # 조망권이 없는 경우(음수)인 경우면 아무것도 하지 않겠다 선언하기
        if left_view <= 0 or right_view <=0:
            continue

        #왼쪽조망권과 오른쪽 조망권 중 작은 값을 가지는 조망권을 더한다.
        if left_view > right_view:
            total += right_view
        else:
            total += left_view



    print("#%d" %tc, total)



