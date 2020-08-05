arr = [[1,2,3,4],  #처음 1에서 시작 -> 왼쪽 막혀서 못감 -> 오른쪽 2 -> 위에 막혀서 못감 -> 아래 5 -> (y가 바뀌니까 이제 2에서 시작) ->
       [5,6,7,8],  # 왼쪽 1 -> 오른쪽 -> 3 -> 위에 못가 -> 아래 6 -> (이제 3에서 시작) -> 2->4-> 막힘 ->7
       [9,10,11,12]
       ]

N = len(arr)
M =len(arr[0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 대각선도 갈 수 있다고 하면 8가지.
#dx = [0, 0, -1, 1, 1, -1, 1, -1]
#dy = [-1, 1, 0, 1, 1, -1, -1, 1]

for x in range(N):
    for y in range(N):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if testX >= 0 and testX < N and testY >= 0 and testX < M: #인덱스체크를 항상 먼저하자. 인덱스를 벗어나면 안되니까.
            #이것은 파이썬만 가능
            ##if 0 <= testX < N  and 0 <= testY < M:

            #이렇게 하는 사람도 있다.
            ##if testX < 0 or testX >= N: continue
            ##if testX < 0 or testX >= M: continue
                print(arr[testX][testY],end = " ")

#visited : 방문한거 또 방문 안하려면 이런걸로 체크한다.