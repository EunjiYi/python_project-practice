T = int(input())
for tc in range(1, T+1):

    def BubbleSort(a):
        for i in range(len(a)-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]

    N = int(input())
    data = list(map(int, input().split()))

    BubbleSort(data)
    # data가 오름차순 정렬됨.

    result = [0] * 10
    result[0] = data[len(data)-1]
    result[1] = data[0]
    result[2] = data[len(data)-2]
    result[3] = data[1]
    result[4] = data[len(data)-3]
    result[5] = data[2]
    result[6] = data[len(data)-4]
    result[7] = data[3]
    result[8] = data[len(data)-5]
    result[9] = data[4]

    #print(result) # 이렇게 출력하면 #1 [10, 1, 9, 2, 8, 3, 7, 4, 6, 5] 이렇게 나옴.
    print('#{}'.format(tc), end=" ")
    for i in range(len(result)):
        print(result[i], end = " ")
    print()