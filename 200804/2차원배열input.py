N = 3

# board = list()
# for n in range(N):
#     board.append(list(map(int, input().split())))

#이거 한 줄로
# board = [list(map(int, input().split())) for _ in range(N)]


board = list()
board.append([1,2,3])
board.append([1,2,3])
board.append([1,2,3])
board.append([1,2,3])
board.append([1,2,3])

print(board)  # 이렇게 출력하면   [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

for row in board:
    print(row)   #이렇게 출력하면
    #[1, 2, 3]
    #[1, 2, 3]
    #[1, 2, 3]
    #[1, 2, 3]

board2 = [list(map(int, input().split())) for _ in range(N)]
#input이렇게 넣었을 때
#123
#123
#123
print(board2) #출력: [[123], [123], [123]]

#input이렇게 넣었을 때
#1 2 3
#1 2 3
#1 2 3
print(board2) # 출력: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]