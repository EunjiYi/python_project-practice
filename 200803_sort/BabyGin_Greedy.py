num = 456789
c = [0] * 12  #12로 한 이유: 9 뒤에 뒤에도 검사하니까. 없는 인덱스 조회 방지

for i in range(6):
    c[num % 10] += 1  #c[num % 10] = c[num % 10] + 1
    num //= 10       # num = num // 10


i = 0
tri = run = 0 #초기화
while i < 10: #C[]의 0~9까지 훑을거다
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue  #  컨틴유하는 이유:  i += 1 안 하려고 -> 같은게 6개있으면 어떡할거야.  저 반복문을 2번 돌려야되니까.
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if tri + run == 2: print("Baby-Gin")
else: print("Lose")