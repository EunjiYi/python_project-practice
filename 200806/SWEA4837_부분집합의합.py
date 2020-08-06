T = int(input())
for tc in range(1, T+1):

    N, K = map(int,input().split())

    n = 12
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    cnt = 0
    for i in range(1<<n):
        subSet = []

        for j in range(n):
            if i & (1<<j):
                subSet.append(arr[j])
                #print(subSet)
                #부분집합 하나 생김.
                #여기 안에서 if len(subSet) == N and sum(subSet) == K: 조건을 걸면
                #만약 [1,2,3,4]인 부분집합 만드는 중(append)인데 [1,2,3 까지만 생겼을 때 이미 조건에 만족해서 cnt를 증가시켜버림.
                #즉 부분집합 다 만들고(for 문 나와서) - 조건을 걸어야한다.
        #=============================================
        #생긴 부분집합에 조건걸기
        if len(subSet) == N and sum(subSet) == K:
            cnt += 1

    print("#{} {}".format(tc, cnt))