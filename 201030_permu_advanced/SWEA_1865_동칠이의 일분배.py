def backtrack(idx, pro):
    global max_pro
    ### 생각도 못한 것
    # 최대의 확률을 구하는데, 곱하는 값이 1보다 작기 때문에 곱할수록 값이 작아진다.
    # 그러니까 차라리 이 이후로 직원들한테 일 배분안하는게 더 이득..
    # 와우..ㅠ
    if pro <= max_pro: # 여기서 등호 빼먹어도 시간초과라는데
        return
    # 애초에 이 두 줄을 안적어도 시간이나 메모리효율이 비슷함. 애초에 아래에 내가 짠 코드에서 이 경우가 걸러짐
    # 그래서 내가 짠 코드에선 이 두 줄이 없었다.
    # 암튼 이런 것 기억해두면 좋으니 적어놓겠다.

    # 여기부턴 내가 아는 백트래킹
    if idx >= N:
        if max_pro < pro:
            max_pro = pro
        return

    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            if pro * matrix[idx][i]/100 > max_pro:
                backtrack(idx + 1, pro * matrix[idx][i]/100)
            selected[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N =  int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    selected = [0] * N

    #구할 값은 최대곱
    max_pro = float('-inf')
    backtrack(0,1)
    #print(f'#{tc} ',round(max_pro * 100, 6) ) round쓰면 마지막 0이 안찍힘
    #print('#%d %0.6f' %(tc, round(max_pro * 100, 6 ))) 그래서 c언어형식으로 쓰자.
    #아니면 format써야함
    print(f'#{tc}', end = " ")
    print(format(max_pro * 100, '.6f'))