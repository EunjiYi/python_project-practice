T = int(input())
for tc in range(1, T+1):
    N = int(input())

    def getResult(a): #종이를 붙여야 될 공간이 a만큼 있을 때 그 경우의 수를 반환하는 함수
        if a == 0:
            return 1
        elif a < 0:
            return 0
        else:
            return getResult(a-10)+getResult(a-20)*2



    print("#{} {}".format(tc, getResult(N)))
