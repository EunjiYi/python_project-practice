# 주어진 x, y좌표의 경계를 체크하는 함수
def check(x, y):  # 갈 수 있으면  True반환
    if x < 0 or x >= 100 or y < 0 or y >= 100: return False
    if arr[x][y] == 0: return False
    return True

for tc in range(1, 11):
    case_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    #도착점을 찾는다.
    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    #direction
    while x:  # 이러면  x가 0일 때 멈춘다.
        arr[x][y] = 0 #방문한 길 지워버리기 = 지나온 길 back하는 현상이 안생기도록
        if check(x, y - 1): #왼쪽으로 가는 경우
            y -= 1
        elif check(x, y + 1): #오른쪽으로 가는 경우
            y += 1
        else:  # 그 외, 위로 가는 경우
            x -= 1

    print(f"#{tc} {y}")
