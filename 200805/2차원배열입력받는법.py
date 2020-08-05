'''
3 3
1 2 3
4 5 6
7 8 9
'''

N, M = map(int, input().split())

# 1.
mylist = [0 for _ in range(N)]  #파이썬은 인터프리터가 줄 단위로 읽어오니까
#mylist = [0] * N

for i in range(N):
    mylist[i] = list(map(int, input().split()))
print(mylist)  #[[1,2,3].[4,5,6],[7,8,9]]



#2.
mylist = []
for i in range(N):
    mylist.append(list(map(int, input().split())))
print(mylist) #[[1,2,3].[4,5,6],[7,8,9]]


#3. 간단하니까 이거 많이 쓴다. list comprehension
mylist = [list(map(int, input().split())) for _ in range(N)]
print(mylist)


#방문체크
#visited = [ [0] * 3 ] *3
# 절대 이렇게 하면 안됨! 이렇게 하면 똑같은 [0] * 3 가 복사가 되서
# 열 별로 같이 움직인다.
# (0,1)체크하면 1열 (0,0) (0,1) (0,2) 전부 다 체크가 되어버림 - 이렇게 쓰면 안된다.

N = 3 #행
M = 4 #열
#2차원배열을 0으로 초기화 하는 방법
visited = [[0 for _ in range(M)] for _ in range(N)] #주의# 열을 먼저 만들고 행을 만들어야한다.
#아니면 visited = [ [0] * M for _ in range(N) ] 이렇게 해라.
print(visited)