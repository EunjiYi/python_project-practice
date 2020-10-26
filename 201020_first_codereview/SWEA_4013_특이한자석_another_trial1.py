### 처음부터 시계/반시계로 돌려버리면 안되서, 돌리지는 않은 상태에서 시계/반시계로 돌릴 것 미리 체크 다 한 뒤에 , 마지막에 한 번에 돌렸는데
#그러지 말고 애초에 제일 안쪽 것부터 시계/반시계로 돌려버리면 됐다! = 재귀쓰면 되지!

def act(g_num, g_direc, signal): # signal을 주는 것이 관건!!! -1: 계속 왼쪽기어 체크 , 1: 계속 오른쪽기어 체크, 맨 처음에는 어디 체크할지 모르니까 0
    # 서로 붙어있는 날의 자성이 다른 경우에만 반대방향으로 1칸 회전.

    # 왼쪽에 있는 톱니바퀴가 다른 극성의 자석인지 확인.
    if signal != 1 and g_num != 0 and gear[g_num][-2] != gear[g_num-1][2]: # 그래서 if절 조건문 순서도 시그널이 제일 앞에
        act(g_num-1, -g_direc, -1)

    # 오른쪽에 있는 톱니바퀴가 다른 극성의 자석인지 확인.
    if signal != -1 and g_num != 3 and gear[g_num][2] != gear[g_num+1][-2]:
        act(g_num+1, -g_direc, 1)

    # 회전하는 코드를 재귀호출보다 아래에 적어야, 돌아갈지말지 모든 톱니바퀴를 다 체크하고나서 실제로 톱니바퀴를 돌릴 수 있다.
    # 회전하기
    if g_direc == 1: # 조심! 1이랑 0이 아니라 1이랑 -1이기 때문에 ==1 해줘야함.
        gear[g_num].insert(0, gear[g_num].pop())
    else:
        gear[g_num].append(gear[g_num].pop(0))

for tc in range(1, int(input()) + 1):
    n = int(input())
    gear = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(n):
        g_num, g_direc = map(int, input().split())
        act(g_num-1, g_direc, 0) # 1번 톱니바퀴가 gear[0] 이니까 g_num -1을 넣어준다.

    result = 0
    for i in range(4):
        if gear[i][0]:
            result += 2 ** i
    print("#{} {}".format(tc, result))