# 기본 아이디어.
arr = [[0]* 10 for _ in range(10)]

x, y = 3, 4
size = 3

for i in range(x, x+size):
    for j in range(y, y+size):
        arr[i][j] = 1
for lst in arr:
    print(*lst)


# for row in arr:
#     print(row)

#DP나 백트래킹도 완전검색이라 생가하자. 효율적인 완전검색.